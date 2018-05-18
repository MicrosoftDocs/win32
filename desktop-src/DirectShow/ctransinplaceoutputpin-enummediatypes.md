---
Description: 'The EnumMediaTypes method enumerates the pin''s preferred media types. This method implements the IPin::EnumMediaTypes method.'
ms.assetid: '942c6594-3053-484a-a0f7-286dcd3f7550'
title: 'CTransInPlaceOutputPin.EnumMediaTypes method'
---

# CTransInPlaceOutputPin.EnumMediaTypes method

The `EnumMediaTypes` method enumerates the pin's preferred media types. This method implements the [**IPin::EnumMediaTypes**](ipin-enummediatypes.md) method.

## Syntax


```C++
HRESULT EnumMediaTypes(
   IEnumMediaTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* 
</dt> <dd>

Receives a pointer to the [**IEnumMediaTypes**](ienummediatypes.md) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                                         |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>         | Insufficient memory.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>             | **NULL** pointer.<br/>                        |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The filter's input pin is not connected.<br/> |



 

## Remarks

This method returns the **IEnumMediaTypes** interface from the upstream output pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceOutputPin Class**](ctransinplaceoutputpin.md)
</dt> </dl>

 

 




