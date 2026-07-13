---
description: The DeleteMediaType function deletes an allocated AM\_MEDIA\_TYPE structure, including the format block.
ms.assetid: 970f6b2b-2bf5-418d-b4ae-637561cd6765
title: DeleteMediaType function (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeleteMediaType
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DeleteMediaType function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DeleteMediaType** function deletes an allocated [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure, including the format block.

## Syntax


```C++
void WINAPI DeleteMediaType(
   AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

A pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use this function to release any media type structure that was allocated using either [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) or [**CreateMediaType**](createmediatype.md).

This function is defined in the [DirectShow Base Classes](directshow-base-classes.md) library. If you prefer not to link to the base class library, you can use the following code:


```C++
// Release the format block for a media type.

void _FreeMediaType(AM_MEDIA_TYPE& mt)
{
    if (mt.cbFormat != 0)
    {
        CoTaskMemFree((PVOID)mt.pbFormat);
        mt.cbFormat = 0;
        mt.pbFormat = NULL;
    }
    if (mt.pUnk != NULL)
    {
        // pUnk should not be used.
        mt.pUnk->Release();
        mt.pUnk = NULL;
    }
}


// Delete a media type structure that was allocated on the heap.
void _DeleteMediaType(AM_MEDIA_TYPE *pmt)
{
    if (pmt != NULL)
    {
        _FreeMediaType(*pmt); 
        CoTaskMemFree(pmt);
    }
}
```





## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**FreeMediaType**](freemediatype.md)
</dt> <dt>

[**Media Type Functions**](media-type-functions.md)
</dt> </dl>

 

