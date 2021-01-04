---
title: EN_LOWFIRTF notification code (Richedit.h)
description: Notifies the parent window of a Microsoft Rich Edit control that an unsupported Rich Text Format (RTF) keyword was received. A Rich Edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 3b18320b-ebc3-44f2-a93c-e967a028c522
keywords:
- EN_LOWFIRTF notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_LOWFIRTF
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_LOWFIRTF notification code

Notifies the parent window of a Microsoft Rich Edit control that an unsupported Rich Text Format (RTF) keyword was received. A Rich Edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_LOWFIRTF

    penLowfiRTF = (ENLOWFIRTF *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

The [**ENLOWFIRTF**](/windows/desktop/api/Richedit/ns-richedit-enlowfirtf) structure.

</dd> </dl>

## Return value

This notification code does not return a value.

## Remarks

To receive an EN\_LOWFIRTF notification, specify the ENM\_LOWFIRTF flag in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ENLOWFIRTF**](/windows/desktop/api/Richedit/ns-richedit-enlowfirtf)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> </dl>

 

 





