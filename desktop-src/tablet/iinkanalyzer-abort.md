---
description: Cancels the current analysis operation.
ms.assetid: 909bfa66-b6df-4730-95b7-809fc2170e85
title: IInkAnalyzer::Abort method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.Abort
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::Abort method

Cancels the current analysis operation.

## Syntax


```C++
HRESULT Abort(
  [out] IAnalysisRegion **ppAbortedRegion
);
```



## Parameters

<dl> <dt>

*ppAbortedRegion* \[out\]
</dt> <dd>

A pointer to an [**IAnalysisRegion**](ianalysisregion.md) that represents the dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)) of the current analysis operation.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppAbortedRegion* when you no longer need to use the object.

This method cancels the current analysis operation.

When *ppAbortedRegion* is **NULL**, this method performs the abort as normal, because this indicates that the caller has no interest in the return value.

**IInkAnalyzer::Abort Method** silences the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) and [**\_IAnalysisEvents::Activity**](-ianalysisevents-activity.md) events for the current analysis operation.

**IInkAnalyzer::Abort Method** runs asynchronously until the current background analysis operation is canceled. Because the cancellation process is asynchronous, the application can perform other tasks while the current analysis opertions is canceled.

If no analysis operations are in progress, this method returns an empty analysis region.

If one analysis operation is in progress, this method cancels the operation.

If both synchronous and asynchronous analysis operations are in progress, this method cancels the synchronous operation.

If this method is called more than once for the same analysis operation, the first call returns the dirty region for the operation, and the subsequent calls return an empty region.

If your application maintains its own data structure that is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md), calling **IInkAnalyzer::Abort Method** can leave your document with partial results. To avoid this, do not call **IInkAnalyzer::Abort Method** between the time the **IInkAnalyzer** receives the [**\_IAnalysisProxyEvents::InkAnalyzerStateChanging**](-ianalysisproxyevents-inkanalyzerstatechanging.md) event and the time the **IInkAnalyzer** receives the [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) or [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event.

For more information about synchronizing your application data with the ink analyzer, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

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

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)
</dt> <dt>

[**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

