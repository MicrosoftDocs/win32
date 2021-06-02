---
description: The DbgCheckModuleLevel function checks whether logging is enabled for the given message types and level. Ignored in retail builds.
ms.assetid: f4b12df7-9001-4bfb-9d84-84a0e8295a8b
title: DbgCheckModuleLevel function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgCheckModuleLevel
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DbgCheckModuleLevel function

The `DbgCheckModuleLevel` function checks whether logging is enabled for the given message types and level. Ignored in retail builds.

## Syntax


```C++
BOOL DbgCheckModuleLevel(
   DWORD Types,
   DWORD Level
);
```



## Parameters

<dl> <dt>

*Types* 
</dt> <dd>

Bitwise combination of one or more message types.

</dd> <dt>

*Level* 
</dt> <dd>

Logging level

</dd> </dl>

## Return value

Returns **TRUE** if logging for any of the specified message types is set to the specified level or higher. Otherwise, returns **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




