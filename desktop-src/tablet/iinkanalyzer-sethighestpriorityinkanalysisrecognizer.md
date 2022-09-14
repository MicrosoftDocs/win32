---
description: Moves the specified IInkAnalysisRecognizer to the first position in the IInkAnalyzer object's list of ink recognizers.
ms.assetid: 9126187f-02dd-4988-91b8-c4f3d3b6f773
title: IInkAnalyzer::SetHighestPriorityInkAnalysisRecognizer method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SetHighestPriorityInkAnalysisRecognizer
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SetHighestPriorityInkAnalysisRecognizer method

Moves the specified [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) to the first position in the [**IInkAnalyzer**](iinkanalyzer.md) object's list of ink recognizers.

## Syntax


```C++
HRESULT SetHighestPriorityInkAnalysisRecognizer(
  [in] IInkAnalysisRecognizer *pInkAnalysisRecognizer
);
```



## Parameters

<dl> <dt>

*pInkAnalysisRecognizer* \[in\]
</dt> <dd>

The [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) to place in the first position.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

To get the list of ink recognizers in priority order, call [**IInkAnalyzer::GetInkAnalysisRecognizersByPriority Method**](iinkanalyzer-getinkanalysisrecognizersbypriority.md).

This method does not affect the order of the rest of the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects in the [**IInkAnalyzer**](iinkanalyzer.md) object's list of ink recognizers.

The order of the ink recognizers returned by [**IInkAnalyzer::GetInkAnalysisRecognizersByPriority Method**](iinkanalyzer-getinkanalysisrecognizersbypriority.md) indicates the order in which the [**IInkAnalyzer**](iinkanalyzer.md) evaluates the available [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects.

Use of the ink recognizers is evaluated based on their order in the list.

During ink analysis, the [**IInkAnalyzer**](iinkanalyzer.md) iterates through the ink recognizers in its list until it finds a recognizer that supports the language and other properties of the strokes. This recognizer is used for ink recognition for those strokes.

If the [**IInkAnalyzer**](iinkanalyzer.md) does not find an [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) that supports a set of strokes during analysis, the **IInkAnalyzer** generates an [**IAnalysisWarning**](ianalysiswarning.md) with a warning code of **AnalysisWarningCode\_InkAnalysisRecognizerNotInstalled** (see [**IAnalysisWarning::GetWarningCode**](ianalysiswarning-getwarningcode.md)).

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

[**IInkAnalyzer::GetInkAnalysisRecognizersByPriority Method**](iinkanalyzer-getinkanalysisrecognizersbypriority.md)
</dt> <dt>

[**IInkAnalysisRecognizers**](iinkanalysisrecognizers.md)
</dt> <dt>

[**IAnalysisWarning**](ianalysiswarning.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




