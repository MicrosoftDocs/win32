---
title: LVM_GETTILEVIEWINFO message (Commctrl.h)
description: Retrieves information about a list-view control in tile view.
ms.assetid: 114990c0-a150-49d8-80e7-b084c648ac34
keywords:
- LVM_GETTILEVIEWINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETTILEVIEWINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETTILEVIEWINFO message

Retrieves information about a list-view control in tile view.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an <a href="/windows/win32/api/commctrl/ns-commctrl-lvtileviewinfo">**LVTILEVIEWINFO**</a> structure that receives the retrieved information.</dd> </dl>

## Return value

Return value not used.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





