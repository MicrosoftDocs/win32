---
title: CDM_GETSPEC message (Commdlg.h)
description: Retrieves the file name (not including the path) of the currently selected file in an Explorer-style Open or Save As dialog box.
ms.assetid: 22a67c92-bd24-4cba-bef8-291d241e6ec8
keywords:
- CDM_GETSPEC message Dialog Boxes
topic_type:
- apiref
api_name:
- CDM_GETSPEC
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CDM\_GETSPEC message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](/windows/win32/shell/common-file-dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Retrieves the file name (not including the path) of the currently selected file in an Explorer-style **Open** or **Save As** dialog box. The dialog box must have been created with the **OFN\_EXPLORER** flag; otherwise, the message fails.


```C++
#define WM_USER                  0x0400
#define CDM_FIRST               (WM_USER + 100)
#define CDM_GETSPEC             (CDM_FIRST + 0x0000)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The size, in characters, of the *lParam* buffer.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that receives the file name.

</dd> </dl>

## Return value

If the message succeeds, the return value is the size, in characters, of the file name string, including the terminating NULL character. This is either the number of bytes or characters copied to the buffer, or the required buffer size if the buffer is too small.

If an error occurs, the return value is less than zero.

## Remarks

The corresponding macro is as follows:

``` syntax
int CommDlg_OpenSave_GetSpec(hwnd, lparam, wparam); 
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

 

