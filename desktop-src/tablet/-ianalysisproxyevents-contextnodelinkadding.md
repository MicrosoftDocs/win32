---
description: Occurs before the ink analyzer adds an IContextLink object between two IContextNode objects.
ms.assetid: ec56cb8e-5154-45ee-911d-e2a240d19dc3
title: '_IAnalysisProxyEvents::ContextNodeLinkAdding event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisProxyEvents.ContextNodeLinkAdding
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisProxyEvents::ContextNodeLinkAdding event

Occurs before the ink analyzer adds an [**IContextLink**](icontextlink.md) object between two [**IContextNode**](icontextnode.md) objects.

## Syntax


```C++
HRESULT ContextNodeLinkAdding(
  [in] IInkAnalyzer *pInkAnalyzer,
  [in] IContextLink *pContextLinkToBeAdded
);
```



## Parameters

<dl> <dt>

*pInkAnalyzer* \[in\]
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) adding the link.

</dd> <dt>

*pContextLinkToBeAdded* \[in\]
</dt> <dd>

The [**IContextLink**](icontextlink.md) object to be added.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this event when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). This event occurs during the reconcile phase of ink analysis, or in response to an ink analyzer method that adds a new [**IContextLink**](icontextlink.md) to an [**IContextNode**](icontextnode.md).

For more information about synchronizing your application data with the [**IInkAnalyzer**](iinkanalyzer.md), see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




