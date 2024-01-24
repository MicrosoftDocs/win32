---
description: Retrieves the analysis hint that caused this warning.
ms.assetid: 715aa4b2-6c45-414b-96f2-44c73a073213
title: IAnalysisWarning::GetHint method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisWarning.GetHint
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisWarning::GetHint method

Retrieves the analysis hint that caused this warning.

## Syntax


```C++
HRESULT GetHint(
  [out] IContextNode **pAnalysisHint
);
```



## Parameters

<dl> <dt>

*pAnalysisHint* \[out\]
</dt> <dd>

The analysis hint context node that caused this warning, or **NULL** if an analysis hint did not cause this warning.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**pAnalysisHint* when you no longer need to use the analysis hint context node.

 

An example of an analysis hint that generates an [**IAnalysisWarning**](ianalysiswarning.md) is an analysis hint that contains an incorrectly spelled factoid. In this case, ink analysis returns an [**IAnalysisStatus**](ianalysisstatus.md) that contains an **IAnalysisWarning** that references the analysis hint context node with the misspelled factoid. Also, in this case, the analysis warning's [**IAnalysisWarning::GetWarningCode**](ianalysiswarning-getwarningcode.md) method returns an [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode) value of **AnalysisWarningCode\_FactoidNotSupported**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisWarning**](ianalysiswarning.md)
</dt> <dt>

[**IAnalysisStatus**](ianalysisstatus.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

