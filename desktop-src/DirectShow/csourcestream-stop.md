---
Description: 'The Stop method signals the streaming thread to stop.'
ms.assetid: '79bc528a-cf53-43f3-aa17-c459063c99ab'
title: 'CSourceStream.Stop method'
---

# CSourceStream.Stop method

The `Stop` method signals the streaming thread to stop.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or E\_UNEXPECTED.

## Remarks

The [**CSourceStream::Inactive**](csourcestream-inactive.md) method calls this method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




