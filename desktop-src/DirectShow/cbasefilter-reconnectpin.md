---
Description: 'The ReconnectPin method breaks an existing pin connection and reconnects it to the same pin, using a specified media type.'
ms.assetid: '9e2dea49-a2bd-4abd-b896-54b13b2271bb'
title: 'CBaseFilter.ReconnectPin method'
---

# CBaseFilter.ReconnectPin method

The `ReconnectPin` method breaks an existing pin connection and reconnects it to the same pin, using a specified media type.

## Syntax


```C++
HRESULT ReconnectPin(
   IPin                *pPin,
   AM_MEDIA_TYPE const *pmt
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the pin's [**IPin**](ipin.md) interface.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](am-media-type.md) structure that specifies the media type, or **NULL**.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                   | Description                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                                               |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | [**m\_pGraph**](cbasefilter-m-pgraph.md) member variable is **NULL**.<br/> |



 

## Remarks

This method calls the [**IFilterGraph2::ReconnectEx**](ifiltergraph2-reconnectex.md) method on the filter graph manager. If the [**IFilterGraph2**](ifiltergraph2.md) interface is not available, the method calls [**IFilterGraph::Reconnect**](ifiltergraph-reconnect.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




