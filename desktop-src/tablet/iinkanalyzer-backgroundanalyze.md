---
description: Performs asynchronous ink analysis.
ms.assetid: 36427b80-5e3b-4c9a-bb49-e6b7f9301cbd
title: IInkAnalyzer::BackgroundAnalyze method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.BackgroundAnalyze
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::BackgroundAnalyze method

Performs asynchronous ink analysis.

## Syntax


```C++
HRESULT BackgroundAnalyze();
```



## Parameters

This method has no parameters.

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

When this method is called, the [**IInkAnalyzer**](iinkanalyzer.md) performs the ink analysis on a background thread.

This method returns **S\_FALSE** and does not start a new background analysis operation under the following circumstances.

-   The [**IInkAnalyzer**](iinkanalyzer.md) is currently performing background analysis.
-   the dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)) represents an empty area.

The [**IInkAnalyzer**](iinkanalyzer.md) analyzes ink within its dirty region during a call to [**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md) or **IInkAnalyzer::BackgroundAnalyze Method**. However, the **IInkAnalyzer** may expand the analysis operation to include neighboring regions.

This method sets the dirty region to an empty region.

If stroke data was added to the [**IInkAnalyzer**](iinkanalyzer.md) after the call to **IInkAnalyzer::BackgroundAnalyze Method**, the **IInkAnalyzer** may update the dirty region during the reconcile phase of ink analysis.

The analysis modes setting (see [**IInkAnalyzer::GetAnalysisModes Method**](iinkanalyzer-getanalysismodes.md)) specifies how the [**IInkAnalyzer**](iinkanalyzer.md) performs background analysis. For more information about ink analysis, see [Ink Analysis Overview](ink-analysis-overview.md).

This method returns an error code under the following circumstances.

-   Your application has set [**AnalysisModes**](analysismodes.md) value **AnalysisModes\_IntermediateResults** in the [**IInkAnalyzer**](iinkanalyzer.md) (see [**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md)) and does not handle the [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) event.
-   Your application has cleared [**AnalysisModes**](analysismodes.md) value **AnalysisModes\_AutomaticReconciliation** in the [**IInkAnalyzer**](iinkanalyzer.md) (see [**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md)) and does not handle the [**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md) event.
-   Your application does not handle the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event.
-   Your application does not handle the [**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md) event.

## Examples

The following example checks the ink analyzer's dirty region, and then initiates background ink analysis if the dirty region is not empty.


```C++
// Check that the ink analyzer's dirty region is not empty.
IAnalysisRegion *pDirtyRegion;
hr = this->m_spIInkAnalyzer->GetDirtyRegion(&pDirtyRegion);

if (SUCCEEDED(hr))
{
    VARIANT_BOOL bIsEmpty;
    hr = pDirtyRegion->IsEmpty(&bIsEmpty);

    if (SUCCEEDED(hr))
    {
        if (!bIsEmpty)
        {
            // Insert code that prepares the application for background
            // ink analysis here.

            // Start background ink analysis. The _IAnalysisEvents::Results
            // event signals when background ink analysis is complete.
            hr = this->m_spIInkAnalyzer->BackgroundAnalyze();
        }
    }
}

// Free the memory for the dirty region.
if (pDirtyRegion != NULL)
{
    pDirtyRegion->Release();
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

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisModes Method**](iinkanalyzer-getanalysismodes.md)
</dt> <dt>

[**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md)
</dt> <dt>

[**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)
</dt> <dt>

[**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md)
</dt> <dt>

[**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




