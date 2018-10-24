---
title: UDM_SETRANGE message
description: Sets the minimum and maximum positions (range) for an up-down control.
ms.assetid: 81875528-86cc-419a-a07c-f4f98baf1462
keywords:
- UDM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- UDM_SETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UDM\_SETRANGE message

Sets the minimum and maximum positions (range) for an up-down control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) is a **short** that specifies the maximum position for the up-down control, and the [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) is a **short** that specifies the minimum position. Neither position can be greater than the UD\_MAXVAL value or less than the UD\_MINVAL value. In addition, the difference between the two positions cannot exceed UD\_MAXVAL.

</dd> </dl>

## Return value

No return value.

## Remarks

The maximum position can be less than the minimum position. Clicking the up arrow button moves the current position closer to the maximum position, and clicking the down arrow button moves toward the minimum position.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**MAKELPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632661)
</dt> <dt>

[**UDM\_SETRANGE**](udm-setrange.md)
</dt> </dl>

 

 





