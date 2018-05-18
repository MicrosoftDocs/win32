---
Description: 'The ChangeMediaType method dynamically changes the media type for the connection.'
ms.assetid: '38efdfdc-f636-4cad-b8d3-8c63a277644e'
title: 'CDynamicOutputPin.ChangeMediaType method'
---

# CDynamicOutputPin.ChangeMediaType method

The `ChangeMediaType` method dynamically changes the media type for the connection. The change can occur while the filter graph is running. Once this method is called, samples with the old media type cannot be delivered. The caller must ensure that no old samples are pending.

## Syntax


```C++
HRESULT ChangeMediaType(
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](am-media-type.md) structure that specifies the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                                                                                                                              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                | Failure. Possibly the owning filter did not call [**CDynamicOutputPin::SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md).<br/> |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The pin is not connected.<br/>                                                                                                     |



 

## Remarks

Call the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method before calling this method.

This method first checks whether the downstream input pin can accept the new format without reconnecting. It queries the input pin for the [**IPinConnection**](ipinconnection.md) interface. If the input pin supports **IPinConnection**, the method calls the [**IPinConnection::DynamicQueryAccept**](ipinconnection-dynamicqueryaccept.md) method with the proposed media type. If the input pin accepts the new media type, the method calls the [**IPin::ReceiveConnection**](ipin-receiveconnection.md) method and renegotiates the allocator requirements.

On the other hand, if the downstream pin does not support **IPinConnection**, or if it rejects the new media type, the method calls the [**CDynamicOutputPin::DynamicReconnect**](cdynamicoutputpin-dynamicreconnect.md) method to perform a dynamic reconnection.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




