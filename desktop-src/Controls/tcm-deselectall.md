---
title: TCM\_DESELECTALL message
description: Resets items in a tab control, clearing any that were set to the TCIS\_BUTTONPRESSED state. You can send this message explicitly or by using the TabCtrl\_DeselectAll macro.
ms.assetid: cc2e5131-3c1b-473a-a0ca-274a2d39a2f1
keywords:
- TCM_DESELECTALL message Windows Controls
topic_type:
- apiref
api_name:
- TCM_DESELECTALL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TCM\_DESELECTALL message

Resets items in a tab control, clearing any that were set to the [**TCIS\_BUTTONPRESSED**](tab-control-item-states.md#tcis-buttonpressed) state. You can send this message explicitly or by using the [**TabCtrl\_DeselectAll**](/windows/win32/Commctrl/nf-commctrl-tabctrl_deselectall?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag that specifies the scope of the item deselection. If this parameter is set to **FALSE**, all tab items will be reset. If it is set to **TRUE**, then all tab items except for the one currently selected will be reset.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

This message is only meaningful if the [**TCS\_BUTTONS**](tab-control-styles.md#tcs-buttons) style flag has been set.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





