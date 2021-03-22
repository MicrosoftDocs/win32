---
description: The Deliver method delivers a media sample to the connected input pin.
ms.assetid: b871df84-c69e-42eb-9da9-c25996bf08c3
title: CBaseOutputPin.Deliver method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.Deliver
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseOutputPin.Deliver method

The `Deliver` method delivers a media sample to the connected input pin.

## Syntax


```C++
virtual HRESULT Deliver(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                           | Description                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>              |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | Pin is not connected.<br/> |



 

## Remarks

This method calls the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method on the input pin. **Receive** can block if the [**IMemInputPin::ReceiveCanBlock**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivecanblock) method returns S\_OK.

Release the sample after calling this method. The input pin might hold a reference count on the sample, so do not reuse the sample. Always call the [**CBaseOutputPin::GetDeliveryBuffer**](cbaseoutputpin-getdeliverybuffer.md) method to obtain a new sample.

Hold the filter's critical section before calling this method. Otherwise, the pin might get disconnected during the method call. If the filter uses a worker thread to deliver samples, hold the critical section when the filter is ready to deliver a sample. Otherwise, you can hold the critical section in the filter's [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method, where the filter processes samples.

Worker threads can create a potential deadlock. When the thread holds the critical section, it might wait on a state change in the filter. At the same time, the state change might be waiting for the thread to complete. To prevent this, the state-change code should signal an event that terminates the thread, and then wait for the thread to signal completion.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




