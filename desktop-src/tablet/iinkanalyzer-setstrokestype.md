---
description: Changes the type of the specified strokes.
ms.assetid: 8d954a7d-c987-41cf-9933-b2e6bacc9489
title: IInkAnalyzer::SetStrokesType method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SetStrokesType
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SetStrokesType method

Changes the type of the specified strokes.

## Syntax


```C++
HRESULT SetStrokesType(
  [in] ULONG      strokeIdCount,
  [in] LONG       *plStrokes,
  [in] StrokeType StrokeType
);
```



## Parameters

<dl> <dt>

*strokeIdCount* \[in\]
</dt> <dd>

The number of stroke identifiers in *plStrokes*.

</dd> <dt>

*plStrokes* \[in\]
</dt> <dd>

An array containing the stroke identifiers of the strokes to which to assign *StrokeType*.

</dd> <dt>

*StrokeType* \[in\]
</dt> <dd>

The [**StrokeType**](stroketype.md) value to assign to the strokes.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

If the stroke's type is the [**StrokeType**](stroketype.md) value **StrokeType\_Unclassified**, the [**IInkAnalyzer**](iinkanalyzer.md) classifies the stroke during ink analysis. Otherwise, the **IInkAnalyzer** uses the type set on the stroke.

The [**IInkAnalyzer**](iinkanalyzer.md) does not set the stroke type value as part of ink analysis. To specify or change the stroke type, use [**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md) or **IInkAnalyzer::SetStrokesType Method**.

If a stroke is associated with an [**IContextNode**](icontextnode.md) that is not an unclassified ink node (see [**IContextNode::GetType**](icontextnode-gettype.md)), this method moves the stroke to an unclassified ink node that contains strokes of the same language. If no such context node exists, this method creates a new unclassified ink node and adds the stroke to it. An unclassified ink node is an **IContextNode** that is of type UnclassifiedInk.

If this method moves a stroke from an [**IContextNode**](icontextnode.md) that is not an unclassified ink node, this method also adds the stroke's bounding box to the ink analyzer's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)).

This method does not move a stroke if the *StrokeType* parameter matches the stroke's current type.

If a stroke identified in *strokeIds* is not associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method ignores the identifier.

If none of the specified strokes identify a stroke associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method returns without updating the **IInkAnalyzer**.

Setting the stroke type on strokes that are associated with a ContextNode that has NodeTypeAndProperties confirmed will raise an InvalidOperationException.

This method returns an error code when *plStrokes* is **NULL**.

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

[**IInkAnalyzer::GetStrokeType Method**](iinkanalyzer-getstroketype.md)
</dt> <dt>

[**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




