---
title: LVM_GETINSERTMARK message (Commctrl.h)
description: Retrieves the position of the insertion point.
ms.assetid: ad00df4c-4b4b-48f1-8821-7849a216df2e
keywords:
- LVM_GETINSERTMARK message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETINSERTMARK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETINSERTMARK message

Retrieves the position of the insertion point.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to a <a href="/windows/desktop/api/Commctrl/ns-commctrl-lvinsertmark">LVINSERTMARK</a> structure that receives the position of the insertion point.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise. **FALSE** is returned if the size in the **cbSize** member of the [**LVINSERTMARK**](/windows/desktop/api/Commctrl/ns-commctrl-lvinsertmark) structure does not equal the actual size of the structure.

## Remarks

An insertion point can appear only if the list-view control is in icon view, small icon view, or tile view, and is not in group-view mode.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





