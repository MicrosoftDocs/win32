---
title: TDM_SET_PROGRESS_BAR_RANGE message
description: Sets the minimum and maximum values for the progress bar in a task dialog.
ms.assetid: ca8b48bc-cf56-4678-bb3d-7c730a96d98c
keywords:
- TDM_SET_PROGRESS_BAR_RANGE message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_PROGRESS_BAR_RANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# TDM\_SET\_PROGRESS\_BAR\_RANGE message

Sets the minimum and maximum values for the progress bar in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the minimum value. By default, the minimum value is zero. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the maximum value. By default, the maximum value is 100.

</dd> </dl>

## Return value

Returns the previous minimum and maximum values, if successful, or zero otherwise. The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the minimum value, and the [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) contains the maximum value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





