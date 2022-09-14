---
title: TDM_ENABLE_RADIO_BUTTON message (Commctrl.h)
description: Enables or disables a radio button in a task dialog.
ms.assetid: da605ce0-b2d5-481a-a0e1-628ae5b65726
keywords:
- TDM_ENABLE_RADIO_BUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TDM_ENABLE_RADIO_BUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_ENABLE\_RADIO\_BUTTON message

Enables or disables a radio button in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

An **int** value that specifies the ID of the radio button to be enabled or disabled.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Specifies button state. Set to 0 to disable the button; set to nonzero to enable the button.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





