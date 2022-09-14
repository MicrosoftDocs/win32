---
description: Applies the results of a background ink analysis operation to the context node tree for the portions of the tree that have not been modified by the application since the call to IInkAnalyzer::BackgroundAnalyze Method.
ms.assetid: 60e15d4f-6e81-48b9-b7f3-97d2de5c0c1c
title: IInkAnalyzer::Reconcile method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.Reconcile
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::Reconcile method

Applies the results of a background ink analysis operation to the context node tree for the portions of the tree that have not been modified by the application since the call to [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md).

## Syntax


```C++
HRESULT Reconcile();
```



## Parameters

This method has no parameters.

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

By default, the [**IInkAnalyzer**](iinkanalyzer.md) performs an automatic reconciliation phase immediately before raising the [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) and [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) events.

To disable automatic reconciliation, clear the **AnalysisModes\_AutomaticReconciliation** flag from the ink analyzer's analysis modes (see [**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md) and [**AnalysisModes**](analysismodes.md)). The [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md) method returns an error when automatic reconciliation is disabled and your application does not handle the [**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md) event. Your application must call the **IInkAnalyzer::Reconcile Method** method before the [**IInkAnalyzer**](iinkanalyzer.md) can continue to process the results or continue further analysis for the corresponding analysis stage.

Your application can make changes, such as adding or removing strokes and changing stroke data, in the [**IInkAnalyzer**](iinkanalyzer.md) object's context node tree during background analysis. Such changes can invalidate portions of the background analysis results. This method applies analysis results only to the analyzer's context node tree for the portions of the tree that your application has not changed. This method also adds regions containing invalidated analysis results to the **IInkAnalyzer** object's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)).

For more information about using the to analyze ink, see [Ink Analysis Overview](ink-analysis-overview.md).[**AnalysisModes**](analysismodes.md)

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




