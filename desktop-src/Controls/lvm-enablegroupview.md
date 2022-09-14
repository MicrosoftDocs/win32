---
title: LVM_ENABLEGROUPVIEW message (Commctrl.h)
description: Enables or disables whether the items in a list-view control display as a group.
ms.assetid: 783a5e23-d1cb-4523-a6d2-b2cf93fa7f62
keywords:
- LVM_ENABLEGROUPVIEW message Windows Controls
topic_type:
- apiref
api_name:
- LVM_ENABLEGROUPVIEW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_ENABLEGROUPVIEW message

Enables or disables whether the items in a list-view control display as a group.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>A **BOOL** that indicates whether to enable a list-view control to group displayed items. Use **TRUE** to enable grouping, **FALSE** to disable it. </dd> <dt>

*lParam* 
</dt> <dd>Must be **NULL**.</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                       | Description                                                                                  |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | The ability to display list-view items as a group is already enabled or disabled.<br/> |
| <dl> <dt>**1**</dt> </dl>  | The state of the control was successfully changed.<br/>                                |
| <dl> <dt>**-1**</dt> </dl> | The operation failed.<br/>                                                             |



 

## Remarks

**LVM\_ENABLEGROUPVIEW** is not supported under the [**LVS\_OWNERDATA**](list-view-window-styles.md) style.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





