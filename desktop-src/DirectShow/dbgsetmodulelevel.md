---
description: The DbgSetModuleLevel function sets the logging level for one or more message types. Ignored in retail builds.
ms.assetid: 89d25106-8018-4089-8b77-d3c87529e984
title: DbgSetModuleLevel function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgSetModuleLevel
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DbgSetModuleLevel function

The **DbgSetModuleLevel** function sets the logging level for one or more message types. Ignored in retail builds.

## Syntax


```C++
void DbgSetModuleLevel(
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

Logging level for the specified message types.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




