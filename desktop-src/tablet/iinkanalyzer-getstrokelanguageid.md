---
description: Returns the locale identifier of the specified stroke.
ms.assetid: a5fb9b7a-ed3e-4552-9412-39529203bd81
title: IInkAnalyzer::GetStrokeLanguageId method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetStrokeLanguageId
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetStrokeLanguageId method

Returns the locale identifier of the specified stroke.

## Syntax


```C++
HRESULT GetStrokeLanguageId(
  [in]  LONG lStrokeId,
  [out] LONG *lStrokeLCID
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The stroke identifier.

</dd> <dt>

*lStrokeLCID* \[out\]
</dt> <dd>

The locale identifier for the specified stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The stroke's locale is set when you add the stroke by calling [**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md), [**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md), [**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md), or [**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md). To change the stroke's locale, use [**IInkAnalyzer::SetStrokeLanguageId Method**](iinkanalyzer-setstrokelanguageid.md) or [**IInkAnalyzer::SetStrokesLanguageId Method**](iinkanalyzer-setstrokeslanguageid.md).

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

[**IInkAnalyzer::SetStrokeLanguageId Method**](iinkanalyzer-setstrokelanguageid.md)
</dt> <dt>

[**IInkAnalyzer::SetStrokesLanguageId Method**](iinkanalyzer-setstrokeslanguageid.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




