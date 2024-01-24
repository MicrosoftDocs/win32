---
description: Retrieves flags that control how the IInkAnalyzer performs ink analysis.
ms.assetid: 982cb9cd-2d73-4064-9a6e-fe123adf0fb6
title: IInkAnalyzer::GetAnalysisModes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetAnalysisModes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetAnalysisModes method

Retrieves flags that control how the [**IInkAnalyzer**](iinkanalyzer.md) performs ink analysis.

## Syntax


```C++
HRESULT GetAnalysisModes(
  [out] AnalysisModes *pAnalysisMode
);
```



## Parameters

<dl> <dt>

*pAnalysisMode* \[out\]
</dt> <dd>

A bitwise combination of the [**AnalysisModes**](analysismodes.md) enumeration values.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

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

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




