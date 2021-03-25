---
description: The RemovePin method removes a specified pin from the filter. The method does not delete the pin.
ms.assetid: 104eccfa-3fff-4f47-ba1b-3206eab9eef8
title: CSource.RemovePin method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSource.RemovePin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSource.RemovePin method

The `RemovePin` method removes a specified pin from the filter. The method does not delete the pin.

## Syntax


```C++
HRESULT RemovePin(
   CSourceStream *pStream
);
```



## Parameters

<dl> <dt>

*pStream* 
</dt> <dd>

Pointer to the [**CSourceStream**](csourcestream.md) object that implements the pin.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                                      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                              |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The filter does not contain this pin.<br/> |



 

## Remarks

The destructor method calls this method, to remove the output pin from the filter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




