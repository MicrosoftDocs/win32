---
title: LVM\_SETINSERTMARK message
description: Sets the insertion point to the defined position.
ms.assetid: 32cf5a11-918a-4dc4-bf10-88b3c26f26cc
keywords:
- LVM_SETINSERTMARK message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETINSERTMARK
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

# LVM\_SETINSERTMARK message

Sets the insertion point to the defined position.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to a [**LVINSERTMARK**](/windows/win32/Commctrl/ns-commctrl-lvinsertmark?branch=master) structure that specifies where to set the insertion point.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise. **FALSE** is returned if the size in the **cbSize** member of the [**LVINSERTMARK**](/windows/win32/Commctrl/ns-commctrl-lvinsertmark?branch=master) structure does not equal the actual size of the structure, or when an insertion point does not apply in the current view.

## Remarks

An insertion point can only appear if the list-view control is in icon view, small icon view, or tile view, and is not in group-view mode.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





