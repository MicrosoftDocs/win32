---
title: UDM_GETRANGE message (Commctrl.h)
description: Retrieves the minimum and maximum positions (range) for an up-down control.
ms.assetid: fd42538a-8d96-4a9c-a1db-07c3e9afef84
keywords:
- UDM_GETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- UDM_GETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UDM\_GETRANGE message

Retrieves the minimum and maximum positions (range) for an up-down control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is a 32-bit value that contains the minimum and maximum positions. The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is the maximum position for the control, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is the minimum position.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

