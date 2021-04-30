---
title: EN_REQUESTRESIZE notification code (Richedit.h)
description: Notifies a rich edit control's parent window that the control's contents are either smaller or larger than the control's window size. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 708c23b1-7b81-46f1-9595-46230693855d
keywords:
- EN_REQUESTRESIZE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_REQUESTRESIZE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_REQUESTRESIZE notification code

Notifies a rich edit control's parent window that the control's contents are either smaller or larger than the control's window size. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_REQUESTRESIZE

    pReqResize = (REQRESIZE *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**REQRESIZE**](/windows/desktop/api/Richedit/ns-richedit-reqresize) structure that receives the requested size.

</dd> </dl>

## Return value

This notification code does not return a value.

## Remarks

To support the bottomless behavior of a rich edit control, the parent window must resize the control when it receives this notification code.

To receive EN\_REQUESTRESIZE notification codes, specify [**ENM\_REQUESTRESIZE**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

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

[**REQRESIZE**](/windows/desktop/api/Richedit/ns-richedit-reqresize)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





