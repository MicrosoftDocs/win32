---
description: Restricts the area of the IAnalysisRegion to the portion of its area that does not intersect the specified rectangle.
ms.assetid: a35b8bfc-a87a-4e9a-908f-2b13a128d222
title: IAnalysisRegion::ExcludeRectangle method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.ExcludeRectangle
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::ExcludeRectangle method

Restricts the area of the [**IAnalysisRegion**](ianalysisregion.md) to the portion of its area that does not intersect the specified rectangle.

## Syntax


```C++
HRESULT ExcludeRectangle(
  [in] RECT *pExcludingRectangle
);
```



## Parameters

<dl> <dt>

*pExcludingRectangle* \[in\]
</dt> <dd>

The rectangle to exclude from this [**IAnalysisRegion**](ianalysisregion.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The rectangle coordinates are in HIMETRIC units.

If the two areas do not intersect, the [**IAnalysisRegion**](ianalysisregion.md) is unchanged.

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

[**IAnalysisRegion::ExcludeRegion Method**](ianalysisregion-excluderegion.md)
</dt> <dt>

[**IAnalysisRegion::IntersectRectangle Method**](ianalysisregion-intersectrectangle.md)
</dt> <dt>

[**IAnalysisRegion::IntersectRegion Method**](ianalysisregion-intersectregion.md)
</dt> <dt>

[**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md)
</dt> <dt>

[**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




