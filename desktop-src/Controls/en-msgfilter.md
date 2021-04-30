---
title: EN_MSGFILTER notification code (Richedit.h)
description: Notifies a rich edit control's parent window of a keyboard or mouse event in the control. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 96cf0047-baae-46cd-82e8-ab6f3f353260
keywords:
- EN_MSGFILTER notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_MSGFILTER
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_MSGFILTER notification code

Notifies a rich edit control's parent window of a keyboard or mouse event in the control. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_MSGFILTER

    pMsgFilter = (MSGFILTER *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**MSGFILTER**](/windows/desktop/api/Richedit/ns-richedit-msgfilter) structure containing information about the keyboard or mouse message. If the parent window modifies this structure and returns a nonzero value, the modified message is processed instead of the original one.

</dd> </dl>

## Return value

Return zero if the control should process the keyboard or mouse event.

Return nonzero if the control should ignore the keyboard or mouse event.

## Remarks

To receive EN\_MSGFILTER notification codes for events, specify one or more of the following flags in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.



| Flag                                                                             | Meaning                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------|
| [**ENM\_KEYEVENTS**](rich-edit-control-event-mask-flags.md)       | To receive notification codes for keyboard events.     |
| [**ENM\_MOUSEEVENTS**](rich-edit-control-event-mask-flags.md)   | To receive notification codes for mouse events.        |
| [**ENM\_SCROLLEVENTS**](rich-edit-control-event-mask-flags.md) | To receive notification codes for a mouse wheel event. |



 

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

[**MSGFILTER**](/windows/desktop/api/Richedit/ns-richedit-msgfilter)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





