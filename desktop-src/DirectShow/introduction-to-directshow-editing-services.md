---
description: Introduction to DirectShow Editing Services
ms.assetid: 247c4ba9-53c1-46ed-83ef-a454351920e3
title: Introduction to DirectShow Editing Services
ms.topic: article
ms.date: 05/31/2018
---

# Introduction to DirectShow Editing Services

\[This API is not supported and may be altered or unavailable in the future.\]

The core of DirectShow is a powerful architecture for handling streaming media. An application can use it to play multimedia content authored in a wide variety of formats, without the developer needing to worry about file compression and other tedious details. Prior to [DirectShow Editing Services](directshow-editing-services.md) (DES), however, DirectShow lacked the flexibility needed for nonlinear editing.

For example, suppose you wanted to create a video sequence consisting of 4 seconds from source A, followed by 10 seconds from source B, and ending with 5 seconds from source C. You could accomplish that much fairly easily using only the core DirectShow API.

But what if you decided that source C should come before source B, not after; that the sequence should use 8 seconds from source A, not 4; and that the entire production needed a separate audio track playing in the background? Even minor changes such as these could be difficult to implement. But the scenario just described is a trivial editing project in DES—you can do it with a handful of method calls.

Here are some of the features that DES brings to DirectShow:

-   A timeline model that organizes video and audio tracks into nested layers, making it easy to manipulate the final production
-   The ability to preview a video project on the fly
-   Project persistence through an XML-based format
-   Support for video and audio effects, as well as transitions between video tracks (such as fades and wipes)
-   Over 100 standard wipes, as defined by the Society of Motion Picture and Television Engineers (SMPTE)
-   Keying based on hue, luminance, RGB value, or alpha value
-   Automatic conversion of frame rates and audio sampling rates, enabling a production to use heterogeneous sources
-   Resizing or cropping of video

Limitations:

-   DES does not support MPEG-2 or H.264 video sources.

## Related topics

<dl> <dt>

[DirectShow Editing Services](directshow-editing-services.md)
</dt> </dl>

 

 



