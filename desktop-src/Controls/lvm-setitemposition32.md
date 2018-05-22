---
title: LVM\_SETITEMPOSITION32 message
description: Moves an item to a specified position in a list-view control (must be in icon or small icon view).
ms.assetid: '77db5fd0-bbc3-47ad-95ef-61ef4ac022bc'
keywords: ["LVM_SETITEMPOSITION32 message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_SETITEMPOSITION32
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_SETITEMPOSITION32 message

Moves an item to a specified position in a list-view control (must be in icon or small icon view). This message differs from the [**LVM\_SETITEMPOSITION**](lvm-setitemposition.md) message in that it uses 32-bit coordinates. You can send this message explicitly or by using the [**ListView\_SetItemPosition32**](listview-setitemposition32.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item for which to set the position.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](https://msdn.microsoft.com/library/windows/desktop/dd162805) structure that contains the new position of the item, in list-view coordinates.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





