---
title: TBM_SETBUDDY message (Commctrl.h)
description: Assigns a window as the buddy window for a trackbar control. Trackbar buddy windows are automatically displayed in a location relative to the control's orientation (horizontal or vertical).
ms.assetid: ab35911f-bf81-47f3-98aa-0901aa877dea
keywords:
- TBM_SETBUDDY message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETBUDDY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETBUDDY message

Assigns a window as the buddy window for a trackbar control. Trackbar buddy windows are automatically displayed in a location relative to the control's orientation (horizontal or vertical).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value specifying the location at which to display the buddy window. This value can be one of the following:



| Value                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | The buddy will appear to the left of the trackbar if the trackbar control uses the [**TBS\_HORZ**](trackbar-control-styles.md) style. If the trackbar uses the [**TBS\_VERT**](trackbar-control-styles.md) style, the buddy appears above the trackbar control.<br/>  |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | The buddy will appear to the right of the trackbar if the trackbar control uses the [**TBS\_HORZ**](trackbar-control-styles.md) style. If the trackbar uses the [**TBS\_VERT**](trackbar-control-styles.md) style, the buddy appears below the trackbar control.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the window that will be set as the trackbar control's buddy.

</dd> </dl>

## Return value

Returns the handle to the window that was previously assigned to the control at that location.

## Remarks

> [!Note]  
> Trackbar controls support up to two buddy windows. This can be useful when you must display text or images at each end of the control.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





