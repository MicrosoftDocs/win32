---
description: Pointer to an AMOVIESETUP\_FILTER structure.
ms.assetid: 72db601b-78a3-484a-a27f-147ec36022ab
title: CFactoryTemplate::m_pAMovieSetup_Filter member (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_pAMovieSetup_Filter
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CFactoryTemplate::m\_pAMovieSetup\_Filter member

Pointer to an [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure.

## Syntax


```C++
const AMOVIESETUP_FILTER *m_pAMovieSetup_Filter;
```



## Remarks

Use this structure to make a filter self-registering. If your component is not a filter, this member variable can be **NULL**. For more information, see How to Register DirectShow Filters.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




