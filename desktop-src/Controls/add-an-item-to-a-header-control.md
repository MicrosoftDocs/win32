---
title: How to Add an Item to a Header Control
description: This topic demonstrates how to add an item to a header control.
ms.assetid: DF71EF92-1726-46E1-A10F-57D3B07FB936
ms.topic: article
ms.date: 05/31/2018
---

# How to Add an Item to a Header Control

This topic demonstrates how to add an item to a header control. A header control typically has several header items that define the columns of the control. You can add an item to a header control by sending the [**HDM\_INSERTITEM**](hdm-insertitem.md) message to the control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


Use the [**HDM\_INSERTITEM**](hdm-insertitem.md) message to add an item to the header control. The message must include the address of an [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure. This structure defines the properties of the header item, which can include a string, a bitmapped image, an initial size, and an application-defined 32-bit value.

The following example illustrates how to use the [**HDM\_INSERTITEM**](hdm-insertitem.md) message and the [**HDITEM**](/windows/win32/api/commctrl/ns-commctrl-hditema) structure to add an item to a header control. The new item consists of a string that is left-justified within the item rectangle.



```C++
// DoInsertItem - inserts an item into a header control. 
// Returns the index of the new item. 
// hwndHeader - handle to the header control. 
// iInsertAfter - index of the previous item. 
// nWidth - width of the new item. 
// lpsz - address of the item string. 
int DoInsertItem(HWND hwndHeader, int iInsertAfter, 
    int nWidth, LPTSTR lpsz) 
{ 
    HDITEM hdi; 
    int index; 
 
    hdi.mask = HDI_TEXT | HDI_FORMAT | HDI_WIDTH; 
    hdi.cxy = nWidth; 
    hdi.pszText = lpsz; 
    hdi.cchTextMax = sizeof(hdi.pszText)/sizeof(hdi.pszText[0]); 
    hdi.fmt = HDF_LEFT | HDF_STRING; 
 
    index = SendMessage(hwndHeader, HDM_INSERTITEM, 
        (WPARAM) iInsertAfter, (LPARAM) &hdi); 
 
    return index; 
}
```



## Related topics

<dl> <dt>

[About Header Controls](header-controls.md)
</dt> <dt>

[Header Control Reference](bumper-header-control-header-control-reference.md)
</dt> <dt>

[Using Header Controls](using-header-controls.md)
</dt> </dl>

 

 




