---
description: The RegisterMediaTime method caches the time stamps from the current sample.
ms.assetid: 9ff8e4ec-3401-4272-894d-643f0fc029de
title: CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h)

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



 

 




