---
Description: Lists the matrix functions provided by DirectXMath.
ms.assetid: d59d0dcc-deae-3f7e-55c5-0c5ff383343b
title: DirectXMath Library Matrix Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DirectXMath Library Matrix Functions

Lists the matrix functions provided by DirectXMath.

> [!Note]  
> DirectXMath offers both left-handed and right-handed versions of matrix functions with 'handedness', but always assumes a row-major format.

 

## In this section



| Topic                                                                                               | Description                                                                                                                            |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**XMMatrixAffineTransformation**](/windows/win32/DirectXMath/?branch=master)<br/>                     | Builds an affine transformation matrix.<br/>                                                                                     |
| [**XMMatrixAffineTransformation2D**](/windows/win32/DirectXMath/?branch=master)<br/>                 | Builds a 2D affine transformation matrix in the xy plane. <br/>                                                                  |
| [**XMMatrixDecompose**](/windows/win32/DirectXMath/?branch=master)<br/>                                           | Breaks down a general 3D transformation matrix into its scalar, rotational, and translational components.<br/>                   |
| [**XMMatrixDeterminant**](/windows/win32/DirectXMath/?branch=master)<br/>                                       | Computes the determinant of a matrix.<br/>                                                                                       |
| [**XMMatrixIdentity**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Builds the identity matrix.<br/>                                                                                                 |
| [**XMMatrixInverse**](/windows/win32/DirectXMath/?branch=master)<br/>                                               | Computes the inverse of a matrix.<br/>                                                                                           |
| [**XMMatrixIsIdentity**](/windows/win32/DirectXMath/?branch=master)<br/>                                         | Tests whether a matrix is the identity matrix.<br/>                                                                              |
| [**XMMatrixIsInfinite**](/windows/win32/DirectXMath/?branch=master)<br/>                                         | Tests whether any of the elements of a matrix are positive or negative infinity.<br/>                                            |
| [**XMMatrixIsNaN**](/windows/win32/DirectXMath/?branch=master)<br/>                                                   | Tests whether any of the elements of a matrix are NaN.<br/>                                                                      |
| [**XMMatrixLookAtLH**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a focal point.<br/>       |
| [**XMMatrixLookAtRH**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a focal point.<br/>      |
| [**XMMatrixLookToLH**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a camera direction.<br/>  |
| [**XMMatrixLookToRH**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a camera direction.<br/> |
| [**XMMatrixMultiply**](/windows/win32/DirectXMath/?branch=master)<br/>                                             | Computes the product of two matrices.<br/>                                                                                       |
| [**XMMatrixMultiplyTranspose**](/windows/win32/DirectXMath/?branch=master)<br/>                           | Computes the transpose of the product of two matrices.<br/>                                                                      |
| [**XMMatrixOrthographicLH**](/windows/win32/DirectXMath/?branch=master)<br/>                                 | Builds an orthogonal projection matrix for a left-handed coordinate system.<br/>                                                 |
| [**XMMatrixOrthographicOffCenterLH**](/windows/win32/DirectXMath/?branch=master)<br/>               | Builds a custom orthogonal projection matrix for a left-handed coordinate system.<br/>                                           |
| [**XMMatrixOrthographicOffCenterRH**](/windows/win32/DirectXMath/?branch=master)<br/>               | Builds a custom orthogonal projection matrix for a right-handed coordinate system.<br/>                                          |
| [**XMMatrixOrthographicRH**](/windows/win32/DirectXMath/?branch=master)<br/>                                 | Builds an orthogonal projection matrix for a right-handed coordinate system.<br/>                                                |
| [**XMMatrixPerspectiveFovLH**](/windows/win32/DirectXMath/?branch=master)<br/>                             | Builds a left-handed perspective projection matrix based on a field of view.<br/>                                                |
| [**XMMatrixPerspectiveFovRH**](/windows/win32/DirectXMath/?branch=master)<br/>                             | Builds a right-handed perspective projection matrix based on a field of view.<br/>                                               |
| [**XMMatrixPerspectiveLH**](/windows/win32/DirectXMath/?branch=master)<br/>                                   | Builds a left-handed perspective projection matrix.<br/>                                                                         |
| [**XMMatrixPerspectiveOffCenterLH**](/windows/win32/DirectXMath/?branch=master)<br/>                 | Builds a custom version of a left-handed perspective projection matrix.<br/>                                                     |
| [**XMMatrixPerspectiveOffCenterRH**](/windows/win32/DirectXMath/?branch=master)<br/>                 | Builds a custom version of a right-handed perspective projection matrix.<br/>                                                    |
| [**XMMatrixPerspectiveRH**](/windows/win32/DirectXMath/?branch=master)<br/>                                   | Builds a right-handed perspective projection matrix.<br/>                                                                        |
| [**XMMatrixReflect**](/windows/win32/DirectXMath/?branch=master)<br/>                                               | Builds a transformation matrix designed to reflect vectors through a given plane.<br/>                                           |
| [**XMMatrixRotationAxis**](/windows/win32/DirectXMath/?branch=master)<br/>                                     | Builds a matrix that rotates around an arbitrary axis.<br/>                                                                      |
| [**XMMatrixRotationNormal**](/windows/win32/DirectXMath/?branch=master)<br/>                                 | Builds a matrix that rotates around an arbitrary normal vector.<br/>                                                             |
| [**XMMatrixRotationQuaternion**](/windows/win32/DirectXMath/?branch=master)<br/>                         | Builds a rotation matrix from a quaternion.<br/>                                                                                 |
| [**XMMatrixRotationRollPitchYaw**](/windows/win32/DirectXMath/?branch=master)<br/>                     | Builds a rotation matrix based on a given pitch, yaw, and roll (Euler angles).<br/>                                              |
| [**XMMatrixRotationRollPitchYawFromVector**](/windows/win32/DirectXMath/?branch=master)<br/> | Builds a rotation matrix based on a vector containing the Euler angles (pitch, yaw, and roll).<br/>                              |
| [**XMMatrixRotationX**](/windows/win32/DirectXMath/?branch=master)<br/>                                           | Builds a matrix that rotates around the x-axis.<br/>                                                                             |
| [**XMMatrixRotationY**](/windows/win32/DirectXMath/?branch=master)<br/>                                           | Builds a matrix that rotates around the y-axis.<br/>                                                                             |
| [**XMMatrixRotationZ**](/windows/win32/DirectXMath/?branch=master)<br/>                                           | Builds a matrix that rotates around the z-axis.<br/>                                                                             |
| [**XMMatrixScaling**](/windows/win32/DirectXMath/?branch=master)<br/>                                               | Builds a matrix that scales along the x-axis, y-axis, and z-axis.<br/>                                                           |
| [**XMMatrixScalingFromVector**](/windows/win32/DirectXMath/?branch=master)<br/>                           | Builds a scaling matrix from a 3D vector.<br/>                                                                                   |
| [**XMMatrixSet**](/windows/win32/DirectXMath/?branch=master)<br/>                                                       | Creates a matrix with **float** values.<br/>                                                                                     |
| [**XMMatrixShadow**](/windows/win32/DirectXMath/?branch=master)<br/>                                                 | Builds a transformation matrix that flattens geometry into a plane.<br/>                                                         |
| [**XMMatrixTransformation**](/windows/win32/DirectXMath/?branch=master)<br/>                                 | Builds a transformation matrix.<br/>                                                                                             |
| [**XMMatrixTransformation2D**](/windows/win32/DirectXMath/?branch=master)<br/>                             | Builds a 2D transformation matrix in the xy plane.<br/>                                                                          |
| [**XMMatrixTranslation**](/windows/win32/DirectXMath/?branch=master)<br/>                                       | Builds a translation matrix from the specified offsets.<br/>                                                                     |
| [**XMMatrixTranslationFromVector**](/windows/win32/DirectXMath/?branch=master)<br/>                   | Builds a translation matrix from a vector.<br/>                                                                                  |
| [**XMMatrixTranspose**](/windows/win32/DirectXMath/?branch=master)<br/>                                           | Computes the transpose of a matrix.<br/>                                                                                         |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




