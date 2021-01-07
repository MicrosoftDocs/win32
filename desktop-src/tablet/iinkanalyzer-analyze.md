---
description: Performs synchronous ink analysis.
ms.assetid: 957845f3-96b4-4184-aaec-e266cbe47e46
title: IInkAnalyzer::Analyze method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.Analyze
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::Analyze method

Performs synchronous ink analysis.

## Syntax


```C++
HRESULT Analyze(
  [out] IAnalysisStatus **ppStatus
);
```



## Parameters

<dl> <dt>

*ppStatus* \[out\]
</dt> <dd>

A pointer to an [**IAnalysisStatus**](ianalysisstatus.md) that describes the status of the analysis operation.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppStatus* when you no longer need to use the analysis status.

 

This method starts a synchronous ink analysis operation. Ink analysis includes layout analysis, writing and drawing classification, and handwriting recognition. This method returns after the analysis operation is complete.

This method returns **E\_POINTER** if *ppStatus* is **NULL**.

During a call to **IInkAnalyzer::Analyze Method** or [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md), the [**IInkAnalyzer**](iinkanalyzer.md) analyzes ink within its dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)). However, the **IInkAnalyzer** may expand the analysis operation to include neighboring regions.

This method sets the [**IInkAnalyzer**](iinkanalyzer.md) object's dirty region to an empty region. If another thread has added stroke data that has not been analyzed, the **IInkAnalyzer** adds the bounding box of the unanalyzed strokes to its dirty region during the reconcile phase of the analysis.

This method returns an error if your application does not handle the [**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md) event.

The [**IInkAnalyzer**](iinkanalyzer.md) does not raise the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) and [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) events in response to this method.

To modify the way ink analysis is performed, use [**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md).

For more information about ink analysis, see [Ink Analysis Overview](ink-analysis-overview.md).

## Examples

The following example performs foreground ink analysis.


```C++
// Perform synchronous ink analysis.
IAnalysisStatus *pAnalysisStatus = NULL;
hr = this->m_spIInkAnalyzer->Analyze(&pAnalysisStatus);

if (SUCCEEDED(hr))
{
    // Insert code that processes the analysis results.
}

// Release this reference to the analysis status.
if (pAnalysisStatus != NULL)
{
    pAnalysisStatus->Release();
    pAnalysisStatus = NULL;
}
```



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

[**AnalysisModes**](analysismodes.md)
</dt> <dt>

[**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)
</dt> <dt>

[**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md)
</dt> <dt>

[**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> </dl>

 

