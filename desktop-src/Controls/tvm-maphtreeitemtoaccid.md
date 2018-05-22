---
title: TVM\_MAPHTREEITEMTOACCID message
description: Maps an HTREEITEM to an accessibility ID.
ms.assetid: '87ef0785-88c1-49f4-8a05-872577e16fe4'
keywords: ["TVM_MAPHTREEITEMTOACCID message Windows Controls"]
topic_type:
- apiref
api_name:
- TVM_MAPHTREEITEMTOACCID
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TVM\_MAPHTREEITEMTOACCID message

Maps an **HTREEITEM** to an accessibility ID.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>**HTREEITEM** that is mapped to an accessibility ID.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an accessibility ID.

## Remarks

When you add an item to a tree-view control an **HTREEITEM** handle is returned that uniquely identifies the item.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TreeView\_MapHTREEITEMtoAccID**](treeview-maphtreeitemtoaccid.md)
</dt> </dl>

 

 





