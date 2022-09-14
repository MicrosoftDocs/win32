---
title: How to Use Tree-View Infotips
description: When you apply the TVS\_INFOTIP style to a tree-view control, it generates TVN\_GETINFOTIP notifications when the cursor is over an item in the tree view. By responding to this notification, you can set the text that appears in the infotip.
ms.assetid: 779BEAC1-877E-43DD-AE1C-6D71C3013384
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Tree-View Infotips

When you apply the [**TVS\_INFOTIP**](tree-view-control-window-styles.md) style to a tree-view control, it generates [TVN\_GETINFOTIP](tvn-getinfotip.md) notifications when the cursor is over an item in the tree view. By responding to this notification, you can set the text that appears in the infotip.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use Tree-View Infotips

The following example code shows how an application might respond to the notification. For simplicity, the example just copies the text for the item to the infotip.


```
  case WM_NOTIFY:
    switch (((LPNMHDR) lParam)->code)
    {
    case TVN_GETINFOTIP:
        {
          LPNMTVGETINFOTIP pTip = (LPNMTVGETINFOTIP)lParam;
          HWND hTree            = GetDlgItem(hDlg, IDC_TREE1);
          HTREEITEM item        = pTip->hItem;

          // Get the text for the item.
          TVITEM tvitem;
          tvitem.mask       = TVIF_TEXT;
          tvitem.hItem      = item;
          TCHAR temp[1024];
          tvitem.pszText    = infoTipBuf;
          tvitem.cchTextMax = sizeof(temp) / sizeof(TCHAR);
          TreeView_GetItem(hTree, &tvitem);

          // Copy the text to the infotip.
          wcscpy_s(pTip->pszText, pTip->cchTextMax, tvitem.pszText);
          break;
        }
      }
      return TRUE;
```



## Related topics

<dl> <dt>

[Using Tree-View Controls](using-treeview.md)
</dt> <dt>

[CustDTv sample illustrates custom draw in a Tree-View control](https://support.microsoft.com/default.aspx?scid=kb;EN-US;q248496)
</dt> </dl>

 

 




