---
Description: 'The OnThreadCreate method is called when the streaming thread is initialized.'
ms.assetid: 'eeaa0d12-3185-4c97-b481-fc420cfc0897'
title: 'CSourceStream.OnThreadCreate method'
---

# CSourceStream.OnThreadCreate method

The `OnThreadCreate` method is called when the streaming thread is initialized.

## Syntax


```C++
virtual HRESULT OnThreadCreate();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The thread procedure, [**CSourceStream::ThreadProc**](csourcestream-threadproc.md), calls this method when it first receives a [**CSourceStream::Init**](csourcestream-init.md) request. The method does nothing in the base class. The derived class can override this method to perform thread initializations. If the derived class returns an error code, the thread exits with an error.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




