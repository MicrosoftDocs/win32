---
title: LVM\_GETORIGIN message
description: Retrieves the current view origin for a list-view control. You can send this message explicitly or by using the ListView\_GetOrigin macro.
ms.assetid: 913c8339-fbe4-43c8-a997-5a972920dc3b
keywords:
- LVM_GETORIGIN message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETORIGIN
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

# LVM\_GETORIGIN message

Retrieves the current view origin for a list-view control. You can send this message explicitly or by using the [**ListView\_GetOrigin**](/windows/win32/Commctrl/nf-commctrl-listview_getorigin?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](https://msdn.microsoft.com/library/windows/desktop/dd162805) structure that receives the view origin.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** if the current view is list or report view.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





