---
Description: Lists the matrix functions provided by DirectXMath.
ms.assetid: d59d0dcc-deae-3f7e-55c5-0c5ff383343b
title: DirectXMath Library Matrix Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectXMath Library Matrix Functions

Lists the matrix functions provided by DirectXMath.

> [!Note]  
> DirectXMath offers both left-handed and right-handed versions of matrix functions with 'handedness', but always assumes a row-major format.

 

## In this section



| Topic                                                                                               | Description                                                                                                                            |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**XMMatrixAffineTransformation**](https://msdn.microsoft.com/en-us/library/Ee419960(v=VS.85).aspx)<br/>                     | Builds an affine transformation matrix.<br/>                                                                                     |
| [**XMMatrixAffineTransformation2D**](https://msdn.microsoft.com/en-us/library/Ee419961(v=VS.85).aspx)<br/>                 | Builds a 2D affine transformation matrix in the xy plane. <br/>                                                                  |
| [**XMMatrixDecompose**](https://msdn.microsoft.com/en-us/library/Ee419962(v=VS.85).aspx)<br/>                                           | Breaks down a general 3D transformation matrix into its scalar, rotational, and translational components.<br/>                   |
| [**XMMatrixDeterminant**](https://msdn.microsoft.com/en-us/library/Ee419963(v=VS.85).aspx)<br/>                                       | Computes the determinant of a matrix.<br/>                                                                                       |
| [**XMMatrixIdentity**](https://msdn.microsoft.com/en-us/library/Ee419964(v=VS.85).aspx)<br/>                                             | Builds the identity matrix.<br/>                                                                                                 |
| [**XMMatrixInverse**](https://msdn.microsoft.com/en-us/library/Ee419965(v=VS.85).aspx)<br/>                                               | Computes the inverse of a matrix.<br/>                                                                                           |
| [**XMMatrixIsIdentity**](https://msdn.microsoft.com/en-us/library/Ee419966(v=VS.85).aspx)<br/>                                         | Tests whether a matrix is the identity matrix.<br/>                                                                              |
| [**XMMatrixIsInfinite**](https://msdn.microsoft.com/en-us/library/Ee419967(v=VS.85).aspx)<br/>                                         | Tests whether any of the elements of a matrix are positive or negative infinity.<br/>                                            |
| [**XMMatrixIsNaN**](https://msdn.microsoft.com/en-us/library/Ee419968(v=VS.85).aspx)<br/>                                                   | Tests whether any of the elements of a matrix are NaN.<br/>                                                                      |
| [**XMMatrixLookAtLH**](https://msdn.microsoft.com/en-us/library/Ee419969(v=VS.85).aspx)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a focal point.<br/>       |
| [**XMMatrixLookAtRH**](https://msdn.microsoft.com/en-us/library/Ee419970(v=VS.85).aspx)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a focal point.<br/>      |
| [**XMMatrixLookToLH**](https://msdn.microsoft.com/en-us/library/Ee419971(v=VS.85).aspx)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a camera direction.<br/>  |
| [**XMMatrixLookToRH**](https://msdn.microsoft.com/en-us/library/Ee419972(v=VS.85).aspx)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a camera direction.<br/> |
| [**XMMatrixMultiply**](https://msdn.microsoft.com/en-us/library/Ee419973(v=VS.85).aspx)<br/>                                             | Computes the product of two matrices.<br/>                                                                                       |
| [**XMMatrixMultiplyTranspose**](https://msdn.microsoft.com/en-us/library/Ee419974(v=VS.85).aspx)<br/>                           | Computes the transpose of the product of two matrices.<br/>                                                                      |
| [**XMMatrixOrthographicLH**](https://msdn.microsoft.com/en-us/library/Ee419975(v=VS.85).aspx)<br/>                                 | Builds an orthogonal projection matrix for a left-handed coordinate system.<br/>                                                 |
| [**XMMatrixOrthographicOffCenterLH**](https://msdn.microsoft.com/en-us/library/Ee419976(v=VS.85).aspx)<br/>               | Builds a custom orthogonal projection matrix for a left-handed coordinate system.<br/>                                           |
| [**XMMatrixOrthographicOffCenterRH**](https://msdn.microsoft.com/en-us/library/Ee419977(v=VS.85).aspx)<br/>               | Builds a custom orthogonal projection matrix for a right-handed coordinate system.<br/>                                          |
| [**XMMatrixOrthographicRH**](https://msdn.microsoft.com/en-us/library/Ee419978(v=VS.85).aspx)<br/>                                 | Builds an orthogonal projection matrix for a right-handed coordinate system.<br/>                                                |
| [**XMMatrixPerspectiveFovLH**](https://msdn.microsoft.com/en-us/library/Ee419979(v=VS.85).aspx)<br/>                             | Builds a left-handed perspective projection matrix based on a field of view.<br/>                                                |
| [**XMMatrixPerspectiveFovRH**](https://msdn.microsoft.com/en-us/library/Ee419980(v=VS.85).aspx)<br/>                             | Builds a right-handed perspective projection matrix based on a field of view.<br/>                                               |
| [**XMMatrixPerspectiveLH**](https://msdn.microsoft.com/en-us/library/Ee419981(v=VS.85).aspx)<br/>                                   | Builds a left-handed perspective projection matrix.<br/>                                                                         |
| [**XMMatrixPerspectiveOffCenterLH**](https://msdn.microsoft.com/en-us/library/Ee419982(v=VS.85).aspx)<br/>                 | Builds a custom version of a left-handed perspective projection matrix.<br/>                                                     |
| [**XMMatrixPerspectiveOffCenterRH**](https://msdn.microsoft.com/en-us/library/Ee419983(v=VS.85).aspx)<br/>                 | Builds a custom version of a right-handed perspective projection matrix.<br/>                                                    |
| [**XMMatrixPerspectiveRH**](https://msdn.microsoft.com/en-us/library/Ee419984(v=VS.85).aspx)<br/>                                   | Builds a right-handed perspective projection matrix.<br/>                                                                        |
| [**XMMatrixReflect**](https://msdn.microsoft.com/en-us/library/Ee419985(v=VS.85).aspx)<br/>                                               | Builds a transformation matrix designed to reflect vectors through a given plane.<br/>                                           |
| [**XMMatrixRotationAxis**](https://msdn.microsoft.com/en-us/library/Ee419986(v=VS.85).aspx)<br/>                                     | Builds a matrix that rotates around an arbitrary axis.<br/>                                                                      |
| [**XMMatrixRotationNormal**](https://msdn.microsoft.com/en-us/library/Ee419987(v=VS.85).aspx)<br/>                                 | Builds a matrix that rotates around an arbitrary normal vector.<br/>                                                             |
| [**XMMatrixRotationQuaternion**](https://msdn.microsoft.com/en-us/library/Ee419988(v=VS.85).aspx)<br/>                         | Builds a rotation matrix from a quaternion.<br/>                                                                                 |
| [**XMMatrixRotationRollPitchYaw**](https://msdn.microsoft.com/en-us/library/Ee419989(v=VS.85).aspx)<br/>                     | Builds a rotation matrix based on a given pitch, yaw, and roll (Euler angles).<br/>                                              |
| [**XMMatrixRotationRollPitchYawFromVector**](https://msdn.microsoft.com/en-us/library/Ee420010(v=VS.85).aspx)<br/> | Builds a rotation matrix based on a vector containing the Euler angles (pitch, yaw, and roll).<br/>                              |
| [**XMMatrixRotationX**](https://msdn.microsoft.com/en-us/library/Ee420011(v=VS.85).aspx)<br/>                                           | Builds a matrix that rotates around the x-axis.<br/>                                                                             |
| [**XMMatrixRotationY**](https://msdn.microsoft.com/en-us/library/Ee420012(v=VS.85).aspx)<br/>                                           | Builds a matrix that rotates around the y-axis.<br/>                                                                             |
| [**XMMatrixRotationZ**](https://msdn.microsoft.com/en-us/library/Ee420013(v=VS.85).aspx)<br/>                                           | Builds a matrix that rotates around the z-axis.<br/>                                                                             |
| [**XMMatrixScaling**](https://msdn.microsoft.com/en-us/library/Ee420014(v=VS.85).aspx)<br/>                                               | Builds a matrix that scales along the x-axis, y-axis, and z-axis.<br/>                                                           |
| [**XMMatrixScalingFromVector**](https://msdn.microsoft.com/en-us/library/Ee420015(v=VS.85).aspx)<br/>                           | Builds a scaling matrix from a 3D vector.<br/>                                                                                   |
| [**XMMatrixSet**](https://msdn.microsoft.com/en-us/library/Ee420016(v=VS.85).aspx)<br/>                                                       | Creates a matrix with **float** values.<br/>                                                                                     |
| [**XMMatrixShadow**](https://msdn.microsoft.com/en-us/library/Ee420017(v=VS.85).aspx)<br/>                                                 | Builds a transformation matrix that flattens geometry into a plane.<br/>                                                         |
| [**XMMatrixTransformation**](https://msdn.microsoft.com/en-us/library/Ee420018(v=VS.85).aspx)<br/>                                 | Builds a transformation matrix.<br/>                                                                                             |
| [**XMMatrixTransformation2D**](https://msdn.microsoft.com/en-us/library/Ee420019(v=VS.85).aspx)<br/>                             | Builds a 2D transformation matrix in the xy plane.<br/>                                                                          |
| [**XMMatrixTranslation**](https://msdn.microsoft.com/en-us/library/Ee420020(v=VS.85).aspx)<br/>                                       | Builds a translation matrix from the specified offsets.<br/>                                                                     |
| [**XMMatrixTranslationFromVector**](https://msdn.microsoft.com/en-us/library/Ee420021(v=VS.85).aspx)<br/>                   | Builds a translation matrix from a vector.<br/>                                                                                  |
| [**XMMatrixTranspose**](https://msdn.microsoft.com/en-us/library/Ee420022(v=VS.85).aspx)<br/>                                           | Computes the transpose of a matrix.<br/>                                                                                         |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




