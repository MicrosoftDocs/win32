---
title: Sequences of Images
description: Sequences of Images
ms.assetid: fbfb944c-a927-4c92-b3d6-2f8c278408e6
keywords:
- DrawDib,image sequences
- DrawDib,sequence of bitmaps
- DrawDibDraw function
- DrawDibBegin function
- DrawDibEnd function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sequences of Images

You can display a sequence of bitmaps with the same dimensions and formats by using the [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) function with the [**DrawDibBegin**](/windows/win32/Vfw/nf-vfw-drawdibbegin?branch=master) function. **DrawDibBegin** improves the efficiency of **DrawDibDraw** by preparing the DrawDib DC for drawing.

> [!Note]  
> If your application does not use [**DrawDibBegin**](/windows/win32/Vfw/nf-vfw-drawdibbegin?branch=master), [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) implicitly executes it prior to drawing. If your application uses **DrawDibBegin** prior to **DrawDibDraw**, **DrawDibDraw** does not have to process the function and wait for it to complete.

 

The [**DrawDibBegin**](/windows/win32/Vfw/nf-vfw-drawdibbegin?branch=master) function provides [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) with the DrawDib DC, the DC handle, the address of the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd318229) structure, and the source and destination rectangle dimensions. When you display a sequence of bitmaps, **DrawDibDraw** checks the values of these items for each image in the sequence. If **DrawDibDraw** detects changes to any of these items, it implicitly calls **DrawDibBegin** again to adjust the DrawDib DC settings.

After using [**DrawDibBegin**](/windows/win32/Vfw/nf-vfw-drawdibbegin?branch=master), you can draw the image sequence by using [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) and specifying one or more flags as appropriate. Specify the **DDF\_SAME\_HDC** flag as long as the DC handle has not changed. Specify the DDF\_SAME\_DRAW flag when the following parameters for **DrawDibDraw** have not changed: the address of the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd318229) structure and the source and destination rectangle dimensions.

You can update the flags set with [**DrawDibBegin**](/windows/win32/Vfw/nf-vfw-drawdibbegin?branch=master) by using the [**DrawDibEnd**](/windows/win32/Vfw/nf-vfw-drawdibend?branch=master) function followed by another call to **DrawDibBegin**. Then use **DrawDibEnd** to clear the DrawDib DC of its current flags and settings. The subsequent call to **DrawDibBegin** reinitializes the DrawDib DC with the appropriate flags and settings. Alternatively, you can update the flags for a DrawDib DC by using **DrawDibBegin** without **DrawDibEnd**. To do this, you must change at least one of the following settings concurrently with the flags: the address of the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd318229) structure, or the source or destination rectangle dimensions.

You can increase the efficiency of [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) for data-streaming operations that use compressed images, such as playing a video clip, by using the [**DrawDibStart**](/windows/win32/Vfw/nf-vfw-drawdibstart?branch=master) and [**DrawDibStop**](/windows/win32/Vfw/nf-vfw-drawdibstop?branch=master) functions. The **DrawDibStart** function prepares the DrawDib DC to receive a stream of images by sending a message to the video compression manager (VCM). When streaming has ended, **DrawDibStop** sends a message to VCM indicating that it can release resources it allocated for the data-streaming operation. For more information about VCM, see [Video Compression Manager](video-compression-manager.md).

> [!Note]  
> You must specify the width and height of the source and destination rectangles in your application. However, you do not need to specify the origins of the rectangles. Your application can redefine the origins in [**DrawDibDraw**](/windows/win32/Vfw/nf-vfw-drawdibdraw?branch=master) to use different portions of the image or to update different portions of the display.

 

## Related topics

<dl> <dt>

[Image Rendering](image-rendering.md)
</dt> </dl>

 

 




