---
title: 台大系所/學院/編碼對照
---

## 資料來源

`NTU_dept_code.txt`: 台大課程網系所下拉選單

## 內容

`tojson.py`: 將 `NTU_dept_code.txt` 系所編碼轉換成 3 碼、處理部分**系所簡稱**
(例如，`心理學系`/`心理系`) 以及**編碼-系所-學院對照**的問題。

- Input: `NTU_dept_code.txt`
- Output:
  - `data/name2std.json`:     系所名稱/別名對照
  - `data/name2code.json`:    系所 -> 編碼
  - `data/code2name.json`:    編碼 -> 系所
  - `data/dept2college.json`: 系所 -> 學院

### 檔案目錄

```{.numberLines}
./
├─ NTU_dept_code.txt
├─ README.md
├─ tojson.py
├─ data/
│      ├─ code2name.json
│      ├─ dept2college.json
│      ├─ name2code.json
│      └─ name2std.json
│ 
└─ legacy/
```

### 資料更新

若發現當前的資料不敷使用或不正確，請修改 `NTU_dept_code.txt` 的資料後，再於 cmd 執行:

```{.python
python tojson.py
```

### 舊版

2022.11.24 前的版本輸出資料為 `.tsv` 檔，資料及程式碼見 `legacy/`。
