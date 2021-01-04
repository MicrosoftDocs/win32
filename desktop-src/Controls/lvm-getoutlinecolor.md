---
title: LVM_GETOUTLINECOLOR message (Commctrl.h)
description: Retrieves the color of the border of a list-view control if the LVS\_EX\_BORDERSELECT extended window style is set.
ms.assetid: cc9d69d1-1470-4eaa-8d54-e31b796cf685
keywords:
- LVM_GETOUTLINECOLOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETOUTLINECOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETOUTLINECOLOR message

Retrieves the color of the border of a list-view control if the [**LVS\_EX\_BORDERSELECT**](extended-list-view-styles.md) extended window style is set.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **COLORREF** structure that contains the color of the border of a list-view control.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





