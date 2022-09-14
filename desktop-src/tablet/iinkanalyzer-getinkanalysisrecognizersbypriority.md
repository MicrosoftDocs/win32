---
description: Retrieves an ordered collection of IInkAnalysisRecognizer objects.
ms.assetid: 67399237-38e2-4905-a97c-10ca72c7799b
title: IInkAnalyzer::GetInkAnalysisRecognizersByPriority method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetInkAnalysisRecognizersByPriority
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetInkAnalysisRecognizersByPriority method

Retrieves an ordered collection of [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects.

## Syntax


```C++
HRESULT GetInkAnalysisRecognizersByPriority(
  [out] IInkAnalysisRecognizers **ppInkAnalysisRecognizers
);
```



## Parameters

<dl> <dt>

*ppInkAnalysisRecognizers* \[out\]
</dt> <dd>

An ordered collection of [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppInkAnalysisRecognizers* when you no longer need to use the object.

 

The order of the recognizers in this collection indicates the order in which the [**IInkAnalyzer**](iinkanalyzer.md) evaluates the available recognizers. The **IInkAnalyzer** uses the language of the strokes as its primary criterion for applying an [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md). As a secondary criterion, the **IInkAnalyzer** compares analysis hint information against an **IInkAnalysisRecognizer** object's supported capabilities (see [**IInkAnalysisRecognizer::GetCapabilities**](iinkanalysisrecognizer-getcapabilities.md)). For more information about analysis hints, see [**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md).

If more than one [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) supports a language identifier, the [**IInkAnalyzer**](iinkanalyzer.md) uses a "first-fit" algorithm to select the first **IInkAnalysisRecognizer** to analyze strokes of that language.

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

[**IInkAnalysisRecognizers**](iinkanalysisrecognizers.md)
</dt> <dt>

[**IInkAnalyzer::SetHighestPriorityInkAnalysisRecognizer Method**](iinkanalyzer-sethighestpriorityinkanalysisrecognizer.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

