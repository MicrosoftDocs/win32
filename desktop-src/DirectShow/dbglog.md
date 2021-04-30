---
description: The DbgLog macro sends a string to the debug output location, if logging is enabled for the specified type and level. This macro is ignored in retail builds.
ms.assetid: 10e95d63-14f2-4fdb-a1b8-c5bf654f9819
title: DbgLog macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgLog
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# DbgLog macro

The **DbgLog** macro sends a string to the debug output location, if logging is enabled for the specified type and level. This macro is ignored in retail builds.

## Syntax


```C++
void DbgLog(
         DWORD Types,
         DWORD Level,
   const TCHAR *pFormat,
               ...
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

Logging level for this message.

</dd> <dt>

*pFormat* 
</dt> <dd>

A **printf** -style format string.

</dd> <dt>

*...* 
</dt> <dd>

Additional arguments for the format string.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

If debug logging for any of the message types is set to the specified level or higher, this macro sends the formatted string to the debug output location.

The macro automatically adds a newline character to the output string.

> [!Note]  
> An additional set of parentheses must enclose the macro parameters:

 


```C++
DbgLog((LOG_TRACE, 3, TEXT("Connected input pin %d"), nPinNumber));
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




