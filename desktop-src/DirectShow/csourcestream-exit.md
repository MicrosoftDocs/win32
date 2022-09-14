---
description: The Exit method signals the streaming thread to exit.
ms.assetid: 1bb59848-e405-40f9-87ec-33de8754e2dd
title: CSourceStream.Exit method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.Exit
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.Exit method

The `Exit` method signals the streaming thread to exit.

## Syntax


```C++
HRESULT Exit();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or E\_UNEXPECTED.

## Remarks

The [**CSourceStream::Inactive**](csourcestream-inactive.md) method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




