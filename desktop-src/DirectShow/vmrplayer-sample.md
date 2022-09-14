---
description: VMRPlayer Sample
ms.assetid: 7fc893a6-afa5-4ada-9295-29122b43b21e
title: VMRPlayer Sample
ms.topic: article
ms.date: 05/31/2018
---

# VMRPlayer Sample

## Description

This sample uses the Video Mixing Renderer 9 (VMR-9) filter to alpha blend one or two running videos and a static image.

## Usage

To open the first video, choose **Open Primary Stream** from the **File** menu. To open a second video, choose **Open Secondary Stream** from the **File** menu (you must open the primary stream first). To play the video, click the **Play** button.

You can set the position, size, and alpha values of the videos by selecting **Primary Stream** or **Secondard Stream** from the **VMR Properties** menu.

To add a static bitmap over the video, choose **Static App Image** from the **VMR Properties** menu and click the **Display App Image** box. You can use the same dialog to control the position, size, and alpha value of the bitmap.

To capture the blended video image, choose **Capture Bitmap Image** from the **VMR Properties** menu.

You can also specify the primary image stream from the command line:

**VMRPlayer** **/P** *filename*

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



