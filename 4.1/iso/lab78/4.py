import numpy as np
import pandas as pd

p = 410  # цена товара
c = 60  # расходы по хранению
k = 90  # расходы по завозу

alpha = 0.5  # коэффициент Гурвица

strategies = [5, 6, 7, 8]
demands = [5, 6, 7, 8]

n = len(strategies)
m = len(demands)

payoff_matrix = np.zeros((n, m))

for i, stock in enumerate(strategies):
    for j, demand in enumerate(demands):
        if stock >= demand:
            # Запас >= спроса: продаем всё что требуется, остаток храним
            profit = p * demand - c * (stock - demand)
        else:
            # Запас < спроса: завозим недостающее, продаем весь спрос
            shortage = demand - stock
            profit = p * demand - k * shortage

        payoff_matrix[i, j] = profit


df_payoff = pd.DataFrame(payoff_matrix, index=[f"Запас {s}" for s in strategies], columns=[f"Спрос {d}" for d in demands])

W = np.min(payoff_matrix, axis=1)

risk_matrix = np.zeros((n, m))
for j in range(m):
    max_profit = np.max(payoff_matrix[:, j])
    for i in range(n):
        risk_matrix[i, j] = max_profit - payoff_matrix[i, j]

df_risk = pd.DataFrame(risk_matrix, index=[f"Запас {s}" for s in strategies], columns=[f"Спрос {d}" for d in demands])

S = np.max(risk_matrix, axis=1)

min_payoff = np.min(payoff_matrix, axis=1)
max_payoff = np.max(payoff_matrix, axis=1)
H = alpha * min_payoff + (1 - alpha) * max_payoff

L = np.mean(payoff_matrix, axis=1)

optimal_wald_idx = np.argmax(W)
optimal_wald_value = W[optimal_wald_idx]

optimal_savage_idx = np.argmin(S)
optimal_savage_value = S[optimal_savage_idx]

optimal_hurwicz_idx = np.argmax(H)
optimal_hurwicz_value = H[optimal_hurwicz_idx]

optimal_laplace_idx = np.argmax(L)
optimal_laplace_value = L[optimal_laplace_idx]

results = pd.DataFrame(
    {
        "Критерий": ["Вальда", "Севиджа", "Гурвица (α=0.5)", "Лапласа"],
        "Оптимальный запас": [
            strategies[optimal_wald_idx],
            strategies[optimal_savage_idx],
            strategies[optimal_hurwicz_idx],
            strategies[optimal_laplace_idx],
        ],
        "Значение критерия": [
            f"{optimal_wald_value:.0f}",
            f"{optimal_savage_value:.0f}",
            f"{optimal_hurwicz_value:.0f}",
            f"{optimal_laplace_value:.2f}",
        ],
    }
)

print("=" * 65)
print("ПЛАТЕЖНАЯ МАТРИЦА")
print(df_payoff)
print()

print("=" * 65)
print("КРИТЕРИЙ ВАЛЬДА")
print("W(αᵢ) = min aᵢⱼ:")
for i, stock in enumerate(strategies):
    print(f"  Запас {stock}: W = {W[i]:.0f}")

print(f"\nОптимальная стратегия: Запас {strategies[optimal_wald_idx]} единиц")
print(f"Гарантированный выигрыш: {optimal_wald_value:.0f} руб.")
print()

print("=" * 65)
print("КРИТЕРИЙ СЕВИДЖА")

print("Матрица рисков rᵢⱼ:")
print(df_risk)
print()

print("S(αᵢ) = max rᵢⱼ:")
for i, stock in enumerate(strategies):
    print(f"  Запас {stock}: S = {S[i]:.0f}")

print(f"\nОптимальная стратегия: Запас {strategies[optimal_savage_idx]} единиц")
print(f"Минимальный максимальный риск: {optimal_savage_value:.0f} руб.")
print()

print("=" * 65)
print(f"КРИТЕРИЙ ГУРВИЦА (α = {alpha})")
print("H(αᵢ) = α × min aᵢⱼ + (1-α) × max aᵢⱼ:")
for i, stock in enumerate(strategies):
    print(f"  Запас {stock}: H = {alpha} × {min_payoff[i]:.0f} + {1 - alpha} × {max_payoff[i]:.0f} = {H[i]:.0f}")

print(f"\nОптимальная стратегия: Запас {strategies[optimal_hurwicz_idx]} единиц")
print(f"Значение критерия: {optimal_hurwicz_value:.0f} руб.")
print()

print("=" * 65)
print("КРИТЕРИЙ ЛАПЛАСА")
print("L(αᵢ) = (1/n) × Σ aᵢⱼ:")
for i, stock in enumerate(strategies):
    print(f"  Запас {stock}: L = {L[i]:.2f}")

print(f"\nОптимальная стратегия: Запас {strategies[optimal_laplace_idx]} единиц")
print(f"Средний выигрыш: {optimal_laplace_value:.2f} руб.")
print()

print("=" * 65)
print(results.to_string(index=False))
