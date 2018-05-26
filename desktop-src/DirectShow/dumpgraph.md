---
Description: The DumpGraph function sends information about a filter graph to the debug output location. Ignored in retail builds.
ms.assetid: c78f86bb-44d0-4904-b7f8-e756bda0151d
title: DumpGraph function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DumpGraph function

The `DumpGraph` function sends information about a filter graph to the debug output location. Ignored in retail builds.

## Syntax


```C++
void DumpGraph(
   IFilterGraph *pGraph,
   DWORD        dwLevel
);
```



## Parameters

<dl> <dt>

*pGraph* 
</dt> <dd>

Pointer to the [**IFilterGraph**](/windows/win32/Strmif/nn-strmif-ifiltergraph?branch=master) interface on the filter graph manager.

</dd> <dt>

*dwLevel* 
</dt> <dd>

Logging level. The function generates a LOG\_TRACE message with the specified logging level.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




