---
title: FILEOKSTRING message
description: An Open or Save As dialog box sends the FILEOKSTRING registered message to your hook procedure, OFNHookProc, when the user specifies a file name and clicks the OK button.
ms.assetid: 32bf3cc7-76a2-4b78-81d7-682b088c4e14
keywords:
- FILEOKSTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- FILEOKSTRING
- FILEOKSTRINGA
- FILEOKSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# FILEOKSTRING message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](https://msdn.microsoft.com/en-us/library/Bb776913(v=VS.85).aspx). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

An **Open** or **Save As** dialog box sends the **FILEOKSTRING** registered message to your hook procedure, [*OFNHookProc*](https://msdn.microsoft.com/en-us/library/ms646931(v=VS.85).aspx), when the user specifies a file name and clicks the **OK** button. The hook procedure can accept the file name and allow the dialog box to close, or reject the file name and force the dialog box to remain open.


```C++
#define FILEOKSTRING TEXT("commdlg_FileNameOK")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna) structure. The **lpstrFile** member of this structure contains the drive, path, and file name specified by the user.

</dd> </dl>

## Return value

If the hook procedure returns zero, the **Open** or **Save As** dialog box accepts the specified file name and closes.

If the hook procedure returns a nonzero value, the **Open** or **Save As** dialog box rejects the specified file name and remains open.

## Remarks

The hook procedure must specify the **FILEOKSTRING** constant in a call to the [**RegisterWindowMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644947) function to get the identifier for the message sent by the dialog box.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **FILEOKSTRINGW** (Unicode) and **FILEOKSTRINGA** (ANSI)<br/>                                      |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CDN\_FILEOK**](cdn-fileok.md)
</dt> <dt>

[**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna)
</dt> <dt>

[**RegisterWindowMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644947)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





