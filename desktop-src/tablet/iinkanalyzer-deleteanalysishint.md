---
description: Removes an analysis hint from the IInkAnalyzer.
ms.assetid: ba5498d4-d31c-4b3f-9004-0448e18d4835
title: IInkAnalyzer::DeleteAnalysisHint method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.DeleteAnalysisHint
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::DeleteAnalysisHint method

Removes an analysis hint from the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT DeleteAnalysisHint(
  [in] IContextNode *pHintToDelete
);
```



## Parameters

<dl> <dt>

*pHintToDelete* \[in\]
</dt> <dd>

The analysis hint from the [**IInkAnalyzer**](iinkanalyzer.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Removing an analysis hint does not mark the hint's area for reanalysis. To mark the area within the hint for reanalysis, use [**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md) to set the dirty region to the union of the current dirty region and area of the analysis hint.

The hint is removed from the analyzer; however, the [**IContextNode**](icontextnode.md) itself is not deleted.

This method returns an error code when *pHintToDelete* is a [**IContextNode**](icontextnode.md) that is not of type AnalysisHint (see [**IContextNode::GetType**](icontextnode-gettype.md)).

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

[**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHints Method**](iinkanalyzer-getanalysishints.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHintsByName Method**](iinkanalyzer-getanalysishintsbyname.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




