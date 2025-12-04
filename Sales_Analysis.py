import numpy as np

def generate_sales(normal_days=350, outlier_days=15, seed=42):
    """
    إنشاء بيانات المبيعات:
    - normal_days: عدد أيام المبيعات الطبيعية
    - outlier_days: عدد الأيام الشاذة (انفجارات المبيعات)
    - seed: لتثبيت الأرقام العشوائية
    """
    np.random.seed(seed)
    normal_sales = np.random.uniform(5, 150, normal_days)
    outliers = np.random.randint(250, 400, outlier_days)
    sales = np.concatenate([normal_sales, outliers])
    np.random.shuffle(sales)
    return sales

def remove_outliers(sales, threshold=250):
    """إزالة الشواذ من المبيعات"""
    return sales[sales < threshold]

def calculate_stats(sales, label="Sales"):
    """حساب المتوسط والانحراف المعياري والقيم القصوى والدنيا"""
    print(f"{label} stats:")
    print("Mean:", np.mean(sales))
    print("Std:", np.std(sales))
    print("Variance:", np.var(sales))
    print("Min:", np.min(sales))
    print("Max:", np.max(sales))
    print("-" * 40)

def flag_unusual_days(sales, mean, std):
    """طباعة الأيام الشاذة بناءً على المتوسط والانحراف المعياري"""
    upper = mean + std
    lower = mean - std
    for i, value in enumerate(sales, start=1):
        if value > upper or value < lower:
            print(f"Day {i}: Sale = {value} <-- Unusual")
        else:
            print(f"Day {i}: Sale = {value}")

def calculate_percentiles(sales):
    """حساب المئينات وأيامها"""
    p25 = np.percentile(sales, 25)
    p50 = np.percentile(sales, 50)
    p75 = np.percentile(sales, 75)

    days_p25 = np.sum(sales < p25)
    days_p50 = np.sum(sales < p50)
    days_p75 = np.sum(sales < p75)

    print("Percentiles (without outliers):")
    print("25th percentile:", p25, "-> Days under:", days_p25)
    print("50th percentile (median):", p50, "-> Days under:", days_p50)
    print("75th percentile:", p75, "-> Days under:", days_p75)
    print("-" * 40)

def weekly_average(sales, window=7):
    """حساب المتوسط الأسبوعي لكل 7 أيام"""
    weekly_avg = [np.mean(sales[i:i+window]) for i in range(0, len(sales), window)]
    weekly_avg = [float(x) for x in weekly_avg]
    print("Weekly averages:", weekly_avg)
    print("Number of weeks:", len(weekly_avg))

def main():
    sales = generate_sales()
    calculate_stats(sales, label="All Sales")

    sales_clean = remove_outliers(sales)
    calculate_stats(sales_clean, label="Sales without outliers")

    mean_clean = np.mean(sales_clean)
    std_clean = np.std(sales_clean)
    flag_unusual_days(sales, mean_clean, std_clean)

    calculate_percentiles(sales_clean)
    weekly_average(sales_clean)

if __name__ == "__main__":
    main()
