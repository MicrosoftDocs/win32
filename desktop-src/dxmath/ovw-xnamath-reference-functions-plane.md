---
Description: Lists the plane functions provided by DirectXMath.
ms.assetid: 6505e72e-4af5-5db3-4fc0-f83fa77692b1
title: DirectXMath Library Plane Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DirectXMath Library Plane Functions

Lists the plane functions provided by DirectXMath.

These functions use an XMVECTOR 4-vector to represent the coefficients of the plane equation, Ax+By+Cz+D = 0, where the X-component is A, the Y-component is B, the Z-component is C, and the W-component is D.

## In this section



| Topic                                                               | Description                                                                                                      |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**XMPlaneDot**](/windows/win32/DirectXMath/?branch=master)<br/>                         | Calculates the dot product between an input plane and a 4D vector.<br/>                                    |
| [**XMPlaneDotCoord**](/windows/win32/DirectXMath/?branch=master)<br/>               | Calculates the dot product between an input plane and a 3D vector.<br/>                                    |
| [**XMPlaneDotNormal**](/windows/win32/DirectXMath/?branch=master)<br/>             | Calculates the dot product between the normal vector of a plane and a 3D vector.<br/>                      |
| [**XMPlaneEqual**](/windows/win32/DirectXMath/?branch=master)<br/>                     | Determines if two planes are equal.<br/>                                                                   |
| [**XMPlaneFromPointNormal**](/windows/win32/DirectXMath/?branch=master)<br/> | Computes the equation of a plane constructed from a point in the plane and a normal vector.<br/>           |
| [**XMPlaneFromPoints**](/windows/win32/DirectXMath/?branch=master)<br/>           | Computes the equation of a plane constructed from three points in the plane.<br/>                          |
| [**XMPlaneIntersectLine**](/windows/win32/DirectXMath/?branch=master)<br/>     | Finds the intersection between a plane and a line.<br/>                                                    |
| [**XMPlaneIntersectPlane**](/windows/win32/DirectXMath/?branch=master)<br/>   | Finds the intersection of two planes.<br/>                                                                 |
| [**XMPlaneIsInfinite**](/windows/win32/DirectXMath/?branch=master)<br/>           | Tests whether any of the coefficients of a plane is positive or negative infinity.<br/>                    |
| [**XMPlaneIsNaN**](/windows/win32/DirectXMath/?branch=master)<br/>                     | Tests whether any of the coefficients of a plane is a NaN.<br/>                                            |
| [**XMPlaneNearEqual**](/windows/win32/DirectXMath/?branch=master)<br/>             | Determines whether two planes are nearly equal.<br/>                                                       |
| [**XMPlaneNormalize**](/windows/win32/DirectXMath/?branch=master)<br/>             | Normalizes the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/> |
| [**XMPlaneNormalizeEst**](/windows/win32/DirectXMath/?branch=master)<br/>       | Estimates the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/>  |
| [**XMPlaneNotEqual**](/windows/win32/DirectXMath/?branch=master)<br/>               | Determines if two planes are unequal.<br/>                                                                 |
| [**XMPlaneTransform**](/windows/win32/DirectXMath/?branch=master)<br/>             | Transforms a plane by a given matrix.<br/>                                                                 |
| [**XMPlaneTransformStream**](/windows/win32/DirectXMath/?branch=master)<br/> | Transforms a stream of planes by a given matrix.<br/>                                                      |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




