---
title: How to Add List-View Columns
description: This topic demonstrates how to add columns to a list-view control.
ms.assetid: 9DBDFF56-7CD6-467C-AD2E-64213615E241
ms.topic: article
ms.date: 05/31/2018
---

# How to Add List-View Columns

This topic demonstrates how to add columns to a list-view control. Columns are used to display the items and subitems when a list-view control is in report (details) view. Text from selected columns can also be displayed in tile view.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


To add a column to a list-view control, send the [**LVM\_INSERTCOLUMN**](lvm-insertcolumn.md) message or use the [**ListView\_InsertColumn**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertcolumn) macro. To delete a column, use the [**LVM\_DELETECOLUMN**](lvm-deletecolumn.md) message.

The following C++ code example calls the [**ListView\_InsertColumn**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertcolumn) macro to add columns to a list-view control. The column headings are defined in the application's header file as string resources, which are numbered consecutively starting with IDS\_FIRSTCOLUMN. The number of columns is defined in the header file as **C\_COLUMNS**.


```C++
// InitListViewColumns: Adds columns to a list-view control.
// hWndListView:        Handle to the list-view control. 
// Returns TRUE if successful, and FALSE otherwise. 
BOOL InitListViewColumns(HWND hWndListView) 
{ 
    WCHAR szText[256];     // Temporary buffer.
    LVCOLUMN lvc;
    int iCol;

    // Initialize the LVCOLUMN structure.
    // The mask specifies that the format, width, text,
    // and subitem members of the structure are valid.
    lvc.mask = LVCF_FMT | LVCF_WIDTH | LVCF_TEXT | LVCF_SUBITEM;

    // Add the columns.
    for (iCol = 0; iCol < C_COLUMNS; iCol++)
    {
        lvc.iSubItem = iCol;
        lvc.pszText = szText;
        lvc.cx = 100;               // Width of column in pixels.

        if ( iCol < 2 )
            lvc.fmt = LVCFMT_LEFT;  // Left-aligned column.
        else
            lvc.fmt = LVCFMT_RIGHT; // Right-aligned column.

        // Load the names of the column headings from the string resources.
        LoadString(g_hInst,
                   IDS_FIRSTCOLUMN + iCol,
                   szText,
                   sizeof(szText)/sizeof(szText[0]));

        // Insert the columns into the list view.
        if (ListView_InsertColumn(hWndListView, iCol, &lvc) == -1)
            return FALSE;
    }
    
    return TRUE;
} 
```



## Related topics

<dl> <dt>

[List-View Control Reference](bumper-list-view-list-view-control-reference.md)
</dt> <dt>

[About List-View Controls](list-view-controls-overview.md)
</dt> <dt>

[Using List-View Controls](using-list-view-controls.md)
</dt> </dl>

 

 




