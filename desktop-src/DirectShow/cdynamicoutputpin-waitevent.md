---
description: The WaitEvent method waits until the specified event is signaled.
ms.assetid: 64880f46-7b8f-4823-9d50-052e30ecf04b
title: CDynamicOutputPin.WaitEvent method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.WaitEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.WaitEvent method

The `WaitEvent` method waits until the specified event is signaled.

## Syntax


```C++
static HRESULT WaitEvent(
   HANDLE hEvent
);
```



## Parameters

<dl> <dt>

*hEvent* 
</dt> <dd>

Handle to an event.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                  | Description                  |
|----------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>          |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected error.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




