---
title: SETRGBSTRING message (Commdlg.h)
description: The hook procedure of a Color dialog box, CCHookProc, can send the SETRGBSTRING registered message to the dialog box to set the current color selection.
ms.assetid: 02d36248-be75-4552-853f-6ac3ec034ebe
keywords:
- SETRGBSTRING message Dialog Boxes
topic_type:
- apiref
api_name:
- SETRGBSTRING
- SETRGBSTRINGA
- SETRGBSTRINGW
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SETRGBSTRING message

The hook procedure of a **Color** dialog box, [*CCHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpcchookproc), can send the **SETRGBSTRING** registered message to the dialog box to set the current color selection.


```C++
#define SETRGBSTRING TEXT("commdlg_SetRGBColor")
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The RGB value of the color to select in the **Color** dialog box. You can use the [**RGB**](/windows/desktop/api/wingdi/nf-wingdi-rgb) macro to specify the red, green, and blue intensities of an RGB color value.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

If *lParam* matches one of the basic colors or one of the 16 custom colors, the dialog box procedure selects that color. The dialog box procedure also updates all the controls in the custom color extension of the **Color** dialog box, if it is open.

If *lParam* does not match a basic or custom color, the dialog box procedure does not change the current color selection, but it does update the custom color controls, if they are visible.

## Examples

The following sample code gets the **SETRGBSTRING** message identifier and then sets the color selection to blue.


```
UINT uiSetRGB;

uiSetRGB = RegisterWindowMessage(SETRGBSTRING);

SendMessage(hdlg, uiSetRGB, 0, (LPARAM) RGB(0, 0, 255)); 
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **SETRGBSTRINGW** (Unicode) and **SETRGBSTRINGA** (ANSI)<br/>                                      |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

[**RGB**](/windows/desktop/api/wingdi/nf-wingdi-rgb)
</dt> <dt>

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

