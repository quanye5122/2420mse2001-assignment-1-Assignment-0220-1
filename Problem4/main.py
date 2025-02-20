# main.py

def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result = 0
    for n in range(num_terms):
        exponent_n = 2 ** n
        exponent_next = 2 ** (n + 1)
        
        numerator = (2 ** n) * (x ** (exponent_n - 1)) - (2 ** (n + 1)) * (x ** (exponent_next - 1))
        denominator = 1 - x ** exponent_n + x ** exponent_next

        term = numerator / denominator
        result += term
    
    return result

def right_side(x):
    """
    计算方程右侧的固定值。
    """
    return (1 + 2 * x) / (1 + x + x ** 2)

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    target = right_side(x)
    total = 0
    num_terms = 0

    while True:
        exponent_n = 2 ** num_terms
        exponent_next = 2 ** (num_terms + 1)
        
        numerator = (2 ** num_terms) * (x ** (exponent_n - 1)) - (2 ** (num_terms + 1)) * (x ** (exponent_next - 1))
        denominator = 1 - x ** exponent_n + x ** exponent_next

        term = numerator / denominator
        total += term
        num_terms += 1

        if abs(total - target) < tolerance:
            return num_terms

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"满足条件的最小项数为: {num_terms}")
