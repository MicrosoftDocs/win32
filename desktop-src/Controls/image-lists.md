---
title: About Image Lists
description: An image list is a collection of images of the same size, each of which can be referred to by its index.
ms.assetid: 'vs|controls|~\controls\imagelist\imagelist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# About Image Lists

An image list is a collection of images of the same size, each of which can be referred to by its index. Image lists are used to efficiently manage large sets of icons or bitmaps. All images in an image list are contained in a single, wide bitmap in screen device format. An image list can also include a monochrome bitmap that contains masks that are used to draw images transparently (icon style).

The Microsoft Win32 API provides image list functions and macros that enable you to create and destroy image lists, add and remove images, replace and merge images, draw images, and drag images. To use the image list functions, include the common control header file in your source code files and link with the common control export library. In addition, before calling any image list function, use the [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols) or [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function to ensure that the common control DLL is loaded.

The following topics are discussed in this section:

-   [Types](#types)
-   [Creating and Destroying Image Lists](#creating-and-destroying-image-lists)
-   [Adding and Removing Images](#adding-and-removing-images)
-   [Replacing and Merging Images](#replacing-and-merging-images)
-   [Drawing Images](#drawing-images)
-   [Dragging Images](#dragging-images)
-   [Image Information](#image-information)
-   [Image Overlays](#image-overlays)
-   [32-Bit Antialiased Icons](#32-bit-antialiased-icons)

## Types

There are two types of image lists: nonmasked and masked. A nonmasked image list consists of a color bitmap that contains one or more images. A masked image list consists of two bitmaps of equal size. The first is a color bitmap that contains the images, and the second is a monochrome bitmap that contains a series of masks—one for each image in the first bitmap.

When a nonmasked image is drawn, it is simply copied into the target device context; that is, it is drawn over the existing background color of the device context. When a masked image is drawn, the bits of the image are combined with the bits of the mask, typically producing transparent areas in the bitmap where the background color of the target device context shows through. There are several drawing styles that you can specify when drawing a masked image. For example, you can specify that the image be dithered to indicate a selected object.

## Creating and Destroying Image Lists

You create an image list by calling the [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) function. The parameters include the type of image list to create, the dimensions of each image, and the number of images you intend to add to the list. For a nonmasked image list, the function creates a single bitmap large enough to hold the specified number of images of the given dimensions. Then it creates a screen-compatible device context and selects the bitmap into it. For a masked image list, the function creates two bitmaps and two screen-compatible device contexts. It selects the image bitmap into one device context and the mask bitmap into the other. The common control DLL contains the executable code for the image list functions.

In [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create), you specify the initial number of images that will be in an image list as well as the number of images by which the list can grow. So if you attempt to add more images than you initially specified, the image list automatically grows to accommodate the new images.

If [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) succeeds, it returns a handle to the HIMAGELIST type. You use this handle in other image list functions to access the image list and manage the images. You can add and remove images, copy images from one image list to another, and merge images from two different image lists. When you no longer need an image list, you can destroy it by specifying its handle in a call to the [**ImageList\_Destroy**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_destroy) function.

## Adding and Removing Images

You can add bitmapped images, icons, or cursors to an image list. You add bitmapped images by specifying the handles to two bitmaps in a call to the [**ImageList\_Add**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_add) function. The first bitmap contains one or more images to add to the image bitmap, and the second bitmap contains the masks to add to the mask bitmap. For nonmasked image lists, the second bitmap handle is ignored; it can be set to **NULL**.

The [**ImageList\_AddMasked**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_addmasked) function also adds bitmapped images to a masked image list. This function is similar to [**ImageList\_Add**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_add), except that you do not specify a mask bitmap. Instead, you specify a color that the system combines with the image bitmap to automatically generate the masks. Each pixel of the specified color in the image bitmap is changed to black, and the corresponding bit in the mask is set to 1. As a result, any pixel in the image that matches the specified color is transparent when the image is drawn.

The [**ImageList\_AddIcon**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_addicon) macro adds an icon or cursor to an image list. If the image list is masked, **ImageList\_AddIcon** adds the mask that is provided with the icon or cursor to the mask bitmap. If the image list is nonmasked, the mask for the icon or cursor is not used when drawing the image.

You can create an icon based on an image and mask in an image list by using the [**ImageList\_GetIcon**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_geticon) function. The function returns the handle to the new icon.

[**ImageList\_Add**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_add), [**ImageList\_AddMasked**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_addmasked), and [**ImageList\_AddIcon**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_addicon) assign an index to each image as it is added to an image list. The indexes are zero-based; that is, the first image in the list has an index of zero, the next has an index of one, and so on. After adding a single image, the functions return the index of the image. When more than one image is added at a time, the functions return the index of the first image.

The [**ImageList\_Remove**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_remove) function removes an image from an image list.

## Replacing and Merging Images

The [**ImageList\_Replace**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_replace) and [**ImageList\_ReplaceIcon**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_replaceicon) functions replace an image in an image list with a new image. **ImageList\_Replace** replaces an image with a bitmapped image and mask, and **ImageList\_ReplaceIcon** replaces an image with an icon or cursor.

The [**ImageList\_Merge**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_merge) function merges two images, storing the new image in a new image list. The new image is created by drawing the second image transparently over the first. The mask for the new image is the result of performing a logical **OR** operation on the bits of the masks for the two existing images.

## Drawing Images

To draw an image, you use the [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) function. You specify the handle to an image list, the index of the image to draw, the handle to the destination device context, a location within the device context, and one or more drawing styles.

When you specify the **ILD\_TRANSPARENT** style, [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) uses a two-step process to draw a masked image. First, it performs a logical **AND** operation on the bits of the image and the bits of the mask. Then it performs a logical **XOR** operation on the results of the first operation and the background bits of the destination device context. This process creates transparent areas in the resulting image; that is, each white bit in the mask causes the corresponding bit in the resulting image to be transparent.

Before drawing a masked image on a solid color background, you should use the [**ImageList\_SetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_setbkcolor) function to set the background color of the image list to the same color as the destination. Setting the color eliminates the need to create transparent areas in the image and enables [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) to simply copy the image to the destination device context, resulting in a significant increase in performance. To draw the image, specify the **ILD\_NORMAL** style in a call to **ImageList\_Draw** or **ImageList\_DrawEx**.

You can set the background color for a masked image list at any time so that it draws correctly on any solid background. Setting the background color to CLR\_NONE causes images to be drawn transparently by default. To retrieve the background color of an image list, use the [**ImageList\_GetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_getbkcolor) function.

The **ILD\_BLEND25** and **ILD\_BLEND50** styles dither the image with the system highlight color. These styles are useful if you use a masked image to represent an object that the user can select. For example, you can use the **ILD\_BLEND50** style to draw the image when the user selects it.

A nonmasked image is copied to the destination device context by using the SRCCOPY raster operation. The colors in the image appear the same regardless of the background color of the device context. The drawing styles specified in [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) also have no effect on the appearance of a nonmasked image.

## Dragging Images

The Win32 API includes functions for dragging an image on the screen. The dragging functions move an image smoothly, in color, and without any flashing of the cursor. Both masked and unmasked images can be dragged.

The [**ImageList\_BeginDrag**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_begindrag) function begins a drag operation. The parameters include the handle to the image list, the index of the image to drag, and the location of the hot spot within the image. The hot spot is a single pixel that the dragging functions recognize as the exact screen location of the image. Typically, an application sets the hot spot so that it coincides with the hot spot of the mouse cursor. The [**ImageList\_DragMove**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_dragmove) function moves the image to a new location.

The [**ImageList\_DragEnter**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_dragenter) function sets the initial position of the drag image within a window and draws the image at the position. The parameters include the handle to the window in which to draw the image and the coordinates of the initial position within the window. The coordinates are relative to the window's upper-left corner, not the client area. The same is true for all of the image dragging functions that take coordinates as parameters. This means you must compensate for the widths of window elements such as the border, title bar, and menu bar when specifying the coordinates. If you specify a **NULL** window handle when calling **ImageList\_DragEnter**, the dragging functions draw the image in the device context that is associated with the desktop window, and the coordinates are relative to the upper-left corner of the screen.

The [**ImageList\_SetDragCursorImage**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_setdragcursorimage) function creates a new drag image by combining the given image (typically a mouse cursor image) with the current drag image. Because the dragging functions use the new image during a drag operation, you should use the [**ShowCursor**](/windows/desktop/api/winuser/nf-winuser-showcursor) function to hide the actual mouse cursor after calling **ImageList\_SetDragCursorImage**. Otherwise, the system may appear to have two mouse cursors for the duration of the drag operation.

When an application calls [**ImageList\_BeginDrag**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_begindrag), the system creates a temporary, internal image list and then copies the specified drag image to the internal list. You can retrieve the handle to the temporary drag image list by using the [**ImageList\_GetDragImage**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_getdragimage) function. The function also retrieves the current drag position and the offset of the drag image relative to the drag position.

## Image Information

There are a number of functions that retrieve information from an image list. The [**ImageList\_GetImageInfo**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_getimageinfo) function fills an [**IMAGEINFO**](/windows/desktop/api) structure with information about a single image, including the handles of the image and mask bitmaps, the number of color planes and bits per pixel, and the bounding rectangle of the image within the image bitmap. You can use this information to directly manipulate the bitmaps for the image. The [**ImageList\_GetImageCount**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_getimagecount) function retrieves the number of images in an image list.

## Image Overlays

Every image list includes a list of indexes to use as overlays. An overlay is an image that is drawn transparently over another image. Any image currently in the image list can be used as an overlay. You can specify up to four overlays per image list. This limit has been expanded to 15 in version 4.71.

You add the index of an image to the list of overlays by using the [**ImageList\_SetOverlayImage**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_setoverlayimage) function, specifying the handle to the image list, the index of the existing image, and the desired overlay index. This, in effect, tells the image list that "the image at index *x* can be used as an overlay, and I want to refer to the overlay as overlay index *y*." The overlay indexes are one-based rather than zero-based because an overlay index of zero means that no overlay will be used.

You specify an overlay when drawing an image with the [**ImageList\_Draw**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_draw) or [**ImageList\_DrawEx**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_drawex) function. The overlay is specified by performing a logical **OR** operation between the desired drawing flags and the result of the [**INDEXTOOVERLAYMASK**](/windows/desktop/api/Commctrl/nf-commctrl-indextooverlaymask) macro. The **INDEXTOOVERLAYMASK** macro takes the overlay index and formats it for inclusion with the flags for these functions. This will draw the image with the specified overlay. The following example demonstrates how an overlay is added and specified when drawing the image.


```
ImageList_SetOverlayImage(himl, 0, 3);
ImageList_Draw(himl, 1, hdc, 0, 0, ILD_MASK | INDEXTOOVERLAYMASK(3));
```



This will draw image 1 and then overlay that image with image 0. Because 3 is the overlay index that you specified in the [**ImageList\_SetOverlayImage**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_setoverlayimage) call, 3 is placed in the [**INDEXTOOVERLAYMASK**](/windows/desktop/api/Commctrl/nf-commctrl-indextooverlaymask) macro.

## 32-Bit Antialiased Icons

Antialiasing is a technique for softening or blurring sharp edges. This gives images a more natural appearance. Image lists in Windows Vista and Windows 7 support the use of 32-bit antialiased icons and bitmaps. Color values use 24 bits, and 8 bits are used as an alpha channel on the icons. To create an image list that can handle a 32 bits-per-pixel (bpp) image, call the [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) function, passing in an ILC\_COLOR32 flag.

To author 32-bit icons correctly, you must create multiple images for each icon, as shown in the following illustration.

![illustration showing three sizes of icons for each of three color depths](images/theme2.png)

-   The first three images are in 16-color mode for use in safe mode.
-   The next three icons are used in 256-color mode.
-   The last three icons have the alpha channel and can be used only in operating systems running 24-bit color or higher.
-   The order of images in the icon format does matter. If the order is wrong, older versions of Windows function poorly when extracting the icons. Extracting the icons incorrectly can cause memory corruption and improper rendering.
-   Previous versions of Windows had a 10-icon resource limit.

> [!Note]  
> You can use third party tools to generate icon files and bitmaps that contain an alpha channel. If you use [**LoadImage**](/windows/desktop/api/winuser/nf-winuser-loadimagea) to load a 32 bpp bitmap that contains alpha, you need to specify the LR\_CREATEDIBSECTION flag.

 

 

 