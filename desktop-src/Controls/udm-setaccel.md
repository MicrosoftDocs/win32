---
title: UDM\_SETACCEL message
description: Sets the acceleration for an up-down control.
ms.assetid: af1d0a34-13ba-4bda-82f5-d7afab6bb1ed
keywords:
- UDM_SETACCEL message Windows Controls
topic_type:
- apiref
api_name:
- UDM_SETACCEL
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

# UDM\_SETACCEL message

Sets the acceleration for an up-down control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Number of [**UDACCEL**](/windows/win32/Commctrl/ns-commctrl-_udaccel?branch=master) structures specified by *aAccels*.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an array of [**UDACCEL**](/windows/win32/Commctrl/ns-commctrl-_udaccel?branch=master) structures that contain acceleration information. Elements should be sorted in ascending order based on the **nSec** member.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**UDM\_GETACCEL**](udm-getaccel.md)
</dt> </dl>

 

 





