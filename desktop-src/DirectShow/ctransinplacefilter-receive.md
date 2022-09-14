---
description: The Receive method receives a media sample, processes it, and delivers it to the downstream filter.
ms.assetid: 87126353-b73a-45f5-a8e7-b719efdf9d76
title: CTransInPlaceFilter.Receive method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.Receive method

The `Receive` method receives a media sample, processes it, and delivers it to the downstream filter.

## Syntax


```C++
HRESULT Receive(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface on the sample.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                  | Description                 |
|----------------------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success<br/>          |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected error<br/> |



 

## Remarks

The filter's input pin calls this method when it receives a sample. The filter calls the [**Transform**](ctransinplacefilter-transform.md) method, which the derived class must implement. The **Transform** method processes the data. If the filter is using only one allocator, it passes *pSample* directly to the **Transform** method. Otherwise, it copies *pSample* and passes the copy.

If the **Transform** method returns S\_FALSE, the `Receive` method drops the sample. On the first dropped sample, the filter sends an [**EC\_QUALITY\_CHANGE**](ec-quality-change.md) event to the filter graph manager. Otherwise, if the **Transform** method returns S\_OK, the filter delivers the output sample. To do so, it calls the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method on the downstream input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




