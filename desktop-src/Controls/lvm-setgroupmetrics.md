---
title: LVM\_SETGROUPMETRICS message
description: Sets information about the display of groups.
ms.assetid: 268b478d-da1f-4efe-9ee9-af3f12e089ee
keywords:
- LVM_SETGROUPMETRICS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETGROUPMETRICS
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

# LVM\_SETGROUPMETRICS message

Sets information about the display of groups.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be **NULL**.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an [**LVGROUPMETRICS**](/windows/win32/Commctrl/ns-commctrl-taglvgroupmetrics?branch=master) structure that contains the metrics to set.</dd> </dl>

## Return value

The return value is not used.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





