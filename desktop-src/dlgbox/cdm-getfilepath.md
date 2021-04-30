---
title: CDM_GETFILEPATH message (Commdlg.h)
description: Retrieves the path and file name of the selected file in an Explorer-style Open or Save As dialog box.
ms.assetid: fad8c5e2-9838-45a8-8c51-4326c989d939
keywords:
- CDM_GETFILEPATH message Dialog Boxes
topic_type:
- apiref
api_name:
- CDM_GETFILEPATH
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CDM\_GETFILEPATH message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](/windows/win32/shell/common-file-dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Retrieves the path and file name of the selected file in an Explorer-style **Open** or **Save As** dialog box. The dialog box must have been created with the **OFN\_EXPLORER** flag; otherwise, the message fails.


```C++
#define WM_USER                  0x0400
#define CDM_FIRST               (WM_USER + 100)
#define CDM_GETFILEPATH         (CDM_FIRST + 0x0001)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The size, in characters, of the *lParam* buffer. For the ANSI version, this is the number of bytes; for the Unicode version, this is the number of characters.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that receives the file name and path.

</dd> </dl>

## Return value

If the message succeeds, the return value is the size, in characters, of the file name and path string, including the terminating NULL character. This is either the number of bytes or characters copied to the buffer, or the required buffer size if the buffer is too small.

If an error occurs, the return value is less than zero.

## Remarks

The corresponding macro is as follows:

``` syntax
int CommDlg_OpenSave_GetFilePath(hwnd, lparam, wparam); 
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetOpenFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getopenfilenamea)
</dt> <dt>

[**GetSaveFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getsavefilenamea)
</dt> <dt>

[**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

