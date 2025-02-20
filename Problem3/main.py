def horner_method(coefficients, x):
    #输入区
    coefficients.reverse()
    result = coefficients[0]
    for a in coefficients[1:]:
        result = result*x + a
    return result

if __name__ == "__main__":
    # 读取输入：第一行为 x0，第二行为多项式系数（从高次到低次排列）
    x0 = float(input('x0=').strip())
    coefficients = list(map(float, input('c_a=').split()))
    
    # 计算并输出结果
    print(horner_method(coefficients, x0))
