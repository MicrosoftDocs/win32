---
description: Source and Target Rectangles in Video Renderers
ms.assetid: fdddbffb-c44f-4364-9e2e-b721ba39c74f
title: Source and Target Rectangles in Video Renderers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Source and Target Rectangles in Video Renderers

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are three sizes found in the [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo), [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader), and [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) format structures of video media types. This article explains what they are and how they work.

First, there is a size in the **bmiHeader** member of these structures. The **bmiHeader** member is a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure with its own width and height members, **bmiHeader.biWidth** and **bmiHeader.biHeight**.

Second, there is a rectangle in the **rcSource** member of these structures; and last, there is a rectangle in the **rcTarget** member of these structures.

Assume you have two filters, A and B, and that these filters are connected to each other (A on the left, or upstream, and B on the right, or downstream) with a certain video media type.

The buffers that pass between filters A and B have the size (**bmiHeader.biWidth**, **bmiHeader.biHeight**). Filter A should take a portion of its input video determined by **rcSource** and stretch that video to fill the **rcTarget** portion of the buffer. The portion of the input video to use is based on how **rcSource** compares to the (**biWidth**, **biHeight**) size of the media type that filters A and B originally connected with. If **rcSource** is empty, filter A uses its entire input video. If **rcTarget** is empty, filter A fills the entire output buffer.

For example, assume filter A is receiving video data that is 160 x 120 pixels. Assume also that filter A is connected to filter B with the following media type.

-   (**biWidth**, **biHeight**): 320, 240
-   **rcSource**: (0, 0, 0, 0)
-   **rcTarget**: (0, 0, 0, 0)

This means that filter A will stretch the video it receives by 2 in both the x and y directions, and fill a 320 x 240 output buffer.

As another example, assume filter A is receiving 160 x 120 video data, and that it is connected to filter B with the following media type.

-   (**biWidth**, **biHeight**): 320, 240
-   **rcSource**: (0, 0, 160, 240)
-   **rcTarget**: (0, 0, 0, 0)

The **rcSource** member is relative to the connected buffer size of 320, 240. Because the specified **rcSource** (0, 0, 160, 240) is the left half of the buffer, filter A will take the left half of its input video, or the (0, 0, 80, 120) portion, and stretch the video to a size of (320, 240) (by 4 in the x direction, and by 2 in the y direction) and filling the 320 x 240 output buffer.

Now assume that filter A calls [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md), and the media sample returned has a media type attached to it, signifying that filter B wants filter A to provide a different size or kind of video than it has previously been providing. Assume the new media type is:

-   (**biWidth**, **biHeight**): 640, 480
-   **rcSource**: (0, 0, 160, 120)
-   **rcTarget**: (0, 0, 80, 60)

This means that the media sample has a buffer that is 640 x 480 in size. The **rcSource** member is relative to the original connected media type (320, 240) not to the new media type of (640, 480), so **rcSource** specifies that the top-left corner (25%) of the input video is to be used. This portion of the input video is placed in the top-left (80, 60) pixels of the 640 x 480 output buffer, as specified by **rcTarget** of (0, 0, 80, 60). Because filter A is receiving 160 x 120 video, the top-left corner of the input video is an (80, 60) piece, the same size of the output bitmap, and no stretching is required.

Filter A will place no data in the other pixels of the output buffer, and will leave those bits untouched. The **rcSource** member is bounded by the **biWidth** and **biHeight** of the original connected media type between filters A and B, and **rcTarget** is bounded by the new **biWidth** and **biHeight** of the media sample. In the preceding example, **rcSource** could not go outside the boundaries of (0, 0, 320, 240) and **rcTarget** could not go outside the boundaries of (0, 0, 640, 480).

 

 



