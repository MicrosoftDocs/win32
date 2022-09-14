---
title: LVM_SETVIEW message (Commctrl.h)
description: Sets the view of a list-view control.
ms.assetid: e6d3f16d-52ea-4863-a6c9-9a085d5f794a
keywords:
- LVM_SETVIEW message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETVIEW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETVIEW message

Sets the view of a list-view control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>**DWORD** that specifies the view.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns 1 if successful, or -1 otherwise. For example, -1 is returned if the view is invalid.

## Remarks

Following are the values for views.

-   LV\_VIEW\_DETAILS
-   LV\_VIEW\_ICON
-   LV\_VIEW\_LIST
-   LV\_VIEW\_SMALLICON
-   LV\_VIEW\_TILE

> [!Note]  
> To use this message, you must provide a manifest specifying Comctl32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





