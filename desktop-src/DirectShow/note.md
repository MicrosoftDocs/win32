---
description: The NOTE macro sends a string to the debug output location. Ignored in retail builds.
ms.assetid: 8b85861a-b4d6-4cc6-9ac9-77d06f173869
title: NOTE (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NOTE
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# NOTE

The `NOTE` macro sends a string to the debug output location. Ignored in retail builds.

``` syntax
NOTE(
    pFormat
);

NOTEn(
    pFormat,
    arg1 ... arg5
);
```

## Parameters

<dl> <dt>

<span id="pFormat"></span><span id="pformat"></span><span id="PFORMAT"></span>*pFormat*
</dt> <dd>

A printf -style format string.

</dd> <dt>

<span id="arg1arg5"></span><span id="ARG1ARG5"></span>*arg1*–*arg5*
</dt> <dd>

Additional arguments for the format string. The number of arguments must match the macro name. For example, **NOTE1** takes one argument, and **NOTE5** takes five arguments.

</dd> </dl>

## Remarks

These macros are variants of the [**DbgLog**](dbglog.md) macro. They generate level 5 LOG\_TRACE messages.

## Example


```C++
NOTE("Warning, failed to created graph.");
NOTE2("Width: %d, Height: %d", width, height);
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




