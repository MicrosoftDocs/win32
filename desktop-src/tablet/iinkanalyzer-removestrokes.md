---
description: Removes the specified strokes from the IInkAnalyzer.
ms.assetid: ea7c8a9f-a427-4781-b5ba-97ffd983dbe5
title: IInkAnalyzer::RemoveStrokes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.RemoveStrokes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::RemoveStrokes method

Removes the specified strokes from the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT RemoveStrokes(
  [in] ULONG ulStrokeIdCount,
  [in] LONG  *plStrokes
);
```



## Parameters

<dl> <dt>

*ulStrokeIdCount* \[in\]
</dt> <dd>

The number of stroke identifiers in *plStrokes*.

</dd> <dt>

*plStrokes* \[in\]
</dt> <dd>

The identifiers for the strokes to remove.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This method removes the packet data for and references to the specified strokes from the [**IInkAnalyzer**](iinkanalyzer.md).

This method removes the strokes from the leaf context node that references the strokes. If any [**IContextNode**](icontextnode.md) no longer references any strokes, this method deletes the **IContextNode** and any ancestor **IContextNode** objects that no longer have any child nodes.

After this method removes the strokes from the [**IContextNode**](icontextnode.md), it updates the [**IInkAnalyzer**](iinkanalyzer.md) object's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)) to include the bounding box of the removed strokes.

If a stroke identified in *plStrokes* is not associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method ignores the identifier.

If none of the strokes identified in *plStrokes* are associated with the ink analyzer, this method returns without updating the [**IInkAnalyzer**](iinkanalyzer.md).

This method returns and error code when *plStrokes* is null.

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

[**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::RemoveStroke Method**](iinkanalyzer-removestroke.md)
</dt> <dt>

[**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




