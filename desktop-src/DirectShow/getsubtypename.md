---
description: The GetSubtypeName function retrieves the human-readable name of a video subtype.
ms.assetid: 493b434e-2d36-4897-a5b2-7be0eb0a560f
title: GetSubtypeName function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetSubtypeName
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# GetSubtypeName function

The `GetSubtypeName` function retrieves the human-readable name of a video subtype.

## Syntax


```C++
TCHAR* GetSubtypeName(
   const GUID *pSubtype
);
```



## Parameters

<dl> <dt>

*pSubtype* 
</dt> <dd>

Pointer to a video subtype **GUID**.

</dd> </dl>

## Return value

Returns a string containing the name.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




