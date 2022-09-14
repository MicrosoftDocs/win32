---
title: HDM_GETITEM message (Commctrl.h)
description: Gets information about an item in a header control. You can send this message explicitly or use the Header\_GetItem macro.
ms.assetid: fb1330d3-fd28-490c-9caa-4b2b5ff86ba0
keywords:
- HDM_GETITEM message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETITEM
- HDM_GETITEMA
- HDM_GETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_GETITEM message

Gets information about an item in a header control. You can send this message explicitly or use the [**Header\_GetItem**](/windows/desktop/api/Commctrl/nf-commctrl-header_getitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the item for which information is to be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure. When the message is sent, the **mask** member indicates the type of information being requested. When the message returns, the other members receive the requested information. If the **mask** member specifies zero, the message returns **TRUE** but copies no information to the structure.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

If the HDI\_TEXT flag is set in the **mask** member of the [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure, the control may change the **pszText** member of the structure to point to the new text instead of filling the buffer with the requested text. Applications should not assume that the text will always be placed in the requested buffer.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDM\_GETITEMW** (Unicode) and **HDM\_GETITEMA** (ANSI)<br/>                   |



 

 





