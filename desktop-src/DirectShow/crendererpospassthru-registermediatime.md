---
description: The RegisterMediaTime method caches the time stamps from the current sample.
ms.assetid: 9ff8e4ec-3401-4272-894d-643f0fc029de
title: CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererPosPassThru.RegisterMediaTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **RegisterMediaTime** method caches the time stamps from the current sample.

## Syntax


```C++
HRESULT RegisterMediaTime(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                                  | Description                                |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                        |
| <dl> <dt>**VFW\_E\_MEDIA\_TIME\_NOT\_SET**</dt> </dl> | The sample is not time-stamped.<br/> |



 

## Remarks

This method stores the time stamps from the current sample. The [**CRendererPosPassThru::GetMediaTime**](crendererpospassthru-getmediatime.md) method retrieves the same values.

The filter should call this method for each sample that it receives. The method is overloaded to accept either a pointer to the sample, or the time stamp values themselves.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




