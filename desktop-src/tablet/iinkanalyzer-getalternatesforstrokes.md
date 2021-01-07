---
description: Retrieves analysis alternates for the strokes with the specified stroke identifiers.
ms.assetid: e8bc198e-de0b-49b7-9120-4298985dfe64
title: IInkAnalyzer::GetAlternatesForStrokes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetAlternatesForStrokes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetAlternatesForStrokes method

Retrieves analysis alternates for the strokes with the specified stroke identifiers.

## Syntax


```C++
HRESULT GetAlternatesForStrokes(
  [in]  ULONG              ulStrokeIdsCount,
  [in]  LONG               *plStrokes,
  [in]  ULONG              ulMaximumAlternates,
  [out] AnalysisAlternates **ppAlternates
);
```



## Parameters

<dl> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of stroke identifiers in *plStrokes*.

</dd> <dt>

*plStrokes* \[in\]
</dt> <dd>

The array of stroke identifiers.

</dd> <dt>

*ulMaximumAlternates* \[in\]
</dt> <dd>

The maximum number of analysis alternatives returned.

</dd> <dt>

*ppAlternates* \[out\]
</dt> <dd>

The [**IAnalysisAlternates**](ianalysisalternates.md) object containing the analysis alternatives.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppAlternates* when you no longer need to use the object.

 

The top [**IAnalysisAlternate**](ianalysisalternate.md) is returned as the first alternate of the collection.

The specified strokes do not have to represent adjacent areas of the document.

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

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IAnalysisAlternates**](ianalysisalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md)
</dt> <dt>

[**IInkAnalyzer::ModifyTopAlternate Method**](iinkanalyzer-modifytopalternate.md)
</dt> <dt>

[**IInkAnalyzer::ModifyTopAlternateWithConfirmation Method**](iinkanalyzer-modifytopalternatewithconfirmation.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

