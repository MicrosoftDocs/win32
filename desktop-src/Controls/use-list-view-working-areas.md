---
title: How to Use List-View Working Areas
description: This topic demonstrates how to work with list-view working areas. Working areas are rectangular virtual areas that can be used to arrange items in a list-view control.
ms.assetid: 7A803B66-7827-49A3-8D87-6A037C09A19A
ms.topic: article
ms.date: 05/31/2018
---

# How to Use List-View Working Areas

This topic demonstrates how to work with list-view working areas. Working areas are rectangular virtual areas that can be used to arrange items in a list-view control. A working area is not a window and cannot have a visible border. By default, the list-view control has no working areas. By creating a working area, you can create an empty border on the left, top, or right of the items or cause a horizontal scroll bar to be displayed when there normally would not be one.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Working Area

The following C++ code example demonstrates how to create a working area with a 25-pixel empty border on its top, left, and right sides.


```C++
void SetWorkAreas1(HWND hWndListView)
{
    #define  EMPTY_SPACE   25
    
    RECT  rcClient;
    
    GetClientRect(hWndListView, &rcClient);
    
    rcClient.left  +=  EMPTY_SPACE;
    rcClient.top   +=  EMPTY_SPACE;
    rcClient.right -= (EMPTY_SPACE * 2);
    
    SendMessage(hWndListView, LVM_SETWORKAREAS, 1, (LPARAM)&rcClient);

    return;
}
```



### Create Multiple Working Areas

The following C++ code example demonstrates how to create two working areas in a control. Each working area uses about half of the client area, and is surrounded by a 25-pixel empty border.


```C++
void SetWorkAreas2(HWND hWndListView)
{
    #define  EMPTY_SPACE   25
    
    RECT  rcClient;
    RECT  rcWork[2];
    
    GetClientRect(hWndListView, &rcClient);
    
    rcWork[0].left   = rcClient.left +      EMPTY_SPACE;
    rcWork[0].top    = rcClient.top +       EMPTY_SPACE;
    rcWork[0].right  = (rcClient.right/2) - EMPTY_SPACE;
    rcWork[0].bottom = rcClient.bottom;
    
    rcWork[1].left   = (rcClient.right/2) + EMPTY_SPACE;
    rcWork[1].top    = rcClient.top +       EMPTY_SPACE;
    rcWork[1].right  = rcClient.right -     EMPTY_SPACE;
    rcWork[1].bottom = rcClient.bottom;
    
    SendMessage(hWndListView, LVM_SETWORKAREAS, 2, (LPARAM)rcWork);

    return;
}
```



### Determine the Working Area to Which an Item Belongs

One way to determine which working area an item belongs is to do the following:

-   Retrieve the list of coordinates of all of the working areas in the list-view control.
-   Retrieve the coordinates of the item.
-   Determine whether the item coordinates lie within the coordinates of one of the working areas.

The application-defined function in the following C++ code example returns the index of the working area to which the item belongs. If the function fails, it returns –1. If the function succeeds, but the item is not inside any of the working areas, the function returns 0, because all items that are not inside a working area automatically become a member of working area zero.


```C++
int GetItemWorkingArea(HWND hWndListView, int iItem)
{
    UINT     uWorkAreas = 0;
    int      nReturn = -1;
    LPRECT   pRects;
    POINT    pt;
    
    if(!ListView_GetItemPosition(hWndListView, iItem, &pt))
        return nReturn;
    
    ListView_GetNumberOfWorkAreas(hWndListView, &uWorkAreas);
    
    if(uWorkAreas)
    {
        pRects = (LPRECT)GlobalAlloc(GPTR, sizeof(RECT) * uWorkAreas);
        
        if(pRects)
        {
            UINT  i;
            nReturn = 0;
    
            ListView_GetWorkAreas(hWndListView, uWorkAreas, pRects);
          
            for(i = 0; i < uWorkAreas; i++)
            {
                if(PtInRect((pRects + i), pt))
                {
                    nReturn = i;
                    break;
                }
            }
            GlobalFree((HGLOBAL)pRects);
        }
    }
    return nReturn;
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

 

 




