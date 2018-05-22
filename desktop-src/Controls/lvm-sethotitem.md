---
title: LVM\_SETHOTITEM message
description: Sets the hot item for a list-view control. You can send this message explicitly or use the ListView\_SetHotItem macro.
ms.assetid: '0aa2b15d-4983-4234-9863-f1fdee09f913'
keywords: ["LVM_SETHOTITEM message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_SETHOTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_SETHOTITEM message

Sets the hot item for a list-view control. You can send this message explicitly or use the [**ListView\_SetHotItem**](listview-sethotitem.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the item to be set as the hot item.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the item that was previously hot.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





