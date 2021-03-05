---
description: Occurs after the IInkAnalyzer updates one or more properties of an IContextNode object.
ms.assetid: f626c263-31a4-45ee-ae04-3251eac0d652
title: '_IAnalysisProxyEvents::ContextNodePropertiesUpdated event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisProxyEvents.ContextNodePropertiesUpdated
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisProxyEvents::ContextNodePropertiesUpdated event

Occurs after the [**IInkAnalyzer**](iinkanalyzer.md) updates one or more properties of an [**IContextNode**](icontextnode.md) object.

## Syntax


```C++
HRESULT ContextNodePropertiesUpdated(
  [in] IInkAnalyzer *pInkAnalyzer,
  [in] IContextNode *pContextNodeUpdated
);
```



## Parameters

<dl> <dt>

*pInkAnalyzer* \[in\]
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) object updating the properties.

</dd> <dt>

*pContextNodeUpdated* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object whose properties are updated.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this event when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). This event occurs during the reconcile phase of ink analysis, or in response to an ink analyzer method that changes the properties of an [**IContextNode**](icontextnode.md) (see [**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)).

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

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Context Node Properties](context-node-properties.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




