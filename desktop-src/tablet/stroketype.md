---
description: Indicates whether a stroke should be analyzed as part of a drawing or as part of writing.
ms.assetid: '3f4c4522-ada7-4759-bca7-88b2a71f36ea'
title: StrokeType enumeration (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StrokeType
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# StrokeType enumeration

Indicates whether a stroke should be analyzed as part of a drawing or as part of writing.

## Syntax


```C++
typedef enum StrokeType { 
  StrokeType_Unclassified  = 0,
  StrokeType_Writing       = 1,
  StrokeType_Drawing       = 2
} StrokeType;
```



## Constants

<dl> <dt>

<span id="StrokeType_Unclassified"></span><span id="stroketype_unclassified"></span><span id="STROKETYPE_UNCLASSIFIED"></span>**StrokeType\_Unclassified**
</dt> <dd>

The stroke might be either part of a drawing or part of writing.

</dd> <dt>

<span id="StrokeType_Writing"></span><span id="stroketype_writing"></span><span id="STROKETYPE_WRITING"></span>**StrokeType\_Writing**
</dt> <dd>

The stroke is part of writing.

</dd> <dt>

<span id="StrokeType_Drawing"></span><span id="stroketype_drawing"></span><span id="STROKETYPE_DRAWING"></span>**StrokeType\_Drawing**
</dt> <dd>

The stroke is part of a drawing.

</dd> </dl>

## Examples

The following example shows part of a stroke event handler, implemented in a similar fashion to the [C++ Event Sinks Sample](c---event-sinks-sample.md). The added stroke is checked to see if the top of its bounding box has been drawn below a margin, `drawingMargin`. If so, the [**IInkAnalyzer**](iinkanalyzer.md) object, `m_spInkAnalyzer`, is set to analyze the stroke as a drawing stroke, rather than as a handwriting stroke. `CheckHResult` is a function that takes an `HRESULT` and a string, and throws an exception created with the string if the `HRESULT` is not **SUCCESS**.


```C++
IInkRectangle* bounds;
CheckHResult(pStroke->GetBoundingBox(IBBM_Default, &bounds), "IInkStrokeDisp::GetBoundingBox failed");
long top;
CheckHResult(bounds->get_Top(&top), "IInkRectangle::get_Top failed");
if (top > drawingMargin)
{
    long strokeId;
    CheckHResult(pStroke->get_ID(&strokeId), "IInkStrokeDisp::get_ID failed");
    m_pInkAnalyzer->SetStrokeType(strokeId, StrokeType_Drawing);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md)
</dt> </dl>

 

 




