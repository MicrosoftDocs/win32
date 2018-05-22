---
title: LVM\_SETITEMINDEXSTATE message
description: Sets the state of a list-view item. Send this message explicitly or by using the ListView\_SetItemIndexState macro.
ms.assetid: '9fea6420-320a-4d2a-84b5-7923fbb14655'
keywords: ["LVM_SETITEMINDEXSTATE message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_SETITEMINDEXSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_SETITEMINDEXSTATE message

Sets the state of a list-view item. Send this message explicitly or by using the [**ListView\_SetItemIndexState**](listview-setitemindexstate.md) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A pointer to an [**LVITEMINDEX**](lvitemindex.md) structure for the item. The calling process is responsible for allocating this structure and setting the members.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to an [**LVITEM**](lvitem.md) structure. The calling process is responsible for allocating memory for the structure. Set the **state** member to one or more (as a bitwise combination) of the [List-View Item States](list-view-item-states.md) flags. Set the **stateMask** member of the structure to indicate the valid bits of the **state** member. For more information, see the **stateMask** member of the **LVITEM** structure.

</dd> </dl>

## Return value

Returns one of the following values of type **HRESULT**.



| Return code                                                                                  | Description                                                       |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The state could not be set.<br/>                            |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | The list-view control was not ready for the operation.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>         | The operation was successful.<br/>                          |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





