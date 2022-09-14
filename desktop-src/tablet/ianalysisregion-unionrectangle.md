---
description: Expands the area of this IAnalysisRegion to the area created by its union with the specified rectangle.
ms.assetid: 9b12f509-4f6a-43b0-9639-bef060fd6d50
title: IAnalysisRegion::UnionRectangle method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.UnionRectangle
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::UnionRectangle method

Expands the area of this [**IAnalysisRegion**](ianalysisregion.md) to the area created by its union with the specified rectangle.

## Syntax


```C++
HRESULT UnionRectangle(
  [in] RECT *pRectangle
);
```



## Parameters

<dl> <dt>

*pRectangle* \[in\]
</dt> <dd>

A pointer to the rectangle with which to combine, in ink-space coordinates.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The rectangle coordinates are in HIMETRIC units.

If either area is infinite, the new area is also infinite.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[**IAnalysisRegion::ExcludeRectangle**](ianalysisregion-excluderectangle.md)
</dt> <dt>

[**IAnalysisRegion::ExcludeRegion Method**](ianalysisregion-excluderegion.md)
</dt> <dt>

[**IAnalysisRegion::IntersectRectangle Method**](ianalysisregion-intersectrectangle.md)
</dt> <dt>

[**IAnalysisRegion::IntersectRegion Method**](ianalysisregion-intersectregion.md)
</dt> <dt>

[**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




