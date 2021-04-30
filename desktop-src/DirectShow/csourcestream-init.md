---
description: The Init method initializes the streaming thread.
ms.assetid: c746e595-de97-478c-8b22-5c4dd5594a8f
title: CSourceStream.Init method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.Init
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.Init method

The `Init` method initializes the streaming thread.

## Syntax


```C++
HRESULT Init();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK, or another **HRESULT** value.

## Remarks

This method must be the first thread request sent to the [**CSourceStream::ThreadProc**](csourcestream-threadproc.md) method. The [**CSourceStream::Active**](csourcestream-active.md) method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




