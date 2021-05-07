---
title: SHAREVISTRING message (Commdlg.h)
description: An Open or Save As dialog box sends the SHAREVISTRING registered message to your hook procedure, OFNHookProc, if a sharing violation occurs for the selected file when the user clicks the OK button.
ms.assetid: 53884497-4872-4aa8-b56e-2bb98df58fed
keywords:
- SHAREVISTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- SHAREVISTRING
- SHAREVISTRINGA
- SHAREVISTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SHAREVISTRING message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](../shell/common-file-dialog.md). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

An **Open** or **Save As** dialog box sends the **SHAREVISTRING** registered message to your hook procedure, [*OFNHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpofnhookproc), if a sharing violation occurs for the selected file when the user clicks the **OK** button.


```C++
#define SHAREVISTRING TEXT("commdlg_ShareViolation")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea) structure. The **lpstrFile** member of this structure contains the file name that caused the sharing violation.

</dd> </dl>

## Return value

The hook procedure must return one of the following values to indicate how the dialog box should handle the sharing violation.



| Return code/value                                                                                                                                           | Description                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**OFN\_SHAREFALLTHROUGH**</dt> <dt>2</dt> </dl> | Accept the file name<br/>                                                                                            |
| <dl> <dt>**OFN\_SHARENOWARN**</dt> <dt>1</dt> </dl>      | Reject the file name but do not warn the user. The application is responsible for displaying a warning message.<br/> |
| <dl> <dt>**OFN\_SHAREWARN**</dt> <dt>0</dt> </dl>        | Reject the file name and displays a warning message (the same result as if there were no hook procedure).<br/>       |



 

## Remarks

The hook procedure must specify the **SHAREVISTRING** constant in a call to the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function to get the identifier for the message sent by the dialog box.

The dialog box sends the **SHAREVISTRING** registered message only if you did not specify the **OFN\_SHAREAWARE** flag in the **Flags** member of the [**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea) structure when you created the dialog.

If the hook procedure returns an undefined value, the dialog box responds as if **OFN\_SHAREWARN** was returned.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **SHAREVISTRINGW** (Unicode) and **SHAREVISTRINGA** (ANSI)<br/>                                    |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CDN\_SHAREVIOLATION**](cdn-shareviolation.md)
</dt> <dt>

[**OPENFILENAME**](/windows/win32/api/commdlg/ns-commdlg-openfilenamea)
</dt> <dt>

[**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

