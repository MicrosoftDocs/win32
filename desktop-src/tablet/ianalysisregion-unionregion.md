---
description: Expands the area of this IAnalysisRegion to the area created by its union with the specified IAnalysisRegion.
ms.assetid: cc3ec5c6-98ff-442e-a1e8-d1a57752ad56
title: IAnalysisRegion::UnionRegion method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.UnionRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::UnionRegion method

Expands the area of this [**IAnalysisRegion**](ianalysisregion.md) to the area created by its union with the specified **IAnalysisRegion**.

## Syntax


```C++
HRESULT UnionRegion(
  [in] IAnalysisRegion *pRegionToUnion
);
```



## Parameters

<dl> <dt>

*pRegionToUnion* \[in\]
</dt> <dd>

The [**IAnalysisRegion**](ianalysisregion.md) with which to combine.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

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

[**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




