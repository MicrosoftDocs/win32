---
Description: Lists the plane functions provided by DirectXMath.
ms.assetid: 6505e72e-4af5-5db3-4fc0-f83fa77692b1
title: DirectXMath Library Plane Functions
ms.topic: article
ms.date: 05/31/2018
---

# DirectXMath Library Plane Functions

Lists the plane functions provided by DirectXMath.

These functions use an XMVECTOR 4-vector to represent the coefficients of the plane equation, Ax+By+Cz+D = 0, where the X-component is A, the Y-component is B, the Z-component is C, and the W-component is D.

## In this section



| Topic                                                               | Description                                                                                                      |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**XMPlaneDot**](https://msdn.microsoft.com/en-us/library/Ee420137(v=VS.85).aspx)<br/>                         | Calculates the dot product between an input plane and a 4D vector.<br/>                                    |
| [**XMPlaneDotCoord**](https://msdn.microsoft.com/en-us/library/Ee420138(v=VS.85).aspx)<br/>               | Calculates the dot product between an input plane and a 3D vector.<br/>                                    |
| [**XMPlaneDotNormal**](https://msdn.microsoft.com/en-us/library/Ee420139(v=VS.85).aspx)<br/>             | Calculates the dot product between the normal vector of a plane and a 3D vector.<br/>                      |
| [**XMPlaneEqual**](https://msdn.microsoft.com/en-us/library/Ee420140(v=VS.85).aspx)<br/>                     | Determines if two planes are equal.<br/>                                                                   |
| [**XMPlaneFromPointNormal**](https://msdn.microsoft.com/en-us/library/Ee420141(v=VS.85).aspx)<br/> | Computes the equation of a plane constructed from a point in the plane and a normal vector.<br/>           |
| [**XMPlaneFromPoints**](https://msdn.microsoft.com/en-us/library/Ee420142(v=VS.85).aspx)<br/>           | Computes the equation of a plane constructed from three points in the plane.<br/>                          |
| [**XMPlaneIntersectLine**](https://msdn.microsoft.com/en-us/library/Ee420143(v=VS.85).aspx)<br/>     | Finds the intersection between a plane and a line.<br/>                                                    |
| [**XMPlaneIntersectPlane**](https://msdn.microsoft.com/en-us/library/Ee420144(v=VS.85).aspx)<br/>   | Finds the intersection of two planes.<br/>                                                                 |
| [**XMPlaneIsInfinite**](https://msdn.microsoft.com/en-us/library/Ee420145(v=VS.85).aspx)<br/>           | Tests whether any of the coefficients of a plane is positive or negative infinity.<br/>                    |
| [**XMPlaneIsNaN**](https://msdn.microsoft.com/en-us/library/Ee420146(v=VS.85).aspx)<br/>                     | Tests whether any of the coefficients of a plane is a NaN.<br/>                                            |
| [**XMPlaneNearEqual**](https://msdn.microsoft.com/en-us/library/Ee420147(v=VS.85).aspx)<br/>             | Determines whether two planes are nearly equal.<br/>                                                       |
| [**XMPlaneNormalize**](https://msdn.microsoft.com/en-us/library/Ee420148(v=VS.85).aspx)<br/>             | Normalizes the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/> |
| [**XMPlaneNormalizeEst**](https://msdn.microsoft.com/en-us/library/Ee420149(v=VS.85).aspx)<br/>       | Estimates the coefficients of a plane so that coefficients of x, y, and z form a unit normal vector.<br/>  |
| [**XMPlaneNotEqual**](https://msdn.microsoft.com/en-us/library/Ee420150(v=VS.85).aspx)<br/>               | Determines if two planes are unequal.<br/>                                                                 |
| [**XMPlaneTransform**](https://msdn.microsoft.com/en-us/library/Ee420151(v=VS.85).aspx)<br/>             | Transforms a plane by a given matrix.<br/>                                                                 |
| [**XMPlaneTransformStream**](https://msdn.microsoft.com/en-us/library/Hh404689(v=VS.85).aspx)<br/> | Transforms a stream of planes by a given matrix.<br/>                                                      |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




