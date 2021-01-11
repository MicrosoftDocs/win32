---
description: Changes the locale identifier for the specified stroke.
ms.assetid: 3714462d-0391-481f-968a-3c121b7dd538
title: IInkAnalyzer::SetStrokeLanguageId method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SetStrokeLanguageId
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SetStrokeLanguageId method

Changes the locale identifier for the specified stroke.

## Syntax


```C++
HRESULT SetStrokeLanguageId(
  [in] LONG lStrokeId,
  [in] LONG lStrokeLCID
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The identifier of the stroke to which to assign the locale identifier.

</dd> <dt>

*lStrokeLCID* \[in\]
</dt> <dd>

The locale identifier to assign to the stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

A stroke's locale is set when you add the stroke by calling [**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md), [**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md), [**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md), or [**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md). To get the locale currently assigned to a stroke, call [**IInkAnalyzer::GetStrokeLanguageId Method**](iinkanalyzer-getstrokelanguageid.md).

The specified stroke is moved to an unclassified ink node (see [**IContextNode::GetType**](icontextnode-gettype.md)) that contains strokes of the same language. If no such [**IContextNode**](icontextnode.md) exists, this method creates a new unclassified ink node and moves the stroke to it. An unclassified ink node is an **IContextNode** that has a type of UnclassifiedInk.

If this method moves a stroke from an [**IContextNode**](icontextnode.md) that is not an unclassified ink node, this method also adds the stroke's bounding box to the ink analyzer's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)).

This method does not move a stroke if the *lStrokeLCID* parameter matches the stroke's current language identifier.

If the specified stroke is not associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method returns without updating the **IInkAnalyzer**.

For more information about language identifiers, see [Language Identifier Constants and Strings](/windows/desktop/Intl/language-identifier-constants-and-strings).

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

[**IInkAnalyzer::GetStrokeLanguageId Method**](iinkanalyzer-getstrokelanguageid.md)
</dt> <dt>

[**IInkAnalyzer::SetStrokesLanguageId Method**](iinkanalyzer-setstrokeslanguageid.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

