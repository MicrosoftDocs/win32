---
title: How to Create an Image List
description: This topic demonstrates how to use the ImageList\_Create function to create an image list.
ms.assetid: 6092C555-B5B6-49DB-B07B-684EDB890761
ms.topic: article
ms.date: 05/31/2018
---

# How to Create an Image List

This topic demonstrates how to use the [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) function to create an image list.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


You create an image list by calling the [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) function. The parameters include the type of image list to create, the dimensions of each image, and the number of images that you intend to add to the list.

The following example creates a masked image list and uses the [**ImageList\_AddIcon**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_addicon) macro to add two icons to the list.



```C++
// AddIconsToImageList - creates a masked image list and adds some 
// icons to it. 
// Returns the handle to the new image list. 
// hinst - handle to the application instance. 
// 
// Global variables and constants 
//     g_nBird and g_nTree - indexes of the images. 
//     cx_icon and cy_icon - width and height of the icon. 
//     num_icons - number of icons to add to the image list. 
extern int g_nBird, g_nTree; 
 
#define CX_ICON  32 
#define CY_ICON  32 
#define NUM_ICONS 3 
 
HIMAGELIST AddIconsToImageList(HINSTANCE hinst) 
{ 
    HIMAGELIST himlIcons;  // handle to new image list 
    HICON hicon;           // handle to icon 
 
    // Ensure that the common control DLL is loaded. 
    InitCommonControls(); 

    // Create a masked image list large enough to hold the icons. 
    himlIcons = ImageList_Create(CX_ICON, CY_ICON, ILC_MASK, NUM_ICONS, 0); 
 
    // Load the icon resources, and add the icons to the image list. 
    hicon = LoadIcon(hinst, MAKEINTRESOURCE(IDI_BIRD)); 
    g_nBird = ImageList_AddIcon(himlIcons, hicon); 
 
    hicon = LoadIcon(hinst, MAKEINTRESOURCE(IDI_TREE)); 
    g_nTree = ImageList_AddIcon(himlIcons, hicon); 
 
    return himlIcons; 
} 
```



## Related topics

<dl> <dt>

[Image Lists Reference](bumper-image-lists-image-lists-reference.md)
</dt> <dt>

[About Image Lists](image-lists.md)
</dt> <dt>

[Using Image Lists](using-image-lists.md)
</dt> </dl>

 

 




