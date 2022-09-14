---
description: Retrieves the area that has changed since the last analysis operation.
ms.assetid: 0cd62775-59c6-41f5-957e-709a53a8c257
title: IInkAnalyzer::GetDirtyRegion method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetDirtyRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetDirtyRegion method

Retrieves the area that has changed since the last analysis operation.

## Syntax


```C++
HRESULT GetDirtyRegion(
  [out] IAnalysisRegion **ppDirtyRegion
);
```



## Parameters

<dl> <dt>

*ppDirtyRegion* \[out\]
</dt> <dd>

An [**IAnalysisRegion**](ianalysisregion.md) that describes the area that has changed since the last analysis operation.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppDirtyRegion* when you no longer need to use the object.

 

This method identifies the areas that need to be analyzed or reanalyzed. All of the [**IInkAnalyzer**](iinkanalyzer.md) methods that add, update, or remove stroke data update the dirty region. To manually mark an area for reanalysis:

1.  Get the dirty region using **IInkAnalyzer::GetDirtyRegion Method**.
2.  Use [**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md) or [**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md) to add the area to the region from step 1.
3.  Use [**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md) to update the dirty region.

The [**IInkAnalyzer**](iinkanalyzer.md) analyzes ink within its dirty region during a call to [**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md) or [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md). However, the **IInkAnalyzer** may expand the analysis operation to include neighboring regions.

This property may contain nonadjacent areas.

Use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory from the *ppDirtyRegion* array when you are finished with it.

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

[**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStroke Method**](iinkanalyzer-removestroke.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStrokes Method**](iinkanalyzer-removestrokes.md)
</dt> <dt>

[**IInkAnalyzer::UpdateStrokesData Method**](iinkanalyzer-updatestrokesdata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

