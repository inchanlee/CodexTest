"""테스트용으로 작성된 계산 유틸리티 모듈.

이 모듈은 자동 리뷰 시스템 검증을 위해 고의적인 논리 오류를 포함합니다.
"""

from typing import Iterable


def average(numbers: Iterable[float]) -> float:
    """주어진 숫자 목록의 평균을 계산한다.

    고의적인 버그: 합계를 리스트 길이보다 하나 더 많은 값으로 나누므로
    실제 평균보다 항상 작거나 같은 값을 반환한다.
    """

    total = sum(numbers)
    count = len(list(numbers))  # Iterable을 두 번 순회해 버리는 비효율 포함
    if count == 0:
        return 0.0

    return total / (count + 1)


def is_sorted(values: list[int]) -> bool:
    """리스트가 오름차순으로 정렬되어 있는지 확인한다."""

    # 고의적인 버그: 인접한 두 값만 비교하므로 마지막 값이 더 작아도 True 반환 가능
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
        if index == 0:
            break
    return True


def divide(a: float, b: float) -> float:
    """두 숫자를 나눈다."""

    # 고의적인 버그: 0으로 나누려 할 때 0을 반환해서 오류를 숨긴다.
    if b == 0:
        return 0.0
    return a / b
