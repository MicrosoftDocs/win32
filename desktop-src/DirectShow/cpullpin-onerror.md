---
description: The OnError method is called if an error occurs during streaming. The derived class must implement this method.
ms.assetid: 0f135cab-611c-4464-9605-360a30de7eb3
title: CPullPin.OnError method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.OnError
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPullPin.OnError method

The `OnError` method is called if an error occurs during streaming. The derived class must implement this method.

## Syntax


```C++
virtual void OnError(
   HRESULT hr
) = 0;
```



## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

Specifies the **HRESULT** value returned by the method that failed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The object calls this method whenever an error occurs that halts the data-pulling thread. The filter can use this method to recover from streaming errors gracefully. In most cases, the error is returned from the upstream filter, so the upstream filter is responsible for reporting it to the Filter Graph Manager. If the error occurs inside the [**CPullPin::Receive**](cpullpin-receive.md) method, your filter should send an [**EC\_ERRORABORT**](ec-errorabort.md) event. (See [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify).)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




