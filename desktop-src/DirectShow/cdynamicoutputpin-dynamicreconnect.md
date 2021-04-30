---
description: The DynamicReconnect method performs a dynamic reconnection with a new media type. The reconnection can occur while the filter graph is running.
ms.assetid: 1fe9f1cc-1f5d-407e-8c80-fea6cd1cb16f
title: CDynamicOutputPin.DynamicReconnect method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.DynamicReconnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.DynamicReconnect method

The `DynamicReconnect` method performs a dynamic reconnection with a new media type. The reconnection can occur while the filter graph is running.

## Syntax


```C++
HRESULT DynamicReconnect(
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that specifies the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                            | Description                                                                                                                                         |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                                                                                                                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failure. Possibly the owning filter did not call the [**CDynamicOutputPin::SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md) method.<br/> |



 

## Remarks

This method must be called from the same thread that delivers data to the pin. Once this method is called, samples with the old media type cannot be delivered. The caller must ensure that no old samples are pending.

Call [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) before calling this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




