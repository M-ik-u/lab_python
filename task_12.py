b_min = 60
b_sms = 30
b_wifi = 1
b_price = 24.99

e_min_p = 0.89
e_sms_p = 0.59
e_mb_p = 0.79

tax =0.02

used_min = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_wifi = float(input("Введите количество израсходованного инета(гб): "))

used_wifi_mb = used_wifi * 1024

e_min = max(0, used_min - b_min)
e_sms = max(0, used_sms - b_sms)
e_wifi = max(0,used_wifi_mb - b_wifi * 1024)

e_min_c = e_min * e_min_p
e_sms_c = e_sms * e_sms_p
e_wifi_c = e_wifi * e_mb_p

total_btax = b_price + e_wifi_c + e_sms_c + e_min_c

tax_c = total_btax * tax

total = total_btax + tax_c

print(f"\nБазовая стоимость {b_price} руб")

if e_min > 0:
    print(f"доп мин ({e_min} мин): {e_min_c:.2f} руб")
if e_sms > 0:
    print(f"доп SMS ({e_sms}): {e_sms_c:.2f} руб")
if e_wifi > 0:
    print(f"доп wifi ({e_wifi} мб): {e_wifi_c:.2f} руб")

print(f"налог (2%): {tax_c:.2f} руб"
      f"\nК оплате: {total:.2f} руб")





