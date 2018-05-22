---
title: HDM\_DELETEITEM message
description: Deletes an item from a header control. You can send this message explicitly or use the Header\_DeleteItem macro.
ms.assetid: '1dd1f233-2812-41ae-8a36-c42b9ac70ffc'
keywords: ["HDM_DELETEITEM message Windows Controls"]
topic_type:
- apiref
api_name:
- HDM_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# HDM\_DELETEITEM message

Deletes an item from a header control. You can send this message explicitly or use the [**Header\_DeleteItem**](header-deleteitem.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

An index of the item to delete.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





