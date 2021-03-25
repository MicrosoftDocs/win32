---
description: Indicates whether the object has changed since it was last saved to its current stream.
ms.assetid: 69840be6-062e-4505-8381-ea04e822c660
title: CPersistStream.IsDirty method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.IsDirty
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.IsDirty method

Indicates whether the object has changed since it was last saved to its current stream.

## Syntax


```C++
HRESULT IsDirty();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the filter needs saving and S\_FALSE if it does not need saving.

## Remarks

This member function implements the **IPersistStream::IsDirty** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




