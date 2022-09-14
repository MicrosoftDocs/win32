---
description: Set allocator properties as part of writing a transform filter. The transform filter's output pin selects the downstream allocator.
ms.assetid: c2fd6d8b-b239-45e4-9c02-41edafa58762
title: Step 4. Set Allocator Properties
ms.topic: article
ms.date: 05/31/2018
---

# Step 4. Set Allocator Properties

This is step 4 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

> [!Note]  
> This step is not required for filters that derive from **CTransInPlaceFilter**.

 

After two pins agree on a media type, they select an allocator for the connection and negotiate allocator properties, such as the buffer size and the number of buffers.

In the **CTransformFilter** class, there are two allocators, one for the upstream pin connection and one for the downstream pin connection. The upstream filter selects the upstream allocator and also chooses the allocator properties. The input pin accepts whatever the upstream filter decides. If you need to modify this behavior, override the [**CBaseInputPin::NotifyAllocator**](cbaseinputpin-notifyallocator.md) method.

The transform filter's output pin selects the downstream allocator. It performs the following steps:

1.  If the downstream filter can provide an allocator, the output pin uses that one. Otherwise, the output pin creates a new allocator.
2.  The output pin gets the downstream filter's allocator requirements (if any) by calling [**IMemInputPin::GetAllocatorRequirements**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocatorrequirements).
3.  The output pin calls the transform filter's [**CTransformFilter::DecideBufferSize**](ctransformfilter-decidebuffersize.md) method, which is pure virtual. The parameters to this method are a pointer to the allocator and an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure with the downstream filter's requirements. If the downstream filter has no allocator requirements, the structure is zeroed out.
4.  In the **DecideBufferSize** method, the derived class sets the allocator properties by calling [**IMemAllocator::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-setproperties).

Generally, the derived class will select allocator properties based on the output format, the downstream filter's requirements, and the filter's own requirements. Try to select properties that are compatible with the downstream filter's request. Otherwise, the downstream filter might reject the connection.

In the following example, the RLE encoder sets minimum values for the buffer size, buffer alignment, and buffer count. For the prefix, it uses whatever value the downstream filter requested. The prefix is typically zero bytes, but some filters require it. For example, the [AVI Mux](avi-mux-filter.md) filter uses the prefix to write RIFF headers.


```C++
HRESULT CRleFilter::DecideBufferSize(
    IMemAllocator *pAlloc, ALLOCATOR_PROPERTIES *pProp)
{
    AM_MEDIA_TYPE mt;
    HRESULT hr = m_pOutput->ConnectionMediaType(&mt);
    if (FAILED(hr))
    {
        return hr;
    }

    ASSERT(mt.formattype == FORMAT_VideoInfo);
    BITMAPINFOHEADER *pbmi = HEADER(mt.pbFormat);
    pProp->cbBuffer = DIBSIZE(*pbmi) * 2; 
    if (pProp->cbAlign == 0)
    {
        pProp->cbAlign = 1;
    }
    if (pProp->cBuffers == 0)
    {
        pProp->cBuffers = 1;
    }
    // Release the format block.
    FreeMediaType(mt);

    // Set allocator properties.
    ALLOCATOR_PROPERTIES Actual;
    hr = pAlloc->SetProperties(pProp, &Actual);
    if (FAILED(hr)) 
    {
        return hr;
    }
    // Even when it succeeds, check the actual result.
    if (pProp->cbBuffer > Actual.cbBuffer) 
    {
        return E_FAIL;
    }
    return S_OK;
}
```



The allocator may not be able to match your request exactly. Therefore, the **SetProperties** method returns the actual result in a separate **ALLOCATOR\_PROPERTIES** structure (the *Actual* parameter, in the previous example). Even when **SetProperties** succeeds, you should check the result to make sure they meet your filter's minimum requirements.

**Custom Allocators**

By default, all of the filter classes use the [**CMemAllocator**](cmemallocator.md) class for their allocators. This class allocates memory from the virtual address space of the client process (using **VirtualAlloc**). If your filter needs to use some other kind of memory, such as DirectDraw surfaces, you can implement a custom allocator. You can use the [**CBaseAllocator**](cbaseallocator.md) class or write an entirely new allocator class. If your filter has a custom allocator, override the following methods, depending on which pin uses the allocator:

-   Input pin: [**CBaseInputPin::GetAllocator**](cbaseinputpin-getallocator.md) and [**CBaseInputPin::NotifyAllocator**](cbaseinputpin-notifyallocator.md).
-   Output pin: [**CBaseOutputPin::DecideAllocator**](cbaseoutputpin-decideallocator.md).

If the other filter refuses to connect using your custom allocator, your filter can either fail the connection, or else connect with the other filter's allocator. In the latter case, you might need to set an internal flag indicating the type of allocator. For an example of this approach, see [**CDrawImage Class**](cdrawimage.md).

Next: [Step 5. Transform the Image](step-5--transform-the-image.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



