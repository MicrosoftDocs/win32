---
description: Step 1.
ms.assetid: 4b2d3add-0430-480b-ad5f-bb1aa19fef21
title: Step 1. Choose a Base Class
ms.topic: article
ms.date: 05/31/2018
---

# Step 1. Choose a Base Class

This is step 1 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

Assuming that you decide to write a filter and not a DMO, the first step is choosing which base class to use. The following classes are appropriate for transform filters:

-   [**CTransformFilter**](ctransformfilter.md) is designed for transform filters that use separate input and output buffers. This kind of filter is sometimes called a copy-transform filter. When a copy-transform filter receives an input sample, it writes new data to an output sample and delivers the output sample to the next filter.
-   [**CTransInPlaceFilter**](ctransinplacefilter.md) is designed for filters that modify data in the original buffer, also called trans-in-place filters. When a trans-in-place filter receives a sample, it changes the data inside that sample and delivers the same sample downstream. The filter's input pin and output pin always connect with matching media types.
-   [**CVideoTransformFilter**](cvideotransformfilter.md) is designed primarily for video decoders. It derives from **CTransformFilter**, but includes functionality for dropping frames if the downstream renderer falls behind.
-   [**CBaseFilter**](cbasefilter.md) is a generic filter class. The other classes in this list all derive from **CBaseFilter**. If none of them is suitable, you can fall back on this class. However, this class also requires the most work on your part.
-   \[!Important\]  
    > In-place video transforms can have a serious impact on rendering performance. In-place transforms require read-modify-write operations on the buffer. If the memory resides on a graphics card, read operations are significantly slower. Moreover, even a copy transform can cause unintended read operations if you do not implement it carefully. Therefore, you should always do performance testing if you write a video transform.

     

For the example RLE encoder, the best choice is either **CTransformFilter** or **CVideoTransformFilter**. In fact, the differences between them are largely internal, so it is easy to convert from one to the other. Because the media types must be different on the two pins, the **CTransInPlaceFilter** class is not appropriate for this filter. This example will use **CTransformFilter**.

Next: [Step 2. Declare the Filter Class](step-2--declare-the-filter-class.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



