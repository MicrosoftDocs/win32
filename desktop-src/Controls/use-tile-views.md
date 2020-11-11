---
title: How to Use Tile Views
description: This topic demonstrates how to set the tile view for a list-view control.
ms.assetid: BDE17F4B-3A15-48BB-8160-036AD0DC3B41
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Tile Views

This topic demonstrates how to set the tile view for a list-view control. In tile view, each item is represented by a large icon with one or more lines of accompanying text. For an illustration, see [About List-View Controls](list-view-controls-overview.md).

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


Set the general display parameters for tile view by using the [**ListView\_SetTileViewInfo**](/windows/desktop/api/Commctrl/nf-commctrl-listview_settileviewinfo) macro. Use the [**LVTILEVIEWINFO**](/windows/win32/api/commctrl/ns-commctrl-lvtileviewinfo) structure that is passed to this macro to specify the position of the text in relation to the icon, the size of each tile (including accompanying text), and the maximum number of lines of text.

If you do not want tiles to be automatically sized, you must set **LVTVIF\_FIXEDSIZE** in the **dwFlags** member and **LVTVIM\_TILESIZE** in the **dwMask** member of [**LVTILEVIEWINFO**](/windows/win32/api/commctrl/ns-commctrl-lvtileviewinfo), as well as providing the dimensions in the **sizeTile** member.

The following C++ code example sets the tile view info for a list-view control so that a maximum of two subitems are displayed for each item. It also sets the size of each tile.


```C++
    SIZE size = { 100, 50 };
    LVTILEVIEWINFO tileViewInfo = {0};

    tileViewInfo.cbSize   = sizeof(tileViewInfo);
    tileViewInfo.dwFlags  = LVTVIF_FIXEDSIZE;
    tileViewInfo.dwMask   = LVTVIM_COLUMNS | LVTVIM_TILESIZE;
    tileViewInfo.cLines   = 2;
    tileViewInfo.sizeTile = size;

    ListView_SetTileViewInfo(hWndListView, &tileViewInfo);

```



For each item in the list, you can set further parameters when the item is inserted in the list, or later. The [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure that is used with [**ListView\_InsertItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertitem) contains members that specify which columns of data to display below the item, and their alignment. These same display parameters are also found in the [**LVTILEINFO**](/windows/win32/api/commctrl/ns-commctrl-lvtileinfo) structure used with [**ListView\_SetTileInfo**](/windows/desktop/api/Commctrl/nf-commctrl-listview_settileinfo).

> [!Note]  
> "Columns" here refers not to display columns in tile view but rather to subitems, which are displayed in columns in details view.

 

## Related topics

<dl> <dt>

[List-View Control Reference](bumper-list-view-list-view-control-reference.md)
</dt> <dt>

[About List-View Controls](list-view-controls-overview.md)
</dt> <dt>

[Using List-View Controls](using-list-view-controls.md)
</dt> </dl>

 

 




