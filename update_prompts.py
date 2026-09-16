content = """# HỆ THỐNG PROMPT TỐI ƯU HÓA ĐA AGENT: PHÂN TÍCH DỮ LIỆU FDI VIỆT NAM (PHIÊN BẢN ĐỐI SOÁT & PHẢN BIỆN CHUYÊN SÂU)

## 1. Bối Cảnh & Kiến Trúc Multi-Agent Đa Phương Thức (Multimodal)

Để đảm bảo độ chính xác tuyệt đối và khắc phục các sai lệch từ các nguồn tin tổng hợp sớm (như lỗi số liệu FDI Singapore 2025: 9,39 tỷ USD vs 9,85 tỷ USD), hệ thống nâng cấp lên kiến trúc **Đa Agent Chuyên Biệt + Hội đồng Phản biện Kép**:

1. **Agent Tổng (Master Prompt Architect & Chief Auditor):**
   - Định nghĩa quy chuẩn schema, kiểm soát chất lượng, chủ trì phiên phản biện giữa các Agent.
2. **Nhóm 3 Agent Xử Lý Văn Bản Đa Phương Thức (Multimodal Harvesters):**
   - **Agent Text (Văn bản):** Trích xuất câu từ, phân biệt vốn cấp mới, điều chỉnh, GVMCP.
   - **Agent Chart & Table (Bảng biểu/Đồ thị):** Trích xuất chính xác ma trận bảng biểu, số liệu tỷ trọng % và vốn tuyệt đối theo ngành và đối tác.
   - **Agent Vision & Image (Thị giác & Hình ảnh):** Quét các infographic, sơ đồ, biểu đồ phân bổ được nhúng dưới dạng hình ảnh trên cổng thông tin nghiệp vụ.
3. **Cặp 2 Agent KYC & Phản Biện Độc Lập:**
   - **KYC Agent 1 (Domain & Institutional Authority):** Thẩm định domain cấp 1 (`mof.gov.vn`, `fia.mof.gov.vn`, `fdi.mof.gov.vn`).
   - **KYC Agent 2 (Discrepancy & Logic Challenger):** Bắt buộc đối soát chéo từng con số, truy tìm các điểm mâu thuẫn thời điểm chốt sổ (ví dụ: số ước tính giữa tháng 12 vs số chốt sổ ngày 31/12/2025).

---

## 2. Đặc Tả Bộ Prompt Tối Ưu Hóa Giao Việc

### 2.1. Prompt Cho Agent Đọc Văn Bản (Text Extraction Agent)
```text
[NHIỆM VỤ]: Đọc toàn bộ phần nội dung chữ của văn bản báo cáo FDI từ Cục Đầu tư nước ngoài.
[YÊU CẦU]:
1. Trích xuất chính xác con số Vốn thực hiện (giải ngân) và Tổng vốn đăng ký.
2. Trích xuất các số liệu định tính và định lượng về các đối tác dẫn đầu: Singapore, Trung Quốc, Hàn Quốc, Nhật Bản, Hồng Kông.
3. Chú ý các cụm từ chốt sổ: "Tính trong 12 tháng...", "Tính lũy kế đến ngày 31/12...".
```

### 2.2. Prompt Cho Agent Đọc Bảng Biểu & Biểu Đồ (Chart & Table Agent)
```text
[NHIỆM VỤ]: Trích xuất toàn bộ dữ liệu bảng biểu có cấu trúc trong tài liệu.
[YÊU CẦU]:
1. Đọc Bảng Xếp hạng vốn ĐTNN theo đối tác: STT, Tên đối tác, Vốn đăng ký (triệu USD), Tăng/giảm so với cùng kỳ.
2. Đọc Bảng/Số liệu Cơ cấu vốn ĐTNN theo ngành nghề: Tên ngành kinh tế, Tổng vốn đăng ký (Tỷ USD hoặc Triệu USD), Tỷ trọng % so với tổng vốn.
3. Đảm bảo tổng tỷ trọng % của các ngành và các đối tác cộng lại đạt 100% (+/- sai số làm tròn).
```

### 2.3. Prompt Cho Cặp 2 Agent KYC & Phản Biện (Confrontational KYC Reviewers)
```text
[NHIỆM VỤ]: Thẩm định và đối chất số liệu với Agent Tổng.
[YÊU CẦU ĐỐI CHẤT]:
1. Nếu phát hiện số liệu giữa bài viết báo chí và hệ thống nghiệp vụ (fdi.mof.gov.vn) có sự chênh lệch (ví dụ 9,39B vs 9,85B), Agent KYC 2 BẮT BUỘC phải bác bỏ số liệu báo chí và lấy số liệu tại bảng gốc của Cục ĐTNN.
2. Kiểm tra tính toàn vẹn của phân rã ngành nghề: Phải có cả số vốn (USD) và tỷ trọng (%) tương ứng.
3. Tổ chức tranh luận trực tiếp với Agent Tổng trước khi cho phép xuất bản lên GitHub và Web Dashboard.
```
"""

with open(r'agents_prompts_orchestration.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated agents_prompts_orchestration.md successfully!')
