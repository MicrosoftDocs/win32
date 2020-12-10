---
title: EN_SELCHANGE notification code (Richedit.h)
description: Notifies a rich edit control's parent window that the current selection has changed. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 53d47b53-a73c-4652-889c-2374f8e99382
keywords:
- EN_SELCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_SELCHANGE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_SELCHANGE notification code

Notifies a rich edit control's parent window that the current selection has changed. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_SELCHANGE

    pSelChange = (SELCHANGE *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**SELCHANGE**](/windows/desktop/api/Richedit/ns-richedit-selchange) structure that receives information about the selection.

</dd> </dl>

## Return value

This notification code does not return a value.

## Remarks

To receive EN\_SELCHANGE notification codes, specify [**ENM\_SELCHANGE**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

This notification code is sent when the caret position changes and no text is selected (the selection is empty). The caret position can change when the user clicks the mouse, types, or presses an arrow key.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**SELCHANGE**](/windows/desktop/api/Richedit/ns-richedit-selchange)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





