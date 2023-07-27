---
description: Writing Transform Filters
ms.assetid: ce84756b-34ee-4710-8f0f-7553733ca10a
title: Writing Transform Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Transform Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to write a transform filter, defined as a filter that has exactly one input pin and one output pin. To illustrate the steps, this section describes a hypothetical transform filter that outputs run-length encoded (RLE) video. It does not describe the RLE-encoding algorithm itself, only the tasks that are specific to DirectShow. (DirectShow already provides an RLE codec through the [AVI Compressor](avi-compressor-filter.md) filter.)

This section assumes that you will use the DirectShow base class library to create filters. Although you can write a filter without it, the base class library is strongly recommended.

> [!Note]  
> Before writing a transform filter, consider whether a DirectX Media Object (DMO) would fulfill your requirements. DMOs can do many of the same things as filters, and the programming model for DMOs is simpler. DMOs are hosted in DirectShow through the [DMO Wrapper](dmo-wrapper-filter.md) filter, but can also be used outside of DirectShow. DMOs are now the recommended solution for encoders and decoders.

 

This section includes the following topics:

-   [Step 1. Choose a Base Class](step-1--choose-a-base-class.md)
-   [Step 2. Declare the Filter Class](step-2--declare-the-filter-class.md)
-   [Step 3. Support Media Type Negotiation](step-3--support-media-type-negotiation.md)
-   [Step 4. Set Allocator Properties](step-4--set-allocator-properties.md)
-   [Step 5. Transform the Image](step-5--transform-the-image.md)
-   [Step 6. Add Support for COM](step-6--add-support-for-com.md)

## Related topics

<dl> <dt>

[Building DirectShow Filters](building-directshow-filters.md)
</dt> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



