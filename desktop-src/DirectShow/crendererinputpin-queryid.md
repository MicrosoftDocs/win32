---
description: The QueryId method retrieves the pin identifier. This method overrides the CBasePin::QueryId method.
ms.assetid: 9543234c-5349-49d0-b410-1c461ee4eabe
title: CRendererInputPin.QueryId method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.QueryId
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRendererInputPin.QueryId method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueryId` method retrieves the pin identifier. This method overrides the [**CBasePin::QueryId**](cbasepin-queryid.md) method.

## Syntax


```C++
HRESULT QueryId(
   LPWSTR *Id
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Receives a string containing the pin identifier.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument<br/> |



 

## Remarks

This method allocates the wide-character string "In" and assigns it to the *Id* parameter. The caller must free the allocated memory, using the **CoTaskMemFree** function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




