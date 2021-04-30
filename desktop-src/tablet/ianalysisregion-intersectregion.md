---
description: Restricts the area of the IAnalysisRegion to the area created by its intersection with the specified IAnalysisRegion.
ms.assetid: 02b3049f-ada9-4de3-a7a2-f9ff8313fbab
title: IAnalysisRegion::IntersectRegion method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.IntersectRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::IntersectRegion method

Restricts the area of the [**IAnalysisRegion**](ianalysisregion.md) to the area created by its intersection with the specified **IAnalysisRegion**.

## Syntax


```C++
HRESULT IntersectRegion(
  [in] IAnalysisRegion *pRegionToIntersect
);
```



## Parameters

<dl> <dt>

*pRegionToIntersect* \[in\]
</dt> <dd>

The [**IAnalysisRegion**](ianalysisregion.md) with which to intersect.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

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

[**IAnalysisRegion::IntersectRectangle Method**](ianalysisregion-intersectrectangle.md)
</dt> <dt>

[**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md)
</dt> <dt>

[**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




