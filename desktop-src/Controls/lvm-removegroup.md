---
title: LVM_REMOVEGROUP message (Commctrl.h)
description: Removes a group from a list-view control.
ms.assetid: c6f4f54c-4cf8-47d0-8e96-fa8a1df0501b
keywords:
- LVM_REMOVEGROUP message Windows Controls
topic_type:
- apiref
api_name:
- LVM_REMOVEGROUP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_REMOVEGROUP message

Removes a group from a list-view control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>ID that specifies the group to remove.</dd> <dt>

*lParam* 
</dt> <dd>

Must be **NULL**.

</dd> </dl>

## Return value

Returns the index of the group if successful, or -1 otherwise.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





