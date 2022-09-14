---
description: Retrieves the maximum byte size needed for the current stream, not including the version number.
ms.assetid: ca1a68e2-02b4-4eea-916a-e0418ae811ae
title: CPersistStream.SizeMax method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.SizeMax
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.SizeMax method

Retrieves the maximum byte size needed for the current stream, not including the version number.

## Syntax


```C++
virtual int SizeMax();
```



## Parameters

This method has no parameters.

## Return value

Returns the number of bytes needed for data, not including the version number.

## Remarks

The default version returns zero; it should be overridden to provide some other appropriate value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




