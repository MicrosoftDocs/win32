---
Description: Lists the plane functions provided by DirectXMath.
ms.assetid: 6505e72e-4af5-5db3-4fc0-f83fa77692b1
title: DirectXMath Library Plane Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectXMath Library Plane Functions

Lists the plane functions provided by DirectXMath.

These functions use an XMVECTOR 4-vector to represent the coefficients of the plane equation, Ax+By+Cz+D = 0, where the X-component is A, the Y-component is B, the Z-component is C, and the W-component is D.

## In this section



| Topic                                                               | Description                                                                                                      |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**XMPlaneDot**](/windows/desktop/api/DirectXMath/)<br/>                         | Calculates the dot product between an input plane and a 4D vector.<br/>                                    |
| [**XMPlaneDotCoord**](/windows/desktop/api/DirectXMath/)<br/>               | Calculates the dot product between an input plane and a 3D vector.<br/>                                    |
| [**XMPlaneDotNormal**](/windows/desktop/api/DirectXMath/)<br/>             | Calculates the dot product between the normal vector of a plane and a 3D vector.<br/>                      |
| [**XMPlaneEqual**](/windows/desktop/api/DirectXMath/)<br/>                     | Determines if two planes are equal.<br/>                                                                   |
| [**XMPlaneFromPointNormal**](/windows/desktop/api/DirectXMath/)<br/> | Computes the equation of a plane constructed from a point in the plane and a normal vector.<br/>           |
| [**XMPlaneFromPoints**](/windows/desktop/api/DirectXMath/)<br/>           | Computes the equation of a plane constructed from three points in the plane.<br/>                          |
| [**XMPlaneIntersectLine**](/windows/desktop/api/DirectXMath/)<br/>     | Finds the intersection between a plane and a line.<br/>                                                    |
| [**XMPlaneIntersectPlane**](/windows/desktop/api/DirectXMath/)<br/>   | Finds the intersection of two planes.<br/>                                                                 |
| [**XMPlaneIsInfinite**](/windows/desktop/api/DirectXMath/)<br/>           | Tests whether any of the coefficients of a plane is positive or negative infinity.<br/>                    |
| [**XMPlaneIsNaN**](/windows/desktop/api/DirectXMath/)<br/>                     | Tests whether any of the coefficients of a plane is a NaN.<br/>                                            |
| [**XMPlaneNearEqual**](/windows/desktop/api/DirectXMath/)<br/>             | Determines whether two planes are nearly equal.<br/>                                                       |
| [**XMPlaneNormalize**](/windows/desktop/api/DirectXMath/)<br/>             | Normalizes the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/> |
| [**XMPlaneNormalizeEst**](/windows/desktop/api/DirectXMath/)<br/>       | Estimates the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/>  |
| [**XMPlaneNotEqual**](/windows/desktop/api/DirectXMath/)<br/>               | Determines if two planes are unequal.<br/>                                                                 |
| [**XMPlaneTransform**](/windows/desktop/api/DirectXMath/)<br/>             | Transforms a plane by a given matrix.<br/>                                                                 |
| [**XMPlaneTransformStream**](/windows/desktop/api/DirectXMath/)<br/> | Transforms a stream of planes by a given matrix.<br/>                                                      |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




