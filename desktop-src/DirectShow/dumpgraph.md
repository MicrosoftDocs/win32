---
description: The DumpGraph function sends information about a filter graph to the debug output location. Ignored in retail builds.
ms.assetid: c78f86bb-44d0-4904-b7f8-e756bda0151d
title: DumpGraph function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DumpGraph
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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

Pointer to the [**IFilterGraph**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph) interface on the filter graph manager.

</dd> <dt>

*dwLevel* 
</dt> <dd>

Logging level. The function generates a LOG\_TRACE message with the specified logging level.

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

 

 




