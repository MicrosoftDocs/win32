---
title: EN_DRAGDROPDONE notification code (Richedit.h)
description: Notifies a rich edit control's parent window that the drag-and-drop operation has completed. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 3c8b95cc-86ef-4aec-b551-11dca50ea5c5
keywords:
- EN_DRAGDROPDONE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_DRAGDROPDONE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_DRAGDROPDONE notification code

Notifies a rich edit control's parent window that the drag-and-drop operation has completed. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_DRAGDROPDONE

    pnmhdr = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure.

</dd> </dl>

## Return value

This notification code does not return a value.

## Remarks

To receive an EN\_DRAGDROPDONE notification code, specify the [**ENM\_DRAGDROPDONE**](rich-edit-control-event-mask-flags.md) flag in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

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

[**EM\_SETEVENTMASK**](em-seteventmask.md)
</dt> </dl>

 

 





