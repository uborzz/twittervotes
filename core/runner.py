from concurrent.futures import ProcessPoolExecutor

import rx

from typing import List


class Runner:
    def __init__(self, on_success, on_error, on_complete):
        self._on_success = on_success
        self._on_error = on_error
        self._on_complete = on_complete

    def exec(self, func, items):
        observables: List[rx.Observable] = []

        with ProcessPoolExecutor() as executor:
            for item in items.values():
                _future = executor.submit(func, item)
                observables.append(rx.from_future(_future))
            all_observables = rx.merge(*observables)
            all_observables.subscribe(
                self._on_success, self._on_error, self._on_complete,
            )
