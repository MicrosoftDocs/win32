---
title: TCM\_SETIMAGELIST message
description: Assigns an image list to a tab control. You can send this message explicitly or by using the TabCtrl\_SetImageList macro.
ms.assetid: 'b457c73c-4c38-4bc5-af5d-12bbd24504a6'
keywords: ["TCM_SETIMAGELIST message Windows Controls"]
topic_type:
- apiref
api_name:
- TCM_SETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TCM\_SETIMAGELIST message

Assigns an image list to a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetImageList**](tabctrl-setimagelist.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the image list to assign to the tab control.

</dd> </dl>

## Return value

Returns the handle to the previous image list, or **NULL** if there is no previous image list.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





