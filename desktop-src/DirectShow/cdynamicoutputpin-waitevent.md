---
Description: The WaitEvent method waits until the specified event is signaled.
ms.assetid: 64880f46-7b8f-4823-9d50-052e30ecf04b
title: CDynamicOutputPin.WaitEvent method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




