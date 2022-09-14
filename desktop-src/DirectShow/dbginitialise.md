---
description: The DbgInitialise function initializes the debug library. Ignored in retail builds.
ms.assetid: d4ca739e-cd39-4692-81da-c5a88a09d546
title: DbgInitialise function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgInitialise
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DbgInitialise function

The **DbgInitialise** function initializes the debug library. Ignored in retail builds.

## Syntax


```C++
void DbgInitialise(
   HINSTANCE hInst
);
```



## Parameters

<dl> <dt>

*hInst* 
</dt> <dd>

Handle to the module instance.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

In an executable, call this method before using the DirectShow debug facilities. Before the executable quits, call the [**DbgTerminate**](dbgterminate.md) function to clean up the debug library.

In a DLL that links to the base-class library (Strmbase.lib), it is not necessary to call this function. The function is called automatically when the DLL is loaded.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




