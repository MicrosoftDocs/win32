---
Description: 'The GetDeliveryBuffer method retrieves a media sample that contains an empty buffer.'
ms.assetid: '5a20c11b-50f8-443e-a4d5-6bcffde741d5'
title: 'CBaseOutputPin.GetDeliveryBuffer method'
---

# CBaseOutputPin.GetDeliveryBuffer method

The `GetDeliveryBuffer` method retrieves a media sample that contains an empty buffer.

## Syntax


```C++
virtual HRESULT GetDeliveryBuffer(
   IMediaSample   **ppSample,
   REFERENCE_TIME *pStartTime,
   REFERENCE_TIME *pEndTime,
   DWORD          dwFlags
);
```



## Parameters

<dl> <dt>

*ppSample* 
</dt> <dd>

Address of a variable that receives a pointer to the buffer's [**IMediaSample**](imediasample.md) interface.

</dd> <dt>

*pStartTime* 
</dt> <dd>

Pointer to the start time of the sample, or **NULL**.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to the ending time of the sample, or **NULL**.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Bitwise combination of flags supported by the [**IMemAllocator::GetBuffer**](imemallocator-getbuffer.md) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                   | Description                        |
|-----------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | No allocator available.<br/> |



 

## Remarks

This method calls the **IMemAllocator::GetBuffer** method on the allocator, and passes the parameters to that method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




