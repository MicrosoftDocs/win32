---
description: Changes the dirty flag for the current stream.
ms.assetid: 65fa7fbe-4fa7-45a3-91a4-4a3547b035b9
title: CPersistStream.SetDirty method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.SetDirty
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.SetDirty method

Changes the dirty flag for the current stream.

## Syntax


```C++
HRESULT SetDirty(
   BOOL fDirty
);
```



## Parameters

<dl> <dt>

*fDirty* 
</dt> <dd>

New dirty flag for this stream. **TRUE** means that the data has not been saved.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




