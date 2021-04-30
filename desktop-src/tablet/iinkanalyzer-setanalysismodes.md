---
description: Modifies flags that control how the IInkAnalyzer performs ink analysis.
ms.assetid: cb82edd0-1f15-4313-a286-1fcd715ac6df
title: IInkAnalyzer::SetAnalysisModes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SetAnalysisModes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SetAnalysisModes method

Modifies flags that control how the [**IInkAnalyzer**](iinkanalyzer.md) performs ink analysis.

## Syntax


```C++
HRESULT SetAnalysisModes(
  [in] AnalysisModes analysisMode
);
```



## Parameters

<dl> <dt>

*analysisMode* \[in\]
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

[**IInkAnalyzer::GetAnalysisModes Method**](iinkanalyzer-getanalysismodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




