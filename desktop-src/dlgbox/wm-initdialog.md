---
title: WM_INITDIALOG message (Winuser.h)
description: Sent to the dialog box procedure immediately before a dialog box is displayed. Dialog box procedures typically use this message to initialize controls and carry out any other initialization tasks that affect the appearance of the dialog box.
ms.assetid: bc4f4718-1dab-48db-ae3b-5a81a7be2644
keywords:
- WM_INITDIALOG message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_INITDIALOG
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INITDIALOG message

Sent to the dialog box procedure immediately before a dialog box is displayed. Dialog box procedures typically use this message to initialize controls and carry out any other initialization tasks that affect the appearance of the dialog box.


```C++
#define WM_INITDIALOG                   0x0110
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the control to receive the default keyboard focus. The system assigns the default keyboard focus only if the dialog box procedure returns **TRUE**.

</dd> <dt>

*lParam* 
</dt> <dd>

Additional initialization data. This data is passed to the system as the *lParam* parameter in a call to the [**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama), [**CreateDialogParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogparama), [**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama), or [**DialogBoxParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxparama) function used to create the dialog box. For property sheets, this parameter is a pointer to the [**PROPSHEETPAGE**](/windows/desktop/api/prsht/ns-prsht-propsheetpagea_v2) structure used to create the page. This parameter is zero if any other dialog box creation function is used.

</dd> </dl>

## Return value

The dialog box procedure should return **TRUE** to direct the system to set the keyboard focus to the control specified by *wParam*. Otherwise, it should return **FALSE** to prevent the system from setting the default keyboard focus.

The dialog box procedure should return the value directly. The **DWL\_MSGRESULT** value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

## Remarks

The control to receive the default keyboard focus is always the first control in the dialog box that is visible, not disabled, and that has the **WS\_TABSTOP** style. When the dialog box procedure returns **TRUE**, the system checks the control to ensure that the procedure has not disabled it. If it has been disabled, the system sets the keyboard focus to the next control that is visible, not disabled, and has the **WS\_TABSTOP**.

An application can return **FALSE** only if it has set the keyboard focus to one of the controls of the dialog box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama)
</dt> <dt>

[**CreateDialogParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogparama)
</dt> <dt>

[**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama)
</dt> <dt>

[**DialogBoxParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxparama)
</dt> <dt>

[**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**PROPSHEETPAGE**](/windows/desktop/api/prsht/ns-prsht-propsheetpagea_v2)
</dt> </dl>

 

