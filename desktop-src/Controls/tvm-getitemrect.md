---
title: TVM\_GETITEMRECT message
description: Retrieves the bounding rectangle for a tree-view item and indicates whether the item is visible. You can send this message explicitly or by using the TreeView\_GetItemRect macro.
ms.assetid: 'f2d7d7b1-cfe7-4361-bd90-e3e99dbcd99c'
keywords: ["TVM_GETITEMRECT message Windows Controls"]
topic_type:
- apiref
api_name:
- TVM_GETITEMRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TVM\_GETITEMRECT message

Retrieves the bounding rectangle for a tree-view item and indicates whether the item is visible. You can send this message explicitly or by using the [**TreeView\_GetItemRect**](treeview-getitemrect.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value specifying the portion of the item for which to retrieve the bounding rectangle. If this parameter is **TRUE**, the bounding rectangle includes only the text of the item. Otherwise, it includes the entire line that the item occupies in the tree-view control.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that, when sending the message, contains the handle of the item to retrieve the rectangle for. See the example below for more information on how to place the item handle in this parameter. After returning from the message, this parameter contains the bounding rectangle. The coordinates are relative to the upper-left corner of the tree-view control.

</dd> </dl>

## Return value

If the item is visible and the bounding rectangle was successfully retrieved, the return value is **TRUE**. Otherwise, the message returns **FALSE** and does not retrieve the bounding rectangle.

## Remarks

When sending this message, the *lParam* parameter contains the handle of the item that the rectangle is being retrieved for. The handle is placed in *lParam* as shown in the following example:


```
RECT rc;

*(HTREEITEM*)&amp;rc = hTreeItem;

SendMessage(hwndTreeView, TVM_GETITEMRECT, FALSE, (LPARAM)&amp;rc);
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





