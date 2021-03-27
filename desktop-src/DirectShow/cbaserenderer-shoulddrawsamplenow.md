---
description: The ShouldDrawSampleNow method determines how a sample is scheduled for rendering.
ms.assetid: 92994f1f-53d5-42d4-90a2-2984b693e4c0
title: CBaseRenderer.ShouldDrawSampleNow method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.ShouldDrawSampleNow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.ShouldDrawSampleNow method

The `ShouldDrawSampleNow` method determines how a sample is scheduled for rendering.

## Syntax


```C++
virtual HRESULT ShouldDrawSampleNow(
   IMediaSample   *pMediaSample,
   REFERENCE_TIME *pStartTime,
   REFERENCE_TIME *pEndTime
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> <dt>

*pStartTime* 
</dt> <dd>

Pointer to a variable that contains the sample's start time.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to a variable that contains the sample's end time.

</dd> </dl>

## Return value

Returns S\_FALSE. If the derived class overrides this method, return one of the values shown in the following table.



| Return code                                                                               | Description                                                                        |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The sample should be rendered immediately.<br/>                              |
| <dl> <dt>**S\_FALSE**</dt> </dl>   | The sample should be scheduled for rendering, based on the time stamps.<br/> |
| <dl> <dt>**Error code**</dt> </dl> | Do not render this sample.<br/>                                              |



 

## Remarks

The [**CBaseRenderer::GetSampleTimes**](cbaserenderer-getsampletimes.md) method calls this method. By default, samples are always scheduled for rendering based on their time stamps. The derived class can override this method; for example, to implement quality control.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




