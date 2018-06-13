---
Description: Lists the vector arithmetic functions.
ms.assetid: d7ed4516-74a6-81ec-79a2-2e39cf112d11
title: Vector Arithmetic Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Vector Arithmetic Functions

Lists the vector arithmetic functions.

## In this section



| Topic                                                                                   | Description                                                                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**XMVectorAbs**](https://msdn.microsoft.com/en-us/library/Ee420988(v=VS.85).aspx)<br/>                                           | Computes the absolute value of each component of an [**XMVECTOR**](xmvector-data-type.md).<br/>                    |
| [**XMVectorAdd**](https://msdn.microsoft.com/en-us/library/Ee420991(v=VS.85).aspx)<br/>                                           | Computes the sum of two vectors.<br/>                                                                               |
| [**XMVectorAddAngles**](https://msdn.microsoft.com/en-us/library/Ee420992(v=VS.85).aspx)<br/>                               | Adds two vectors representing angles.<br/>                                                                          |
| [**XMVectorCeiling**](https://msdn.microsoft.com/en-us/library/Ee421007(v=VS.85).aspx)<br/>                                   | Computes the ceiling of each component of an [**XMVECTOR**](xmvector-data-type.md).<br/>                           |
| [**XMVectorClamp**](https://msdn.microsoft.com/en-us/library/Ee421008(v=VS.85).aspx)<br/>                                       | Clamps the components of a vector to a specified minimum and maximum range.<br/>                                    |
| [**XMVectorDivide**](https://msdn.microsoft.com/en-us/library/Ff729805(v=VS.85).aspx)<br/>                                     | Divides one instance of `XMVECTOR` by a second instance, returning the result in a third instance.<br/>             |
| [**XMVectorFloor**](https://msdn.microsoft.com/en-us/library/Ee421024(v=VS.85).aspx)<br/>                                       | Computes the floor of each component of an [**XMVECTOR**](xmvector-data-type.md).<br/>                             |
| [**XMVectorIsInfinite**](https://msdn.microsoft.com/en-us/library/Ee421169(v=VS.85).aspx)<br/>                             | Performs a per-component test for +/- infinity on a vector.<br/>                                                    |
| [**XMVectorIsNaN**](https://msdn.microsoft.com/en-us/library/Ee421170(v=VS.85).aspx)<br/>                                       | Performs a per-component NaN test on a vector.<br/>                                                                 |
| [**XMVectorMax**](https://msdn.microsoft.com/en-us/library/Ee421177(v=VS.85).aspx)<br/>                                           | Makes a per-component comparison between two vectors, and returns a vector containing the largest components.<br/>  |
| [**XMVectorMin**](https://msdn.microsoft.com/en-us/library/Ee421181(v=VS.85).aspx)<br/>                                           | Makes a per-component comparison between two vectors, and returns a vector containing the smallest components.<br/> |
| [**XMVectorMod**](https://msdn.microsoft.com/en-us/library/Ee421183(v=VS.85).aspx)<br/>                                           | Computes the per-component floating-point remainder of the quotient of two vectors.<br/>                            |
| [**XMVectorModAngles**](https://msdn.microsoft.com/en-us/library/Ee421184(v=VS.85).aspx)<br/>                               | Computes the per-component angle modulo 2PI.<br/>                                                                   |
| [**XMVectorMultiply**](https://msdn.microsoft.com/en-us/library/Ee421185(v=VS.85).aspx)<br/>                                 | Computes the per-component product of two vectors.<br/>                                                             |
| [**XMVectorMultiplyAdd**](https://msdn.microsoft.com/en-us/library/Ee421186(v=VS.85).aspx)<br/>                           | Computes the product of the first two vectors added to the third vector.<br/>                                       |
| [**XMVectorNegate**](https://msdn.microsoft.com/en-us/library/Ee421188(v=VS.85).aspx)<br/>                                     | Computes the negation of a vector.<br/>                                                                             |
| [**XMVectorNegativeMultiplySubtract**](https://msdn.microsoft.com/en-us/library/Ee421189(v=VS.85).aspx)<br/> | Computes the difference of a third vector and the product of the first two vectors.<br/>                            |
| [**XMVectorPow**](https://msdn.microsoft.com/en-us/library/Ee421196(v=VS.85).aspx)<br/>                                           | Computes *V1* raised to the power of *V2*.<br/>                                                                     |
| [**XMVectorReciprocal**](https://msdn.microsoft.com/en-us/library/Ee421198(v=VS.85).aspx)<br/>                             | Computes the per-component reciprocal of a vector.<br/>                                                             |
| [**XMVectorReciprocalEst**](https://msdn.microsoft.com/en-us/library/Ee421199(v=VS.85).aspx)<br/>                       | Estimates the per-component reciprocal of a vector.<br/>                                                            |
| [**XMVectorReciprocalSqrt**](https://msdn.microsoft.com/en-us/library/Ee421200(v=VS.85).aspx)<br/>                     | Computes the per-component reciprocal square root of a vector.<br/>                                                 |
| [**XMVectorReciprocalSqrtEst**](https://msdn.microsoft.com/en-us/library/Ee421201(v=VS.85).aspx)<br/>               | Estimates the per-component reciprocal square root of a vector.<br/>                                                |
| [**XMVectorRound**](https://msdn.microsoft.com/en-us/library/Ee421208(v=VS.85).aspx)<br/>                                       | Rounds each component of a vector to the nearest integer.<br/>                                                      |
| [**XMVectorSaturate**](https://msdn.microsoft.com/en-us/library/Ee421209(v=VS.85).aspx)<br/>                                 | Saturates each component of a vector to the range 0.0f to 1.0f.<br/>                                                |
| [**XMVectorScale**](https://msdn.microsoft.com/en-us/library/Ee421210(v=VS.85).aspx)<br/>                                       | Scalar multiplies a vector by a floating-point value.<br/>                                                          |
| [**XMVectorSqrt**](https://msdn.microsoft.com/en-us/library/Ee421356(v=VS.85).aspx)<br/>                                         | Computes the per-component square root of a vector.<br/>                                                            |
| [**XMVectorSqrtEst**](https://msdn.microsoft.com/en-us/library/Ee421357(v=VS.85).aspx)<br/>                                   | Estimates the per-component square root of a vector.<br/>                                                           |
| [**XMVectorSubtract**](https://msdn.microsoft.com/en-us/library/Ee421358(v=VS.85).aspx)<br/>                                 | Computes the difference of two vectors.<br/>                                                                        |
| [**XMVectorSubtractAngles**](https://msdn.microsoft.com/en-us/library/Ee421359(v=VS.85).aspx)<br/>                     | Subtracts two vectors representing angles.<br/>                                                                     |
| [**XMVectorSum**](https://msdn.microsoft.com/en-us/library/Mt802013(v=VS.85).aspx)<br/>                                           | Computes the horizontal sum of the components of an [**XMVECTOR**](xmvector-data-type.md).<br/>                    |
| [**XMVectorTruncate**](https://msdn.microsoft.com/en-us/library/Ee421366(v=VS.85).aspx)<br/>                                 | Rounds each component of a vector to the nearest integer value in the direction of zero.<br/>                       |



 

## Related topics

<dl> <dt>

[DirectXMath Library Vector Functions](ovw-xnamath-reference-functions-vector.md)
</dt> </dl>

 

 




