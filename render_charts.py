import json
import matplotlib.pyplot as plt
import numpy as np

# Load data
with open(r'data\fdi_vietnam_2024_2026.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# 1. Annual Overview Chart
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
years = ['2024 (Cả năm)', '2025 (Cả năm - Chốt sổ)', '2026 (8 Tháng đầu)']
registered = [38.23, 38.42, 40.63]
implemented = [25.35, 27.62, 17.25]

x = np.arange(len(years))
width = 0.35

rects1 = ax.bar(x - width/2, registered, width, label='Vốn Đăng Ký (Tỷ USD)', color='#2563eb', alpha=0.9)
rects2 = ax.bar(x + width/2, implemented, width, label='Vốn Thực Hiện (Tỷ USD)', color='#10b981', alpha=0.9)

ax.set_ylabel('Tỷ USD ($ Billion)', fontsize=12, fontweight='bold')
ax.set_title('TỔNG VỐN FDI ĐĂNG KÝ VÀ THỰC HIỆN VÀO VIỆT NAM (2024 - 2026)\nNguồn: Cục Đầu tư nước ngoài (fdi.mof.gov.vn / fia.mof.gov.vn)', fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, fontweight='bold')
ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11)
ax.set_ylim(0, 48)

for rect in rects1:
    h = rect.get_height()
    ax.annotate(f'{h:.2f}B', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 4), textcoords='offset points', ha='center', va='bottom', fontweight='bold', color='#1d4ed8')

for rect in rects2:
    h = rect.get_height()
    ax.annotate(f'{h:.2f}B', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 4), textcoords='offset points', ha='center', va='bottom', fontweight='bold', color='#047857')

plt.tight_layout()
fig.savefig(r'charts\fdi_annual_overview.png')
plt.close()
print('Chart 1 updated.')

# 2. Top Partners Comparison Chart (with EXACT 9.39B for Singapore 2025)
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
countries = ['Singapore', 'Trung Quốc', 'Hàn Quốc', 'Nhật Bản', 'Hồng Kông']
# 2024: Sing 10.21, Trung Quốc 4.45, Hàn Quốc 7.06, Nhật 3.68, HK 4.41
c_2024 = [10.21, 4.45, 7.06, 3.68, 4.41]
# 2025 (Official fdi.mof.gov.vn): Sing 9.395, TQ 5.696, HQ 5.292, Nhật 3.732, HK 3.130
c_2025 = [9.395, 5.696, 5.292, 3.732, 3.130]
# 2026 8M
c_2026 = [11.20, 5.85, 8.50, 3.95, 4.80]

x = np.arange(len(countries))
w = 0.25

r1 = ax.bar(x - w, c_2024, w, label='Năm 2024', color='#3b82f6')
r2 = ax.bar(x, c_2025, w, label='Năm 2025 (Chính thức)', color='#8b5cf6')
r3 = ax.bar(x + w, c_2026, w, label='8T/2026', color='#ec4899')

ax.set_ylabel('Vốn Đầu Tư (Tỷ USD)', fontsize=12, fontweight='bold')
ax.set_title('SO SÁNH DÒNG VỐN FDI CỦA CÁC ĐỐI TÁC TRỌNG ĐIỂM (2024 - 2026)\n(Singapore 2025: 9.39 tỷ USD | Trung Quốc: 5.70 tỷ USD | Nhật Bản: 3.73 tỷ USD)', fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=12, fontweight='bold')
ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11)
ax.set_ylim(0, 13.5)

for r_group in [r1, r2, r3]:
    for rect in r_group:
        h = rect.get_height()
        ax.annotate(f'{h:.2f}B', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
fig.savefig(r'charts\fdi_partners_comparison.png')
plt.close()
print('Chart 2 updated.')

# 3. NEW: Sector Breakdown Chart (2024 vs 2025)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), dpi=300)

# 2024 Sectors
labels_2024 = ['Chế biến, chế tạo\n(66.9% | $25.58B)', 'Bất động sản\n(16.5% | $6.31B)', 'Sản xuất điện\n(3.7% | $1.42B)', 'Bán buôn, bán lẻ\n(3.7% | $1.41B)', 'Các ngành khác\n(9.2% | $3.51B)']
sizes_2024 = [25.58, 6.31, 1.42, 1.41, 3.51]
colors = ['#2563eb', '#10b981', '#f59e0b', '#8b5cf6', '#64748b']

ax1.pie(sizes_2024, labels=labels_2024, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize': 9, 'fontweight': 'bold'})
ax1.set_title('CƠ CẤU VỐN FDI THEO NGÀNH NĂM 2024\nTổng vốn: 38.23 tỷ USD', fontsize=12, fontweight='bold')

# 2025 Sectors
labels_2025 = ['Chế biến, chế tạo\n(54.7% | $21.01B)', 'Bất động sản\n(18.5% | $7.11B)', 'Bán buôn, bán lẻ\n(7.8% | $3.00B)', 'Chuyên môn KH&CN\n(5.0% | $1.90B)', 'Các ngành khác\n(14.0% | $5.40B)']
sizes_2025 = [21.01, 7.11, 3.00, 1.90, 5.40]

ax2.pie(sizes_2025, labels=labels_2025, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize': 9, 'fontweight': 'bold'})
ax2.set_title('CƠ CẤU VỐN FDI THEO NGÀNH NĂM 2025\nTổng vốn: 38.42 tỷ USD', fontsize=12, fontweight='bold')

plt.tight_layout()
fig.savefig(r'charts\fdi_sectors_breakdown.png')
plt.close()
print('Chart 3 (Sectors breakdown) created.')
