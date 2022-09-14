---
description: Removes the specified stroke from the IInkAnalyzer.
ms.assetid: e182ae35-854e-401d-8e26-aee645c05430
title: IInkAnalyzer::RemoveStroke method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.RemoveStroke
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::RemoveStroke method

Removes the specified stroke from the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT RemoveStroke(
  [in] LONG *plStrokeId
);
```



## Parameters

<dl> <dt>

*plStrokeId* \[in\]
</dt> <dd>

The stroke identifier.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This method removes the packet data for, and references to, the specified stroke from the [**IInkAnalyzer**](iinkanalyzer.md).

This method removes the stroke from the leaf context node that references the stroke. If the [**IContextNode**](icontextnode.md) no longer references any strokes, this method deletes the **IContextNode** and any ancestor **IContextNode** objects that no longer have any child nodes.

After this method removes the stroke from the [**IContextNode**](icontextnode.md), it updates the [**IInkAnalyzer**](iinkanalyzer.md) object's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)) to include the bounding box of the removed stroke.

If *plStrokeId* does not identify a stroke associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method returns without updating the ink analyzer.

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

[**IInkAnalyzer::RemoveStrokes Method**](iinkanalyzer-removestrokes.md)
</dt> <dt>

[**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




