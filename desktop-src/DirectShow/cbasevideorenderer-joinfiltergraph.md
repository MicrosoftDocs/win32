---
description: The JoinFilterGraph method sends EC\_WINDOW\_DESTROYED event notification when a filter is removed from the filter graph.
ms.assetid: b54d2deb-d36f-43a9-aa00-d607f487d8b7
title: CBaseVideoRenderer.JoinFilterGraph method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.JoinFilterGraph
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.JoinFilterGraph method

The `JoinFilterGraph` method sends [**EC\_WINDOW\_DESTROYED**](ec-window-destroyed.md) event notification when a filter is removed from the filter graph.

## Syntax


```C++
HRESULT JoinFilterGraph(
       IBaseFilterGraph *pGraph,
  [in] LPCWSTR          pName
);
```



## Parameters

<dl> <dt>

*pGraph* 
</dt> <dd>

Pointer to the filter graph to join.

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to the name of the filter being added.

</dd> </dl>

## Return value

No return value.

## Remarks

This member function overrides the [**CBaseFilter::JoinFilterGraph**](cbasefilter-joinfiltergraph.md) member function. If the filter is leaving the filter graph (*pGraph* is **NULL**), it sends an [**EC\_WINDOW\_DESTROYED**](ec-window-destroyed.md) event notification so that the resource manager does not hold on to the renderer as a focus object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




