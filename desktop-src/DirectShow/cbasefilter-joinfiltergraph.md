---
description: The JoinFilterGraph method notifies the filter that it has joined or left a filter graph. This method implements the IBaseFilter::JoinFilterGraph method.
ms.assetid: ee02650c-aaf0-4a0e-914f-180230010709
title: CBaseFilter.JoinFilterGraph method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.JoinFilterGraph
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.JoinFilterGraph method

The `JoinFilterGraph` method notifies the filter that it has joined or left a filter graph. This method implements the [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method.

## Syntax


```C++
HRESULT JoinFilterGraph(
       IFilterGraph *pGraph,
  [in] LPCWSTR      pName
);
```



## Parameters

<dl> <dt>

*pGraph* 
</dt> <dd>

Pointer to the filter graph manager's [**IFilterGraph**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph) interface, or **NULL** if the filter is leaving the graph.

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to a Unicode string containing a name for the filter.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CBaseFilter::m\_pGraph**](cbasefilter-m-pgraph.md) member variable equal to the *pGraph* parameter. It also queries for an [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink) interface pointer and stores it in the [**CBaseFilter::m\_pSink**](cbasefilter-m-psink.md) member variable. However, the filter does not keep a reference count on either of these interfaces. Doing so would create a circular reference count, because the filter graph manager keeps a reference count on the filter.

The method copies the string specified by *pName* into the [**CBaseFilter::m\_pName**](cbasefilter-m-pname.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




