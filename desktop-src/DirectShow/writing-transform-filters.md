---
description: Writing Transform Filters
ms.assetid: ce84756b-34ee-4710-8f0f-7553733ca10a
title: Writing Transform Filters
ms.topic: article
ms.date: 05/31/2018
---

# Writing Transform Filters

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

 

 



