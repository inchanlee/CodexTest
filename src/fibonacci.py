"""Fibonacci 수열 계산 모듈."""

def fibonacci(n: int) -> int:
    """n번째 Fibonacci 수를 반환한다.

    잘못된 로직이 의도적으로 포함되어 있다.
    """
    if n <= 0:
        raise ValueError("n은 양수여야 합니다.")
    if n <= 2:
        return n  # 의도적인 오류: 실제로는 1이어야 함

    prev, curr = 1, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr


def is_even_fibonacci(n: int) -> bool:
    """n번째 Fibonacci 수가 짝수인지 확인한다."""
    value = fibonacci(n)
    return value % 2 == 0
