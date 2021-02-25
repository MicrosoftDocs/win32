---
description: Occurs before the IInkAnalyzer reconciles analysis results so that an application can synchronize data with the IInkAnalyzer.
ms.assetid: 9daa8723-5234-40d9-ac41-6dcca988a8b4
title: '_IAnalysisProxyEvents::InkAnalyzerStateChanging event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisProxyEvents.InkAnalyzerStateChanging
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisProxyEvents::InkAnalyzerStateChanging event

Occurs before the [**IInkAnalyzer**](iinkanalyzer.md) reconciles analysis results so that an application can synchronize data with the **IInkAnalyzer**.

## Syntax


```C++
HRESULT InkAnalyzerStateChanging(
  [in] IInkAnalyzer *pInkAnalyzer
);
```



## Parameters

<dl> <dt>

*pInkAnalyzer* \[in\]
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) that is about to reconcile its analysis results.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this event when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). When the **IInkAnalyzer** raises this event, your application should populate the subnodes of the ink analyzer's root node (see [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md) and [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md)).

The [**IInkAnalyzer**](iinkanalyzer.md) raises this event after it raises the [**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md) event. It raises this event only while performing background analysis.

Lock your data structure when the [**IInkAnalyzer**](iinkanalyzer.md) raises the **\_IAnalysisProxyEvents::InkAnalyzerStateChanging** event. Changes to your data structure during this phase of analysis can cause errors in ink analysis and synchronization. Unlock your data structure when the **IInkAnalyzer** raises the [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) or [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event.

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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




