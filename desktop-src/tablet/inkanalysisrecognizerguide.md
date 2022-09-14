---
description: Specifies the guide, or area where ink is drawn and recognized.
ms.assetid: 5bd874ff-003b-4471-b4ef-50731007dc5a
title: InkAnalysisRecognizerGuide structure (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkAnalysisRecognizerGuide
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# InkAnalysisRecognizerGuide structure

Specifies the guide, or area where ink is drawn and recognized.

## Syntax


```C++
typedef struct InkAnalysisRecognizerGuide {
  RECT rectWritingBox;
  RECT rectDrawnBox;
  long cRows;
  long cColumns;
  long midline;
} InkAnalysisRecognizerGuide;
```



## Members

<dl> <dt>

**rectWritingBox**
</dt> <dd>

The invisible writing area of the recognition guide in which writing can actually take place.

</dd> <dt>

**rectDrawnBox**
</dt> <dd>

The rectangle that is drawn on the tablet screen and in which writing takes place.

</dd> <dt>

**cRows**
</dt> <dd>

The number of rows in the recognition guide box.

</dd> <dt>

**cColumns**
</dt> <dd>

The number of columns in the recognition guide box.

</dd> <dt>

**midline**
</dt> <dd>

The midline height of the recognition guide box. The midline height is the distance from the baseline to the midline, of the drawn box.

</dd> </dl>

## Remarks

An **InkAnalysisRecognizerGuide** defines an expected area of input, such as a line or boxes, for characters. An **InkAnalysisRecognizerGuide** structure can be set only on an analysis hint context node (see [**IContextNode::GetType**](icontextnode-gettype.md)). The [**IInkAnalyzer**](iinkanalyzer.md) uses the location of the analysis hint node and the locations of the ink strokes to associate a stroke with the analysis hint node. Any strokes with an association to the analysis hint node will have the specified **InkAnalysisRecognizerGuide** used when recognized by an **IInkAnalyzer**, provided the **IInkAnalyzer** supports the **InkAnalysisRecognizerGuide**. The values expressed in the **InkAnalysisRecognizerGuide** class are always relative to the location of the analysis hint node and are specified in ink space coordinates.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[Analysis Hint Properties](analysis-hint-properties.md)
</dt> <dt>

[**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
</dt> <dt>

[**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




