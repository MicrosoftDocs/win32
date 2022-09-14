---
description: Exposes methods and properties for a region that represents an area of a document.
ms.assetid: ee823a9e-a144-4394-847e-abf390fb839a
title: IAnalysisRegion interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion interface

Exposes methods and properties for a region that represents an area of a document.

## Members

The **IAnalysisRegion** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IAnalysisRegion** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAnalysisRegion** interface has these methods.



| Method                                                           | Description                                                                                                                                    |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](ianalysisregion-clone.md)                           | Creates a copy of the **IAnalysisRegion**.<br/>                                                                                          |
| [**ExcludeRectangle**](ianalysisregion-excluderectangle.md)     | Restricts the area of the **IAnalysisRegion** to the portion of its area that does not intersect the specified rectangle.<br/>           |
| [**ExcludeRegion**](ianalysisregion-excluderegion.md)           | Restricts the area of the **IAnalysisRegion** to the portion of its area that does not intersect the specified **IAnalysisRegion**.<br/> |
| [**GetBounds**](ianalysisregion-getbounds.md)                   | Retrieves the bounding rectangle of the **IAnalysisRegion**.<br/>                                                                        |
| [**GetRegionScans**](ianalysisregion-getregionscans.md)         | Retrieves an array of rectangles that defines the area of the **IAnalysisRegion**.<br/>                                                  |
| [**IntersectRectangle**](ianalysisregion-intersectrectangle.md) | Restricts the area of this **IAnalysisRegion** to the area created by its intersection with the specified rectangle.<br/>                |
| [**IntersectRegion**](ianalysisregion-intersectregion.md)       | Restricts the area of the **IAnalysisRegion** to the area created by its intersection with the specified **IAnalysisRegion**.<br/>       |
| [**IntersectsWith**](ianalysisregion-intersectswith.md)         | Determines whether the area of the **IAnalysisRegion** intersects with the specified rectangle.<br/>                                     |
| [**IsEmpty**](ianalysisregion-isempty.md)                       | Retrieves a value indicating whether the **IAnalysisRegion** represents an empty region.<br/>                                            |
| [**IsInfinite**](ianalysisregion-isinfinite.md)                 | Retrieves a value indicating whether the **IAnalysisRegion** represents an infinite region.<br/>                                         |
| [**MakeEmpty**](ianalysisregion-makeempty.md)                   | Reduces the **IAnalysisRegion** to represent an empty area.<br/>                                                                         |
| [**MakeInfinite**](ianalysisregion-makeinfinite.md)             | Expands the **IAnalysisRegion** to represent an infinite area.<br/>                                                                      |
| [**UnionRectangle**](ianalysisregion-unionrectangle.md)         | Expands the area of this **IAnalysisRegion** to the area created by its union with the specified rectangle.<br/>                         |
| [**UnionRegion**](ianalysisregion-unionregion.md)               | Expands the area of this **IAnalysisRegion** to the area created by its union with the specified **IAnalysisRegion**.<br/>               |



 

## Remarks

This interface represents an area that is constructed from rectangular regions. The [**IInkAnalyzer**](iinkanalyzer.md) returns or interprets an area's coordinates within the coordinate space in which it receives stroke data.

To get the current bounds of the **IAnalysisRegion**, use [**IAnalysisRegion::GetBounds Method**](ianalysisregion-getbounds.md) or [**IAnalysisRegion::GetRegionScans Method**](ianalysisregion-getregionscans.md).

To modify the area of an existing **IAnalysisRegion**, use the following methods.

-   [**IAnalysisRegion::ExcludeRectangle**](ianalysisregion-excluderectangle.md)
-   [**IAnalysisRegion::ExcludeRegion Method**](ianalysisregion-excluderegion.md)
-   [**IAnalysisRegion::IntersectRectangle Method**](ianalysisregion-intersectrectangle.md)
-   [**IAnalysisRegion::IntersectRegion Method**](ianalysisregion-intersectregion.md)
-   [**IAnalysisRegion::MakeEmpty Method**](ianalysisregion-makeempty.md)
-   [**IAnalysisRegion::MakeInfinite Method**](ianalysisregion-makeinfinite.md)
-   [**IAnalysisRegion::UnionRectangle Method**](ianalysisregion-unionrectangle.md)
-   [**IAnalysisRegion::UnionRegion Method**](ianalysisregion-unionregion.md)

This interface is equivalent to the System.Windows.Ink.AnalysisCore.AnalysisRegionBase class in the .NET Framework.

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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

