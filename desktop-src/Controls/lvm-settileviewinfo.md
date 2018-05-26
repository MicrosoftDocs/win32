---
title: LVM\_SETTILEVIEWINFO message
description: Sets information that a list-view control uses in tile view.
ms.assetid: 1c4f2aff-1ce1-484a-9360-3efbe870b39b
keywords:
- LVM_SETTILEVIEWINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETTILEVIEWINFO
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

# LVM\_SETTILEVIEWINFO message

Sets information that a list-view control uses in tile view.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an [**LVTILEVIEWINFO**](/windows/win32/Commctrl/ns-commctrl-taglvtileviewinfo?branch=master) structure that contains the information to set.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





