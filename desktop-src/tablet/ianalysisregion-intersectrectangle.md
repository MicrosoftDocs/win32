---
description: Restricts the area of this IAnalysisRegion to the area created by its intersection with the specified rectangle.
ms.assetid: de6b565f-34c1-4551-ab92-db6bacb8608d
title: IAnalysisRegion::IntersectRectangle method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.IntersectRectangle
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::IntersectRectangle method

Restricts the area of this [**IAnalysisRegion**](ianalysisregion.md) to the area created by its intersection with the specified rectangle.

## Syntax


```C++
HRESULT IntersectRectangle(
  [in] RECT *pIntersectingRectangle
);
```



## Parameters

<dl> <dt>

*pIntersectingRectangle* \[in\]
</dt> <dd>

A pointer to the rectangle with which to intersect, in ink-space coordinates.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The rectangle coordinates are in HIMETRIC units.

If the two areas do not intersect, the new area is empty.

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

[**IAnalysisRegion::IntersectRegion Method**](ianalysisregion-intersectregion.md)
</dt> <dt>

[**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md)
</dt> <dt>

[**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




