---
description: Determines whether the area of the IAnalysisRegion intersects with the specified rectangle.
ms.assetid: 683c3ad8-0236-474e-a16d-6164c2244cfb
title: IAnalysisRegion::IntersectsWith method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.IntersectsWith
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::IntersectsWith method

Determines whether the area of the [**IAnalysisRegion**](ianalysisregion.md) intersects with the specified rectangle.

## Syntax


```C++
HRESULT IntersectsWith(
  [in]  RECT         *pRectangle,
  [out] VARIANT_BOOL *pfIsIntersecting
);
```



## Parameters

<dl> <dt>

*pRectangle* \[in\]
</dt> <dd>

A pointer to the rectangle with which to compare, in ink-space coordinates.

</dd> <dt>

*pfIsIntersecting* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the area of the [**IAnalysisRegion**](ianalysisregion.md) intersects with the specified rectangle; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The comparison is in ink-space coordinates.

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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




