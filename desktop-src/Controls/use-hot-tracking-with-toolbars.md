---
title: How to Use Hot-Tracking with Toolbars
description: When a mouse pointer hovers over an item, the item becomes hot. If hot-tracking is enabled, the hot item is highlighted. A toolbar that is created with the TBSTYLE\_FLAT style, or one that uses Visual Styles, supports hot-tracking by default.
ms.assetid: E77B15D7-F0C9-41F7-8BE9-30260FA4BB0C
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Hot-Tracking with Toolbars

When a mouse pointer hovers over an item, the item becomes hot. If hot-tracking is enabled, the hot item is highlighted. A toolbar that is created with the [**TBSTYLE\_FLAT**](toolbar-control-and-button-styles.md) style, or one that uses [Visual Styles](themes-overview.md), supports hot-tracking by default.

Hot-tracking requires that you create image lists; therefore, you cannot use the [**TB\_ADDBITMAP**](tb-addbitmap.md) message or the [**CreateToolbarEx**](/windows/desktop/api/Commctrl/nf-commctrl-createtoolbarex) function to create your toolbar.

When the mouse hovers over a toolbar button, the button is outlined to highlight it. The following illustration shows a toolbar with hot-tracking enabled; the mouse pointer was hovering on the Save button when the screen shot was taken.

![screen shot of a dialog box with a three-item toolbar; the selected icon is outlined](images/tb-withstyles.png)

If you want a toolbar button bitmap to change when the state of the control changes, store the different images in [image lists](image-lists.md). For example, some applications have black and white toolbar buttons that become colored when they are selected. The two different images are stored in image lists. Toolbars support using up to three image lists. Typically an application has a default, disabled, and hot-tracking list of images. To set and retrieve image lists for hot toolbar buttons, use the [**TB\_SETHOTIMAGELIST**](tb-sethotimagelist.md) and [**TB\_GETHOTIMAGELIST**](tb-gethotimagelist.md) messages.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use Hot-Tracking with a Toolbar

The following code example creates, fills, and assigns an image list for hot buttons.


```C++
// Create the image list, himlHot.
g_himlHot = ImageList_Create(MYICON_CX,MYICON_CY,ILC_COLOR8,0,4);

// Load a bitmap from a resource file, and add the images to the image list.
// Note that the bitmap contains four images.

hBitmapHot = LoadBitmap(g_hinst, MAKEINTRESOURCE(IDB_HOT));

ImageList_Add(g_himlHot, hBitmapHot, NULL);
   
// Set the image list. 
SendMessage(hwndTB, TB_SETHOTIMAGELIST, 0, (LPARAM)g_himlHot);
   
// Loop to fill the array of TBBUTTON structures.  
for(i=0;i<MAX_BUTTONS;i++)
{
    tbArray[i].iBitmap   = i;                   // Bitmap from image list.
    tbArray[i].idCommand = IDM_BUTTONSTART + i;
    tbArray[i].fsState   = TBSTATE_ENABLED;
    tbArray[i].fsStyle   = BTNS_DROPDOWN;
    tbArray[i].dwData    = 0;
    tbArray[i].iString   = i;
}

DeleteObject(hBitmapHot);    // Delete the loaded bitmap.
```



## Related topics

<dl> <dt>

[Using Toolbar Controls](using-toolbar-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




