---
description: The EOS method updates the cached time stamps after an end-of-stream notification.
ms.assetid: 7fb2f964-ec15-47f5-902b-29b9b121e876
title: CRendererPosPassThru.EOS method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererPosPassThru.EOS
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererPosPassThru.EOS method

The `EOS` method updates the cached time stamps after an end-of-stream notification.

## Syntax


```C++
HRESULT EOS();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                            | Description                                               |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failure. Possibly the filter is not streaming.<br/> |



 

## Remarks

The filter should call this method when it receives an end-of-stream notification ([**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream)). The method sets both cached time stamps equal to the stop position, ensuring that the [**IMediaSeeking:: GetCurrentPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getcurrentposition) method returns the correct values at the end of the stream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




