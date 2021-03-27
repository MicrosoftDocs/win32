---
description: Loads the filter's data from a given stream.
ms.assetid: c2bfd379-2916-4698-bc41-653161723706
title: CPersistStream.Load method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.Load
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.Load method

Loads the filter's data from a given stream.

## Syntax


```C++
HRESULT Load(
   LPSTREAM pStm
);
```



## Parameters

<dl> <dt>

*pStm* 
</dt> <dd>

Pointer to the stream from which to be loaded.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the **IPersistStream::Load** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




