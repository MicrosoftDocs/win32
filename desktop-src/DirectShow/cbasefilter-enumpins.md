---
Description: The EnumPins method enumerates the pins on this filter. This method implements the IBaseFilterEnumPins method.
ms.assetid: c1015ed3-658f-4f96-a1fb-e04b81a9ddb5
title: CBaseFilter.EnumPins method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseFilter.EnumPins method

The `EnumPins` method enumerates the pins on this filter. This method implements the [**IBaseFilter::EnumPins**](/windows/win32/Strmif/nf-strmif-ibasefilter-enumpins?branch=master) method.

## Syntax


```C++
HRESULT EnumPins(
   IEnumPins **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* 
</dt> <dd>

Address of a variable that receives a pointer to the [**IEnumPins**](/windows/win32/Strmif/nn-strmif-ienumpins?branch=master) interface.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                   | Description                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument<br/> |



 

## Remarks

This method creates an instance of the [**CEnumPins**](cenumpins.md) base class, and returns a pointer to that object, of type **IEnumPins**. The **CEnumPins** class calls the filter's [**CBaseFilter::GetPin**](cbasefilter-getpin.md) method to enumerate the pins on the filter.

If this method succeeds, the **IEnumPins** interface has an outstanding reference count. The caller must release the interface.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




