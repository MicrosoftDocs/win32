---
title: Using the Stream Buffer Engine with the Video Control
description: Using the Stream Buffer Engine with the Video Control
ms.assetid: 41b458d6-e2c1-4587-9342-91aa13f91b86
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Stream Buffer Engine with the Video Control

This topic applies to Windows XP Service Pack 1 or later.

The Video Control can pause a live video stream using the Stream Buffer Engine.

To do so, create two instances of the Video Control. The first instance is for creating the tune request and recording the content into the stream buffer. The second instance is for playing back the content from the stream buffer.

Using the first instance of the Video Control, do the following:

1.  Create a tune request.
2.  Pass the tune request to the Video Control by calling the **View** method.
3.  Add the video encoder feature (CLSID\_MSVidEncoder) to the active features collection.
4.  Enumerate the available output devices in the GUID\_NULL category. Find the Stream Buffer Sink device and set it to be the active output device.
5.  Specify a file name for the output device.
6.  Disable video and audio rendering.
7.  Run the Video Control.

Using the second instance of the Video Control, do the following:

1.  Enumerate the available input devices in the GUID\_NULL category. Set the Stream Buffer Source device as the active input device.
2.  Specify the same file name used previously in step 5 of the first instance of the Video Control.
3.  Run the Video Control.

## Related topics

<dl> <dt>

[Using the Video Control](using-the-video-control.md)
</dt> </dl>

 

 




