---
title: HDM_SETITEM message (Commctrl.h)
description: Sets the attributes of the specified item in a header control. You can send this message explicitly or use the Header\_SetItem macro.
ms.assetid: c8f0d526-3ebe-48c5-8aea-ea3703e2d983
keywords:
- HDM_SETITEM message Windows Controls
topic_type:
- apiref
api_name:
- HDM_SETITEM
- HDM_SETITEMA
- HDM_SETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_SETITEM message

Sets the attributes of the specified item in a header control. You can send this message explicitly or use the [**Header\_SetItem**](/windows/desktop/api/Commctrl/nf-commctrl-header_setitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The current index of the item whose attributes are to be changed.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure that contains item information. When this message is sent, the **mask** member of the structure must be set to indicate which attributes are being set.

</dd> </dl>

## Return value

Returns nonzero upon success, or zero otherwise.

## Remarks

The [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure that supports this message supports item order and image list information. By using these members, you can control the order in which items are displayed and specify images to appear with items.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDM\_SETITEMW** (Unicode) and **HDM\_SETITEMA** (ANSI)<br/>                   |



 

 





