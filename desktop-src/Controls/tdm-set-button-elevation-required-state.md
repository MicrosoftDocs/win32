---
title: TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE message (Commctrl.h)
description: Specifies whether a given task dialog button or command link should have a User Account Control (UAC) shield icon; that is, whether the action invoked by the button requires elevation.
ms.assetid: c4321fdb-3ea9-49bf-b53d-eb73d5b11084
keywords:
- TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_SET\_BUTTON\_ELEVATION\_REQUIRED\_STATE message

Specifies whether a given task dialog button or command link should have a User Account Control (UAC) shield icon; that is, whether the action invoked by the button requires elevation.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The ID of the push button or command link to be updated.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Set to 0 to designate that the action invoked by the button does not require elevation. Set to nonzero to designate that the action requires elevation.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





