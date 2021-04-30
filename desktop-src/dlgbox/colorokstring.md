---
title: COLOROKSTRING message (Commdlg.h)
description: A Color dialog box sends the COLOROKSTRING registered message to your hook procedure, CCHookProc, when the user selects a color and clicks the OK button.
ms.assetid: 18b28558-1262-4c88-becf-76ce799b7542
keywords:
- COLOROKSTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- COLOROKSTRING
- COLOROKSTRINGA
- COLOROKSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# COLOROKSTRING message

A **Color** dialog box sends the **COLOROKSTRING** registered message to your hook procedure, [*CCHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpcchookproc), when the user selects a color and clicks the **OK** button. The hook procedure can accept the color and allow the dialog box to close, or reject the color and force the dialog box to remain open.


```C++
#define COLOROKSTRING TEXT("commdlg_ColorOK")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**CHOOSECOLOR**](/windows/win32/api/commdlg/ns-commdlg-choosecolora-r1) structure. The **rgbResult** member of this structure contains the RGB color value of the selected color.

</dd> </dl>

## Return value

If the hook procedure returns zero, the **Color** dialog box accepts the selected color and closes.

If the hook procedure returns a nonzero value, the **Color** dialog box rejects the selected color and remains open.

## Remarks

The hook procedure must specify the **COLOROKSTRING** constant in a call to the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function to get the identifier of the message sent by the dialog box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **COLOROKSTRINGW** (Unicode) and **COLOROKSTRINGA** (ANSI)<br/>                                    |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CHOOSECOLOR**](/windows/win32/api/commdlg/ns-commdlg-choosecolora-r1)
</dt> <dt>

[**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

