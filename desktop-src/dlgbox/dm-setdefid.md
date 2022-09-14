---
title: DM_SETDEFID message (Winuser.h)
description: Changes the identifier of the default push button for a dialog box.
ms.assetid: 30720fa1-48cb-42d4-8370-87bdbaa34600
keywords:
- DM_SETDEFID message Dialog Boxes
topic_type:
- apiref
api_name:
- DM_SETDEFID
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DM\_SETDEFID message

Changes the identifier of the default push button for a dialog box.


```C++
#define WM_USER              0x0400
#define DM_SETDEFID         (WM_USER+1)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The identifier of a push button control that will become the default.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is always **TRUE**.

## Remarks

This message is processed by the [**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw) function. To set the default push button, the function can send [**WM\_GETDLGCODE**](wm-getdlgcode.md) and [**BM\_SETSTYLE**](../controls/bm-setstyle.md) messages to the specified control and the current default push button.

Using the **DM\_SETDEFID** message can result in more than one button appearing to have the default push button state. When the system brings up a dialog, it draws the first push button in the dialog template with the default state border. Sending a **DM\_SETDEFID** message to change the default button will not always remove the default state border from the first push button. In these cases, the application should send a [**BM\_SETSTYLE**](../controls/bm-setstyle.md) message to change the first push button border style.

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

[**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw)
</dt> <dt>

[**DM\_GETDEFID**](dm-getdefid.md)
</dt> <dt>

[**WM\_GETDLGCODE**](wm-getdlgcode.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**BM\_SETSTYLE**](../controls/bm-setstyle.md)
</dt> <dt>

[**EM\_SETLIMITTEXT**](../controls/em-setlimittext.md)
</dt> </dl>

 

