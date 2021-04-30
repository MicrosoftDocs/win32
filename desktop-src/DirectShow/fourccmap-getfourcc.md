---
description: Retrieves the FOURCC&\#160;DWORD from the FOURCCMap object.
ms.assetid: bb382a57-8499-44c0-b287-2d31f5f5d1d0
title: FOURCCMap::GetFOURCC method (Fourcc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FOURCCMap.GetFOURCC
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# FOURCCMap::GetFOURCC method

Retrieves the **FOURCC** **DWORD** from the [**FOURCCMap**](fourccmap.md) object.

## Syntax


```C++
DWORD GetFOURCC();
```



## Parameters

This method has no parameters.

## Return value

Returns the **FOURCC** **DWORD** value. Note that if you construct a **GUID** that was not originally derived from a **FOURCC**, the return value will be essentially random.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Fourcc.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**FOURCCMap Class**](fourccmap.md)
</dt> </dl>

 

 




