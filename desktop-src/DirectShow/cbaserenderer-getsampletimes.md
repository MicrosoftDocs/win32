---
description: The GetSampleTimes method retrieves the time stamps from a sample.
ms.assetid: a8fead22-a12c-489d-9c42-d5b61f480c25
title: CBaseRenderer.GetSampleTimes method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.GetSampleTimes
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.GetSampleTimes method

The `GetSampleTimes` method retrieves the time stamps from a sample.

## Syntax


```C++
virtual HRESULT GetSampleTimes(
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

Pointer to a variable that receives the start time.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to a variable that receives the end time.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                    | Description                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | The sample should be rendered immediately.<br/>                              |
| <dl> <dt>**S\_FALSE**</dt> </dl>                        | The sample should be scheduled for rendering, based on the time stamps.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                         | Do not render this sample.<br/>                                              |
| <dl> <dt>**VFW\_E\_START\_TIME\_AFTER\_END**</dt> </dl> | Bad time stamp: The end time is earlier than the start time.<br/>            |



 

## Remarks

The filter calls this method to determine how it should handle a sample. If the return value is S\_OK, the filter renders the sample immediately. If the return value is S\_FALSE, the filter schedules the sample for rendering, based on the time stamps. If the return value is an error code, the filter rejects the sample.

This method returns S\_OK if the sample has no time stamps, or if the filter does not have a reference clock. Otherwise, it returns the value of the [**CBaseRenderer::ShouldDrawSampleNow**](cbaserenderer-shoulddrawsamplenow.md) method. In the base class, **ShouldDrawSampleNow** always returns S\_FALSE. The derived class can override this behavior. For example, if the derived class implements quality control management, it might return E\_FAIL to drop a sample.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




