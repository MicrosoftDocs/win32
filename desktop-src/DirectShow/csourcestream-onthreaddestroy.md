---
description: The OnThreadDestroy method is called when the streaming thread is about to exit.
ms.assetid: a484b6d2-bce6-4a42-9176-2a6ce374e28b
title: CSourceStream.OnThreadDestroy method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.OnThreadDestroy
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.OnThreadDestroy method

The `OnThreadDestroy` method is called when the streaming thread is about to exit.

## Syntax


```C++
virtual HRESULT OnThreadDestroy();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The thread procedure, [**CSourceStream::ThreadProc**](csourcestream-threadproc.md), calls this method before it exits. The method does nothing in the base class; it is available for the derived class to override. If the derived class returns an error code, the thread exits with an error.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




