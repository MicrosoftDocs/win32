---
title: TVM_MAPACCIDTOHTREEITEM message (Commctrl.h)
description: Maps an accessibility ID to an HTREEITEM.
ms.assetid: f4feb7cb-2138-4930-b8ee-b9e2d4b19001
keywords:
- TVM_MAPACCIDTOHTREEITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_MAPACCIDTOHTREEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_MAPACCIDTOHTREEITEM message

Maps an accessibility ID to an **HTREEITEM**.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>**UINT** that contains the accessibility ID to map to an **HTREEITEM**. </dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the **HTREEITEM** that the specified accessibility ID is mapped to.

## Remarks

When you add an item to a tree-view control an **HTREEITEM** returns, which uniquely identifies the item.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TreeView\_MapAccIDToHTREEITEM**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_mapaccidtohtreeitem)
</dt> </dl>

 

 





