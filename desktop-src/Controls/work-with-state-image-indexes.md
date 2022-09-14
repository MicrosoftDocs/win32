---
title: How to Work With State Image Indexes
description: There is often confusion about how to set and retrieve the state image index in a tree-view control.
ms.assetid: 2666D922-9957-4A75-BFDA-038720F1EEDC
ms.topic: article
ms.date: 05/31/2018
---

# How to Work With State Image Indexes

There is often confusion about how to set and retrieve the state image index in a tree-view control. The following examples demonstrate the proper method for setting and retrieving the state image index. The examples assume that there are only two state image indexes in the tree-view control, unchecked and checked. If your application contains more than two, these functions will need to be modified to handle that case.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Set a Tree-View Item's Check State

The following example demonstrates how to set a tree-view item's check state.


```C++
  BOOL TreeView_SetCheckState(HWND hwndTreeView, HTREEITEM hItem, BOOL fCheck)
  {
      TVITEM tvItem;

      tvItem.mask   = TVIF_HANDLE | TVIF_STATE;
      tvItem.hItem  = hItem;
      tvItem.stateMask  = TVIS_STATEIMAGEMASK;

      // Image 1 in the tree-view check box image list is the unchecked box. 
      // Image 2 is the checked box.

      tvItem.state = INDEXTOSTATEIMAGEMASK((fCheck ? 2 : 1));

      return TreeView_SetItem(hwndTreeView, &tvItem);
  }
```



### Retrieve a Tree-View Item's Check State

The following example demonstrates how to retrieve a tree-view item's check state.


```C++
  BOOL TreeView_GetCheckState(HWND hwndTreeView, HTREEITEM hItem)
  {
      TVITEM tvItem;

      // Prepare to receive the desired information.
      tvItem.mask   = TVIF_HANDLE | TVIF_STATE;
      tvItem.hItem  = hItem;
      tvItem.stateMask  = TVIS_STATEIMAGEMASK;

      // Request the information.
      TreeView_GetItem(hwndTreeView, &tvItem);

      // Return zero if it's not checked, or nonzero otherwise.
      return ((BOOL)(tvItem.state >> 12) - 1);
  }
```



## Related topics

<dl> <dt>

[Using Tree-View Controls](using-treeview.md)
</dt> <dt>

[CustDTv sample illustrates custom draw in a Tree-View control](https://support.microsoft.com/default.aspx?scid=kb;EN-US;q248496)
</dt> </dl>

 

 




