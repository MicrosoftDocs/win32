---
Description: 'Lists the matrix functions provided by DirectXMath.'
ms.assetid: 'd59d0dcc-deae-3f7e-55c5-0c5ff383343b'
title: DirectXMath Library Matrix Functions
---

# DirectXMath Library Matrix Functions

Lists the matrix functions provided by DirectXMath.

> [!Note]  
> DirectXMath offers both left-handed and right-handed versions of matrix functions with 'handedness', but always assumes a row-major format.

 

## In this section



| Topic                                                                                               | Description                                                                                                                            |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**XMMatrixAffineTransformation**](xmmatrixaffinetransformation.md)<br/>                     | Builds an affine transformation matrix.<br/>                                                                                     |
| [**XMMatrixAffineTransformation2D**](xmmatrixaffinetransformation2d.md)<br/>                 | Builds a 2D affine transformation matrix in the xy plane. <br/>                                                                  |
| [**XMMatrixDecompose**](xmmatrixdecompose.md)<br/>                                           | Breaks down a general 3D transformation matrix into its scalar, rotational, and translational components.<br/>                   |
| [**XMMatrixDeterminant**](xmmatrixdeterminant.md)<br/>                                       | Computes the determinant of a matrix.<br/>                                                                                       |
| [**XMMatrixIdentity**](xmmatrixidentity.md)<br/>                                             | Builds the identity matrix.<br/>                                                                                                 |
| [**XMMatrixInverse**](xmmatrixinverse.md)<br/>                                               | Computes the inverse of a matrix.<br/>                                                                                           |
| [**XMMatrixIsIdentity**](xmmatrixisidentity.md)<br/>                                         | Tests whether a matrix is the identity matrix.<br/>                                                                              |
| [**XMMatrixIsInfinite**](xmmatrixisinfinite.md)<br/>                                         | Tests whether any of the elements of a matrix are positive or negative infinity.<br/>                                            |
| [**XMMatrixIsNaN**](xmmatrixisnan.md)<br/>                                                   | Tests whether any of the elements of a matrix are NaN.<br/>                                                                      |
| [**XMMatrixLookAtLH**](xmmatrixlookatlh.md)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a focal point.<br/>       |
| [**XMMatrixLookAtRH**](xmmatrixlookatrh.md)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a focal point.<br/>      |
| [**XMMatrixLookToLH**](xmmatrixlooktolh.md)<br/>                                             | Builds a view matrix for a left-handed coordinate system using a camera position, an up direction, and a camera direction.<br/>  |
| [**XMMatrixLookToRH**](xmmatrixlooktorh.md)<br/>                                             | Builds a view matrix for a right-handed coordinate system using a camera position, an up direction, and a camera direction.<br/> |
| [**XMMatrixMultiply**](xmmatrixmultiply.md)<br/>                                             | Computes the product of two matrices.<br/>                                                                                       |
| [**XMMatrixMultiplyTranspose**](xmmatrixmultiplytranspose.md)<br/>                           | Computes the transpose of the product of two matrices.<br/>                                                                      |
| [**XMMatrixOrthographicLH**](xmmatrixorthographiclh.md)<br/>                                 | Builds an orthogonal projection matrix for a left-handed coordinate system.<br/>                                                 |
| [**XMMatrixOrthographicOffCenterLH**](xmmatrixorthographicoffcenterlh.md)<br/>               | Builds a custom orthogonal projection matrix for a left-handed coordinate system.<br/>                                           |
| [**XMMatrixOrthographicOffCenterRH**](xmmatrixorthographicoffcenterrh.md)<br/>               | Builds a custom orthogonal projection matrix for a right-handed coordinate system.<br/>                                          |
| [**XMMatrixOrthographicRH**](xmmatrixorthographicrh.md)<br/>                                 | Builds an orthogonal projection matrix for a right-handed coordinate system.<br/>                                                |
| [**XMMatrixPerspectiveFovLH**](xmmatrixperspectivefovlh.md)<br/>                             | Builds a left-handed perspective projection matrix based on a field of view.<br/>                                                |
| [**XMMatrixPerspectiveFovRH**](xmmatrixperspectivefovrh.md)<br/>                             | Builds a right-handed perspective projection matrix based on a field of view.<br/>                                               |
| [**XMMatrixPerspectiveLH**](xmmatrixperspectivelh.md)<br/>                                   | Builds a left-handed perspective projection matrix.<br/>                                                                         |
| [**XMMatrixPerspectiveOffCenterLH**](xmmatrixperspectiveoffcenterlh.md)<br/>                 | Builds a custom version of a left-handed perspective projection matrix.<br/>                                                     |
| [**XMMatrixPerspectiveOffCenterRH**](xmmatrixperspectiveoffcenterrh.md)<br/>                 | Builds a custom version of a right-handed perspective projection matrix.<br/>                                                    |
| [**XMMatrixPerspectiveRH**](xmmatrixperspectiverh.md)<br/>                                   | Builds a right-handed perspective projection matrix.<br/>                                                                        |
| [**XMMatrixReflect**](xmmatrixreflect.md)<br/>                                               | Builds a transformation matrix designed to reflect vectors through a given plane.<br/>                                           |
| [**XMMatrixRotationAxis**](xmmatrixrotationaxis.md)<br/>                                     | Builds a matrix that rotates around an arbitrary axis.<br/>                                                                      |
| [**XMMatrixRotationNormal**](xmmatrixrotationnormal.md)<br/>                                 | Builds a matrix that rotates around an arbitrary normal vector.<br/>                                                             |
| [**XMMatrixRotationQuaternion**](xmmatrixrotationquaternion.md)<br/>                         | Builds a rotation matrix from a quaternion.<br/>                                                                                 |
| [**XMMatrixRotationRollPitchYaw**](xmmatrixrotationrollpitchyaw.md)<br/>                     | Builds a rotation matrix based on a given pitch, yaw, and roll (Euler angles).<br/>                                              |
| [**XMMatrixRotationRollPitchYawFromVector**](xmmatrixrotationrollpitchyawfromvector.md)<br/> | Builds a rotation matrix based on a vector containing the Euler angles (pitch, yaw, and roll).<br/>                              |
| [**XMMatrixRotationX**](xmmatrixrotationx.md)<br/>                                           | Builds a matrix that rotates around the x-axis.<br/>                                                                             |
| [**XMMatrixRotationY**](xmmatrixrotationy.md)<br/>                                           | Builds a matrix that rotates around the y-axis.<br/>                                                                             |
| [**XMMatrixRotationZ**](xmmatrixrotationz.md)<br/>                                           | Builds a matrix that rotates around the z-axis.<br/>                                                                             |
| [**XMMatrixScaling**](xmmatrixscaling.md)<br/>                                               | Builds a matrix that scales along the x-axis, y-axis, and z-axis.<br/>                                                           |
| [**XMMatrixScalingFromVector**](xmmatrixscalingfromvector.md)<br/>                           | Builds a scaling matrix from a 3D vector.<br/>                                                                                   |
| [**XMMatrixSet**](xmmatrixset.md)<br/>                                                       | Creates a matrix with **float** values.<br/>                                                                                     |
| [**XMMatrixShadow**](xmmatrixshadow.md)<br/>                                                 | Builds a transformation matrix that flattens geometry into a plane.<br/>                                                         |
| [**XMMatrixTransformation**](xmmatrixtransformation.md)<br/>                                 | Builds a transformation matrix.<br/>                                                                                             |
| [**XMMatrixTransformation2D**](xmmatrixtransformation2d.md)<br/>                             | Builds a 2D transformation matrix in the xy plane.<br/>                                                                          |
| [**XMMatrixTranslation**](xmmatrixtranslation.md)<br/>                                       | Builds a translation matrix from the specified offsets.<br/>                                                                     |
| [**XMMatrixTranslationFromVector**](xmmatrixtranslationfromvector.md)<br/>                   | Builds a translation matrix from a vector.<br/>                                                                                  |
| [**XMMatrixTranspose**](xmmatrixtranspose.md)<br/>                                           | Computes the transpose of a matrix.<br/>                                                                                         |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 




