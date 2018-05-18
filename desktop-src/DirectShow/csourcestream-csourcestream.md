---
Description: 'Constructor method.'
ms.assetid: '9078b2f5-b11e-4780-8143-6738e9df4f4b'
title: 'CSourceStream.CSourceStream constructor'
---

# CSourceStream.CSourceStream constructor

Constructor method.

## Syntax


```C++
CSourceStream(
   TCHAR   *pObjectName,
   HRESULT *phr,
   CSource *pms,
   LPCWSTR pName
);
```



## Parameters

<dl> <dt>

*pObjectName* 
</dt> <dd>

Pointer to a string containing the debug name of the pin.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value indicating the success or failure of the method. Initialize the value to S\_OK before creating the object. The value is changed only if an error occurs.

</dd> <dt>

*pms* 
</dt> <dd>

Pointer to the [**CSource**](csource.md) filter that created this pin.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to a string that contains the name of the pin.

</dd> </dl>

## Remarks

The string given in the *pObjectName* parameter is used only for debugging purposes. For more information, see [**CBaseObject**](cbaseobject.md).

The string given in the *pName* parameter is the name returned by the [**IPin::QueryPinInfo**](ipin-querypininfo.md) method. The `CSourceStream` class does not use this name for the pin identifier returned by the [**CSourceStream::QueryId**](csourcestream-queryid.md) method. Instead, **QueryId** calculates a pin identifier based on the pin number. (Pin identifiers support graph persistence. For more information, see [**IPin::QueryId**](ipin-queryid.md).)

The constructor automatically adds the pin to the owning filter, by calling [**CSource::AddPin**](csource-addpin.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




