---
description: Retrieves the type of the specified stroke.
ms.assetid: bbd0bc23-89f9-4033-bc32-f9bd737c960c
title: IInkAnalyzer::GetStrokeType method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetStrokeType
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetStrokeType method

Retrieves the type of the specified stroke.

## Syntax


```C++
HRESULT GetStrokeType(
  [in]  LONG       lStrokeId,
  [out] StrokeType *pStrokeType
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The stroke identifier.

</dd> <dt>

*pStrokeType* \[out\]
</dt> <dd>

The classification of the specified stroke.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

If the stroke's type is the [**StrokeType**](stroketype.md) value StrokeType\_Unclassified, the [**IInkAnalyzer**](iinkanalyzer.md) classifies the stroke during ink analysis. Otherwise, the **IInkAnalyzer** uses the type set on the stroke.

The [**IInkAnalyzer**](iinkanalyzer.md) does not set the stroke type value as part of ink analysis. To specify or change the stroke type, use [**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md) or [**IInkAnalyzer::SetStrokesType Method**](iinkanalyzer-setstrokestype.md).

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

[**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md)
</dt> <dt>

[**IInkAnalyzer::SetStrokesType Method**](iinkanalyzer-setstrokestype.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




