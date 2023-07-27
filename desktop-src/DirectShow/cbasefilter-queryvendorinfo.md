---
description: The QueryVendorInfo method retrieves a string containing vendor information. This method implements the IBaseFilter::QueryVendorInfo method.
ms.assetid: 083c0556-d516-4daf-8621-e158ea78b5a3
title: CBaseFilter.QueryVendorInfo method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.QueryVendorInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseFilter.QueryVendorInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueryVendorInfo` method retrieves a string containing vendor information. This method implements the [**IBaseFilter::QueryVendorInfo**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-queryvendorinfo) method.

## Syntax


```C++
HRESULT QueryVendorInfo(
   LPWSTR *pVendorInfo
);
```



## Parameters

<dl> <dt>

*pVendorInfo* 
</dt> <dd>

Address of a variable that receives a pointer to a wide-character string containing the vendor information.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

To provide vendor information for a filter, override this method. If you implement this method, use the **CoTaskMemAlloc** function to allocate memory for the string. The caller is responsible for calling the **CoTaskMemFree** function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




