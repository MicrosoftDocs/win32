---
title: How to Use Groups in a List-View
description: This topic describes how to create an instance of a group and add it to a list-view control.
ms.assetid: 8486B9A2-C519-4912-9E88-3BAFCC4D51CF
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Groups in a List-View

This topic describes how to create an instance of a group and add it to a list-view control. Grouping allows a user to arrange lists into groups of items that are visually divided on the page, using a horizontal divider and a group title.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


To use groups in a list-view control, ensure that the control includes the [**LVS\_ALIGNTOP**](list-view-window-styles.md) window style.

When you add an item to the list, you assign it to a group by setting the **iGroupId** member of the item's [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure to the value of the **iGroupId** member of the groups's [**LVGROUP**](/windows/win32/api/commctrl/ns-commctrl-lvgroup) structure. An item that is not assigned to a group does not appear in the list when group view is enabled. To enable or disable group view, use the [**ListView\_EnableGroupView**](/windows/desktop/api/Commctrl/nf-commctrl-listview_enablegroupview) macro.

The following example shows how to create a group with a header and add it to a list-view control.


```C++
    LVGROUP group;

    group.cbSize    = sizeof(LVGROUP);
    group.mask      = LVGF_HEADER | LVGF_GROUPID;
    group.pszHeader = TEXT("Dogs");
    group.iGroupId  = 1;

    ListView_InsertGroup(hWndListView, -1, &group);

```



## Related topics

<dl> <dt>

[List-View Control Reference](bumper-list-view-list-view-control-reference.md)
</dt> <dt>

[About List-View Controls](list-view-controls-overview.md)
</dt> <dt>

[Using List-View Controls](using-list-view-controls.md)
</dt> </dl>

 

 




