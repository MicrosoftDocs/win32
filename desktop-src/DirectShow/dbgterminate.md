---
Description: 'The DbgTerminate function cleans up the debug library. Ignored in retail builds.'
ms.assetid: 'a0e23c57-b4b5-4bcf-8c63-0dee40cc71a7'
title: DbgTerminate function
---

# DbgTerminate function

The **DbgTerminate** function cleans up the debug library. Ignored in retail builds.

## Syntax


```C++
void DbgTerminate(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

Call this function if you call the [**DbgInitialise**](dbginitialise.md) function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




