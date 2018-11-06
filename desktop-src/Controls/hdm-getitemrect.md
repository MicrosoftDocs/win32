---
title: HDM_GETITEMRECT message
description: Gets the bounding rectangle for a given item in a header control. You can send this message explicitly or use the Header\_GetItemRect macro.
ms.assetid: b483ef97-3700-425b-8160-81c673850f68
keywords:
- HDM_GETITEMRECT message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETITEMRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# HDM\_GETITEMRECT message

Gets the bounding rectangle for a given item in a header control. You can send this message explicitly or use the [**Header\_GetItemRect**](/windows/desktop/api/Commctrl/nf-commctrl-header_getitemrect) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the header control item for which to retrieve the bounding rectangle.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that receives the bounding rectangle information.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





