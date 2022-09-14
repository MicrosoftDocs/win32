---
description: The Active method creates a worker thread that pulls data from the output pin. This method also commits the allocator.
ms.assetid: 9efa20f3-7909-4d87-bfa8-314d055b80f8
title: CPullPin.Active method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.Active
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPullPin.Active method

The **Active** method creates a worker thread that pulls data from the output pin. This method also commits the allocator.

## Syntax


```C++
HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                                   |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | The pin connection was not established correctly.<br/>          |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Could not create the thread, or the thread already exists.<br/> |



 

## Remarks

Call this method when the owning filter becomes active. (If your input pin derives from [**CBasePin**](cbasepin.md), override the [**CBasePin::Active**](cbasepin-active.md) method.)

Before calling this method, call the [**CPullPin::Connect**](cpullpin-connect.md) method to establish the connection with the output pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




