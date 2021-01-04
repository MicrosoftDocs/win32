---
title: LVM_GETVIEW message (Commctrl.h)
description: Retrieves the current view of a list-view control.
ms.assetid: dd63e726-3a7f-40e7-8d46-4680816c02a3
keywords:
- LVM_GETVIEW message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETVIEW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETVIEW message

Retrieves the current view of a list-view control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **DWORD** that specifies the current view.

## Remarks

Following are the values for views.

-   LV\_VIEW\_DETAILS
-   LV\_VIEW\_ICON
-   LV\_VIEW\_LIST
-   LV\_VIEW\_SMALLICON
-   LV\_VIEW\_TILE

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





