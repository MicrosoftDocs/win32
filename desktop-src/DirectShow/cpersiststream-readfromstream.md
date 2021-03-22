---
description: Reads the filter's data from the given stream.
ms.assetid: 009f4812-8cc6-436a-9553-3a3161d5e992
title: CPersistStream.ReadFromStream method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.ReadFromStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.ReadFromStream method

Reads the filter's data from the given stream.

## Syntax


```C++
virtual HRESULT ReadFromStream(
   IStream *pStream
);
```



## Parameters

<dl> <dt>

*pStream* 
</dt> <dd>

Pointer to an **IStream** interface from which data is to be read.

</dd> </dl>

## Return value

Returns S\_OK. The derived class should return a valid **HRESULT** value.

## Remarks

The default version reads nothing; it can be overridden to read data specific to your class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




