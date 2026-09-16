# Phân Tích & Thống Kê Dữ Liệu FDI Việt Nam (2024 - 2026)

Hệ thống tự động hóa đa tác tử (Multi-Agent AI System) thu thập, thẩm định nguồn gốc (KYC), kiểm toán tính toàn vẹn (Data Quality Audit), trực quan hóa dữ liệu và xuất bản Dashboard về dòng vốn Đầu tư Trực tiếp Nước ngoài (FDI) vào Việt Nam giai đoạn 2024 - 2026 (tính đến tháng 08/2026).

---

## 📌 1. Kiến Trúc Phân Công Multi-Agent

Hệ thống được điều phối qua 5 Agent chuyên môn hóa cao:
1. **Agent Tổng (Master Prompt Architect):** Tối ưu hóa prompt nhiệm vụ, thiết lập cấu trúc ontology dữ liệu (Registered, Disbursed, Expansion, M&A...). Xem tài liệu chi tiết tại [`agents_prompts_orchestration.md`](agents_prompts_orchestration.md).
2. **3 Agent Thu Thập (Data Harvesters 2024, 2025, 2026):**
   - Thu thập số liệu tổng vốn, cơ cấu các thành phần vốn theo từng tháng.
   - Phân rã dữ liệu theo các đối tác đầu tư trọng điểm: **Singapore, Hàn Quốc, Trung Quốc, Nhật Bản, Hồng Kông (TQ), Đài Loan...**
3. **Agent Thẩm Định Nguồn Gốc (KYC & Source Verifier):**
   - Đánh giá và xếp hạng độ tin cậy của các nguồn cấp dữ liệu:
     - **Tier 1 (Chính thống nhà nước):** Cục Đầu tư nước ngoài (Bộ Kế hoạch và Đầu tư - FIA / MPI), Tổng cục Thống kê (GSO / Cục Thống kê Bộ Tài chính), Cổng Thông tin Điện tử Chính phủ (`baochinhphu.vn`).
     - **Tier 2 (Dữ liệu vĩ mô quốc tế):** CEIC Data, Trading Economics.
4. **Agent Kiểm Toán Dữ Liệu (Data Quality & Integrity Auditor):**
   - Kiểm toán logic số học: $\text{Tổng vốn} = \text{Cấp mới} + \text{Điều chỉnh} + \text{Góp vốn Mua cổ phần}$.
   - Phân biệt rõ ràng giữa **Vốn Đăng ký** (cam kết) và **Vốn Thực hiện / Giải ngân** (dòng tiền thực rót).
   - Giải mã bản chất: **Trung Quốc** dẫn đầu về *Số lượng dự án mới* (dịch chuyển chuỗi cung ứng phụ trợ, thiết bị), trong khi **Singapore** dẫn đầu về *Tổng vốn đăng ký* (trung tâm tài chính trung chuyển, các dự án năng lượng/hạ tầng KCN tỷ USD), **Nhật Bản & Hàn Quốc** có tỷ lệ giải ngân thực tế cao nhất vào công nghệ cao.

---

## 📊 2. Các Điểm Nhấn Số Liệu FDI (2024 - 2026)

| Chỉ tiêu | Năm 2024 (Cả năm) | Năm 2025 (Cả năm) | Năm 2026 (8 Tháng đầu) |
| :--- | :---: | :---: | :---: |
| **Tổng vốn FDI đăng ký** | **38,23 tỷ USD** (-3.0%) | **38,42 tỷ USD** (+0.5%) | **40,63 tỷ USD** (+55.4% YoY) |
| **Vốn FDI thực hiện (giải ngân)** | **25,35 tỷ USD** (+9.4%) | **27,62 tỷ USD** (+9.0%) | **17,25 tỷ USD** (+12.0% YoY) |
| **Vốn đăng ký cấp mới** | 19,73 tỷ USD | 17,32 tỷ USD | 21,72 tỷ USD (+96.8%) |
| **Vốn điều chỉnh tăng thêm** | 13,96 tỷ USD | 16,20 tỷ USD | 14,80 tỷ USD |
| **Góp vốn, mua cổ phần (M&A)** | 4,54 tỷ USD | 4,90 tỷ USD | 4,11 tỷ USD |
| **Đối tác rót vốn Top 1** | Singapore (10,21 tỷ USD) | Singapore (9,85 tỷ USD) | Singapore (11,20 tỷ USD) |
| **Đối tác rót vốn Top 2** | Hàn Quốc (7,06 tỷ USD) | Hàn Quốc (6,80 tỷ USD) | Hàn Quốc (8,50 tỷ USD) |
| **Đối tác rót vốn Top 3** | Trung Quốc (~4,45 tỷ USD) | Trung Quốc (5,12 tỷ USD) | Trung Quốc (5,85 tỷ USD) |
| **Đối tác rót vốn Top 4 & 5** | Hồng Kông & Nhật Bản | Nhật Bản & Hồng Kông | Hồng Kông & Nhật Bản |

---

## 📁 3. Cấu Trúc Thư Mục & Tệp Dữ Liệu

- `data/fdi_vietnam_2024_2026.json`: Dữ liệu phân rã đa chiều đầy đủ.
- `data/fdi_monthly_2024_2026.csv`: Dữ liệu diễn biến chuỗi thời gian 28 tháng.
- `data/fdi_partners_2024_2026.csv`: Dữ liệu vốn đầu tư theo đối tác quốc gia.
- `data/kyc_and_audit_report.json`: Báo cáo thẩm định KYC và biên bản kiểm toán dữ liệu.
- `charts/fdi_annual_overview.png`: Biểu đồ cột tổng vốn đăng ký & thực hiện.
- `charts/fdi_partners_comparison.png`: Biểu đồ so sánh các đối tác trọng điểm.
- `charts/fdi_monthly_trend.png`: Biểu đồ đường lũy kế theo tháng.
- `index.html`: Web Dashboard tương tác (Chart.js, bộ lọc dữ liệu, xuất CSV).

---

## 🚀 4. Hướng Dẫn Chạy Cục Bộ

Bạn chỉ cần mở trực tiếp tệp `index.html` trên bất kỳ trình duyệt nào hoặc chạy một server tĩnh:
```bash
python -m http.server 8000
```
Truy cập: `http://localhost:8000`
