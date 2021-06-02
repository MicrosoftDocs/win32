---
description: Grabbing a Poster Frame
ms.assetid: 0727a1ed-1bc7-49fc-a288-00283e637a71
title: Grabbing a Poster Frame
ms.topic: article
ms.date: 05/31/2018
---

# Grabbing a Poster Frame

\[This API is not supported and may be altered or unavailable in the future.\]

This article describes how to display a poster frame from a digital media file, using the [Media Detector (MediaDet)](media-detector--mediadet.md) object provided with [DirectShow Editing Services](directshow-editing-services.md).

The Media Detector is a helper object that can get format information from a media source file. It can also grab a bitmap image from a video stream in the source file. Assuming the file is seekable, you can obtain the image from any point in the file. The returned image is always in 24-bit RGB format.

The Media Detector is not a filter, and the application does not need to use the Filter Graph Manager or create a filter graph. Internally, the Media Detector creates a filter graph that contains the [**Sample Grabber Filter**](sample-grabber-filter.md). To get a bitmap, the Media Detector seeks and pauses the filter graph, and then retrieves the bitmap from the Sample Grabber filter. The application communicates with the Media Detector through the [**IMediaDet**](imediadet.md) interface. The Media Detector is a good example of encapsulating a filter graph inside a helper object, in order to shield applications from graph-related details.

The Media Detector operates in two modes. When you first create it, the Media Detector is in "information gathering" mode. You can specify the name of a media file and get information about each of the streams in the file, such as the format type, the frame rate, or the duration. If the file contains a video stream, you can switch the Media Detector into "bitmap grab" mode and retrieve bitmaps from the source. However, once you do so, you cannot switch the Media Detector back to its original mode; it is permanently attached to that video stream. To work with another stream or another file, you must create a new instance of the Media Detector.

> [!Note]  
> The code examples in this tutorial use the ATL **CComPtr** class, which automatically manages reference counts. If you prefer to use raw interface pointers, remember to release every interface when you are done with it. Also, for brevity the code examples omit much of the error checking that an application should perform. In working code, always check **HRESULT** values.

 

This tutorial contains the following steps:

-   [Step 1: Create the Windows Framework](step-1--create-the-windows-framework.md)
-   [Step 2: Add a Menu Command to Grab a Poster Frame](step-2--add-a-menu-command-to-grab-a-poster-frame.md)
-   [Step 3: Implement the Frame-Grabbing Function](step-3--implement-the-frame-grabbing-function.md)
-   [Step 4: Draw the Bitmap on the Client Area](step-4--draw-the-bitmap-on-the-client-area.md)

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 



