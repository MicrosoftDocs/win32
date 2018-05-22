---
Description: 'An application combines two regions by calling the CombineRgn function.'
ms.assetid: 'd16f9ca5-33e2-4752-900e-743245838377'
title: Combining Regions
---

# Combining Regions

An application combines two regions by calling the [**CombineRgn**](combinergn.md) function. Using this function, an application can combine the intersecting parts of two regions, all but the intersecting parts of two regions, the two original regions in their entirety, and so on. Following are five values that define the region combinations.



| Value     | Meaning                                                                               |
|-----------|---------------------------------------------------------------------------------------|
| RGN\_AND  | The intersecting parts of two original regions define a new region.                   |
| RGN\_COPY | A copy of the first (of the two original regions) defines a new region.               |
| RGN\_DIFF | The part of the first region that does not intersect the second defines a new region. |
| RGN\_OR   | The two original regions define a new region.                                         |
| RGN\_XOR  | Those parts of the two original regions that do not overlap define a new region.      |



 

The following illustration shows the five possible combinations of a square and a circular region resulting from a call to [**CombineRgn**](combinergn.md).

![illustration that demonstrates the results described in the previous table](images/csrgn-02.png)

 

 



