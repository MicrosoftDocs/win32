---
title: EN\_OBJECTPOSITIONS notification code
description: Notifies a rich edit control's parent window when the control reads in objects. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: '1965185f-8a13-4989-8574-af8b9b30f6b0'
keywords: ["EN_OBJECTPOSITIONS notification code Windows Controls"]
topic_type:
- apiref
api_name:
- EN_OBJECTPOSITIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EN\_OBJECTPOSITIONS notification code

Notifies a rich edit control's parent window when the control reads in objects. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_OBJECTPOSITIONS

    pOjectPositions = (OBJECTPOSITIONS *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**OBJECTPOSITIONS**](objectpositions.md) structure.

</dd> </dl>

## Return value

Return zero to continue the **Read** operation.

Return a nonzero value to stop the **Read** operation.

## Remarks

To receive an EN\_OBJECTPOSITIONS notification code, specify the [**ENM\_OBJECTPOSITIONS**](rich-edit-control-event-mask-flags.md#enm-objectpositions) flag in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_SETEVENTMASK**](em-seteventmask.md)
</dt> <dt>

[**OBJECTPOSITIONS**](objectpositions.md)
</dt> <dt>

[**WM\_NOTIFY**](wm-notify.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> </dl>

 

 





