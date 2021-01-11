---
description: Indicates the level of confidence that the IInkAnalyzer has in the accuracy of the recognition result.
ms.assetid: 'fd4fc350-b4db-4f9a-a5ae-00065e33606c'
title: RecognitionConfidence enumeration (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RecognitionConfidence
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# RecognitionConfidence enumeration

Indicates the level of confidence that the [**IInkAnalyzer**](iinkanalyzer.md) has in the accuracy of the recognition result.

## Syntax


```C++
typedef enum RecognitionConfidence { 
  RecognitionConfidence_Strong        = 0,
  RecognitionConfidence_Intermediate  = 1,
  RecognitionConfidence_Poor          = 2,
  RecognitionConfidence_Unknown       = 3
} RecognitionConfidence;
```



## Constants

<dl> <dt>

<span id="RecognitionConfidence_Strong"></span><span id="recognitionconfidence_strong"></span><span id="RECOGNITIONCONFIDENCE_STRONG"></span>**RecognitionConfidence\_Strong**
</dt> <dd>

Strong confidence in the result or alternate.

</dd> <dt>

<span id="RecognitionConfidence_Intermediate"></span><span id="recognitionconfidence_intermediate"></span><span id="RECOGNITIONCONFIDENCE_INTERMEDIATE"></span>**RecognitionConfidence\_Intermediate**
</dt> <dd>

Intermediate confidence in the result or alternate.

</dd> <dt>

<span id="RecognitionConfidence_Poor"></span><span id="recognitionconfidence_poor"></span><span id="RECOGNITIONCONFIDENCE_POOR"></span>**RecognitionConfidence\_Poor**
</dt> <dd>

Poor confidence in the result or alternate.

</dd> <dt>

<span id="RecognitionConfidence_Unknown"></span><span id="recognitionconfidence_unknown"></span><span id="RECOGNITIONCONFIDENCE_UNKNOWN"></span>**RecognitionConfidence\_Unknown**
</dt> <dd>

The [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) that generated the recognized text does not support confidence levels.

</dd> </dl>

## Remarks

The [**IInkAnalyzer**](iinkanalyzer.md) uses one or more [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects to convert handwriting to text.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IAnalysisAlternate::GetRecognitionConfidence Method**](ianalysisalternate-getrecognitionconfidence.md)
</dt> <dt>

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[Context Node Properties](context-node-properties.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




