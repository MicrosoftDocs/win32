---
description: Pure virtual method that derived classes override.
ms.assetid: 05c73f6b-27f4-4930-b4d5-1688b6bf1791
title: CBaseControlVideo.GetStaticImage method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetStaticImage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.GetStaticImage method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Pure virtual method that derived classes override.

## Syntax


```C++
virtual HRESULT GetStaticImage(
   long *pBufferSize,
   long *pDIBImage
) = 0;
```



## Parameters

<dl> <dt>

*pBufferSize* 
</dt> <dd>

Pointer to the size of the output buffer.

</dd> <dt>

*pDIBImage* 
</dt> <dd>

Pointer to the output buffer.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface, an application can request that it be given a copy of the current image in a memory buffer (some renderers can return E\_NOTIMPL to this if they do not support it). The derived class determines how to retrieve the image. When the application calls **CBaseControlVideo::GetStaticImage**, it calls this pure virtual method that the derived class should override to implement it. This is also called by the [**CBaseControlVideo::GetCurrentImage**](cbasecontrolvideo-getcurrentimage.md) member function.

The class provides a helper member function, [**CBaseControlVideo::CopyImage**](cbasecontrolvideo-copyimage.md), that can be given a sample that contains an image, and the member function will copy the relevant section of it (based on the current source rectangle) into the output buffer supplied by the application.

The following example demonstrates an implementation of this member function in a derived class. In this example, m\_pRenderer holds an object of a class derived from [**CBaseVideoRenderer**](cbasevideorenderer.md).


```C++
// Return a copy of the current image in the video renderer
HRESULT CVideoText::GetStaticImage(long *pBufferSize,long *pDIBImage)
{
    // Get any sample the renderer may be holding.

    IMediaSample *pMediaSample = m_pRenderer->GetCurrentSample();
    if (pMediaSample == NULL) {
        return E_UNEXPECTED;
    }

    // Call the base class helper method to do the work.

    HRESULT hr = CopyImage(pMediaSample,       // Buffer containing image
                      &m_pRenderer->m_mtIn,    // Type representing bitmap
                      pBufferSize,             // Size of buffer for DIB
                     (BYTE*) pDIBImage);       // Data buffer for output

    pMediaSample->Release();
    return hr;
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




