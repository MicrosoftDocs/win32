---
title: HDM\_GETITEMCOUNT message
description: Gets a count of the items in a header control. You can send this message explicitly or use the Header\_GetItemCount macro.
ms.assetid: '0e6d2131-53b4-4927-bd0f-577b8eaf237a'
keywords: ["HDM_GETITEMCOUNT message Windows Controls"]
topic_type:
- apiref
api_name:
- HDM_GETITEMCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# HDM\_GETITEMCOUNT message

Gets a count of the items in a header control. You can send this message explicitly or use the [**Header\_GetItemCount**](header-getitemcount.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of items if successful, or -1 otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





