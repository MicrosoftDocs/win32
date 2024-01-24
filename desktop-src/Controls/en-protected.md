---
title: EN_PROTECTED notification code (Richedit.h)
description: Notifies a rich edit control's parent window that the user is taking an action that would change a protected range of text. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 29c0cb51-675c-44b1-ad45-5f7140ca5675
keywords:
- EN_PROTECTED notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_PROTECTED
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_PROTECTED notification code

Notifies a rich edit control's parent window that the user is taking an action that would change a protected range of text. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_PROTECTED

    penProtected = (ENPROTECTED *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**ENPROTECTED**](/windows/desktop/api/Richedit/ns-richedit-enprotected) structure containing information about the message that triggered the notification code.

</dd> </dl>

## Return value

Return zero to allow the operation.

Return a nonzero value to prevent the operation.

## Remarks

If zero is returned and the **msg**, **wParam**, and **lParam** members of the [**ENPROTECTED**](/windows/desktop/api/Richedit/ns-richedit-enprotected) structure are changed, the control processes the revised message instead of the original message.

To receive EN\_PROTECTED notification codes, specify [**ENM\_PROTECTED**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

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

[**ENPROTECTED**](/windows/desktop/api/Richedit/ns-richedit-enprotected)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





