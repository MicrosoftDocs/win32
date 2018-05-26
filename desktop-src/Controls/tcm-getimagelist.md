---
title: TCM\_GETIMAGELIST message
description: Retrieves the image list associated with a tab control. You can send this message explicitly or by using the TabCtrl\_GetImageList macro.
ms.assetid: 86a0d8c7-ff3d-4e16-994e-4c72d1e62e9f
keywords:
- TCM_GETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETIMAGELIST
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

# TCM\_GETIMAGELIST message

Retrieves the image list associated with a tab control. You can send this message explicitly or by using the [**TabCtrl\_GetImageList**](/windows/win32/Commctrl/nf-commctrl-tabctrl_getimagelist?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the image list if successful, or **NULL** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





