---
title: How to Draw an Image
description: This topic demonstrates how to use the ImageList\_Draw function to draw an image.
ms.assetid: BE2F20F3-B7D3-4FA2-B1E9-60A47A609C36
ms.topic: article
ms.date: 05/31/2018
---

# How to Draw an Image

This topic demonstrates how to use the [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) function to draw an image.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


To draw an image, you use the [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) function. You specify the handle to an image list, the index of the image to draw, the handle to the destination device context, a location within the device context, and one or more drawing styles.

The user-defined function in the following C++ code example uses the [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) function to draw an image and saves the client coordinates of the image's bounding rectangle. A subsequent function uses the bounding rectangle to determine whether the user has clicked on the image.



```C++
// DrawTheImage - draws an image transparently and saves 
// the bounding rectangle of the drawn image.
// Returns TRUE if successful, or FALSE otherwise. 
// hwnd - handle to the window in which to draw the image. 
// himl - handle to the image list that contains the image. 
// cx and cy - client coordinates for the upper-left corner of the image. 
// 
// Global variables and constants 
//     g_nImage - index of the image to draw. 
//     g_rcImage - bounding rectangle of the image. 
//     CX_IMAGE and CY_IMAGE - width and height of the image. 
extern int g_nImage; 
extern RECT g_rcImage; 
 
#define CX_IMAGE 32 
#define CY_IMAGE 32 
 
BOOL DrawTheImage(HWND hwnd, HIMAGELIST himl, int cx, int cy) 
{ 
    HDC hdc; 
 
    if ((hdc = GetDC(hwnd)) == NULL) 
        return FALSE; 
    if (!ImageList_Draw(himl, g_nImage, hdc, cx, cy, ILD_TRANSPARENT)) 
        return FALSE; 
    ReleaseDC(hwnd, hdc); 
 
    SetRect(&g_rcImage, cx, cy, CX_IMAGE + cx, CY_IMAGE + cy); 
 
    return TRUE; 
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

 

 




