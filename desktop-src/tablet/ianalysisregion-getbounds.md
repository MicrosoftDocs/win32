---
description: Gets the bounding rectangle of the IAnalysisRegion.
ms.assetid: 6b9deff7-12e9-4b30-86cb-25b94737d28d
title: IAnalysisRegion::GetBounds method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.GetBounds
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::GetBounds method

Gets the bounding rectangle of the [**IAnalysisRegion**](ianalysisregion.md).

## Syntax


```C++
HRESULT GetBounds(
  [out] RECT *pBoundingRectangle
);
```



## Parameters

<dl> <dt>

*pBoundingRectangle* \[out\]
</dt> <dd>

The bounding rectangle of the [**IAnalysisRegion**](ianalysisregion.md) in ink space coordinates.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The bounds are in ink-space coordinates.

If the [**IAnalysisRegion**](ianalysisregion.md) represents an infinite area, the left and top bounds are **INT\_MIN**; and the right and bottom bounds are **INT\_MAX**.

If the [**IAnalysisRegion**](ianalysisregion.md) represents an empty area, all the bounds of the rectangle are 0.

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

[**IAnalysisRegion::GetRegionScans Method**](ianalysisregion-getregionscans.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




