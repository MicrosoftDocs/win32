---
title: Providing Controls for Cropping and Stretching Images
description: Providing Controls for Cropping and Stretching Images
ms.assetid: cc62d70d-3f5f-477c-bc09-ab8ab0a9dce3
keywords:
- MCIWndGetSource macro
- MCIWndPutSource macro
- MCIWndGetDest macro
- MCIWndPutDest macro
ms.topic: article
ms.date: 05/31/2018
---

# Providing Controls for Cropping and Stretching Images

MCIWnd allows you to crop and stretch images of a video clip. To understand these features, you need to understand the relationships between *frame size*, *source rectangle*, *destination rectangle*, and *playback area*.

A video clip consists of several frames, each containing one image. The frame size of a video clip is the size of the image in the current frame. Typically, a video clip has one frame size because all the images in the clip are the same size.

The source rectangle is a rectangular area that overlays the frames of a video clip. The source rectangle defines the portion of each frame that is displayed during playback. When a video clip is loaded with MCIWnd, the source rectangle is initialized with the same dimensions and position as the initial frame of the video clip.

The destination rectangle is a rectangular area that defines a virtual playback window. The destination rectangle receives the image data from the source rectangle for each frame of the video clip. When the source and destination rectangle dimensions are different, MCIWnd adjusts the image data horizontally and vertically as needed to fill the destination rectangle. When a video clip is loaded with MCIWnd, the destination rectangle is initialized with the same dimensions and position as the initial frame of the video clip.

The playback area is the portion of an MCIWnd window an application uses to display the video clip. The playback area is the client area of an MCIWnd window or the portion of the client area that excludes the MCIWnd toolbar. When a video clip is loaded with MCIWnd, the playback area is initialized with the same dimensions and position as the initial frame of the video clip.

You can crop a video clip by using the [**MCIWndGetSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetsource) and [**MCIWndPutSource**](/windows/desktop/api/Vfw/nf-vfw-mciwndputsource) macros to alter the source rectangle. Cropping an image determines only which portion of the frames are displayed during playback; it does not alter the content of the file being played. Before you crop an image, you can retrieve the current size of the source rectangle by using **MCIWndGetSource**. After the new size and location of the source rectangle are calculated, you can set the cropping boundaries of the source rectangle by using **MCIWndPutSource**.

You can stretch a video clip by using the [**MCIWndGetDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdest) and [**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest) macros to alter the destination rectangle. When you stretch a video clip, you lengthen or shorten the frame size of a video clip vertically, horizontally, or in both directions. Before you stretch an image, you can retrieve the current size and location of the destination rectangle by using **MCIWndGetDest**. The **MCIWndPutDest** macro allows you to redefine the destination rectangle. Stretching can distort the image during playback, but it does not alter the content of the file being played.

If the size of the destination rectangle becomes larger than the playback area, you can specify which portion of the playback area will display the video clip by using **MCIWndPutDest**.

> [!Note]  
> The [**MCIWndPutDest**](/windows/desktop/api/Vfw/nf-vfw-mciwndputdest) macro does not change the size of the playback area. To stretch the MCIWnd window along with the destination rectangle, you need to know the current size of the MCIWnd window and issue new window dimensions based on the destination rectangle. You can retrieve the MCIWnd window dimensions by using the [GetWindowRect](/windows/win32/api/winuser/nf-winuser-getwindowrect) function and resize the MCIWnd window by using the [SetWindowPos](/windows/win32/api/winuser/nf-winuser-setwindowpos) function.

 

 

 