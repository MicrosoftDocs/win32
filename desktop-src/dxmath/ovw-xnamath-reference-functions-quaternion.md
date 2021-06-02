---
description: Lists the quaternion functions provided by DirectXMath.
ms.assetid: 2d397c98-d0cd-08e0-6104-cca31bb6bd11
title: DirectXMath Library quaternion functions
ms.topic: reference
ms.date: 05/31/2018
---

# DirectXMath Library quaternion functions

Lists the quaternion functions provided by DirectXMath.

## In this section



| Topic                                                                                                       | Description                                                                                                     |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**XMQuaternionBaryCentric**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionbarycentric)<br/>                                       | Returns a point in barycentric coordinates, using the specified quaternions.<br/>                         |
| [**XMQuaternionBaryCentricV**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionbarycentricv)<br/>                                     | Returns a point in barycentric coordinates, using the specified quaternions.<br/>                         |
| [**XMQuaternionConjugate**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionconjugate)<br/>                                           | Computes the conjugate of a quaternion.<br/>                                                              |
| [**XMQuaternionDot**](/windows/win32/api/directxmath/nf-directxmath-xmquaterniondot)<br/>                                                       | Computes the dot product of two quaternions.<br/>                                                         |
| [**XMQuaternionEqual**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionequal)<br/>                                                   | Tests whether two quaternions are equal.<br/>                                                             |
| [**XMQuaternionExp**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionexp)<br/>                                                       | Computes the exponential of a given pure quaternion.<br/>                                                 |
| [**XMQuaternionIdentity**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionidentity)<br/>                                             | Returns the identity quaternion.<br/>                                                                     |
| [**XMQuaternionInverse**](/windows/win32/api/directxmath/nf-directxmath-xmquaternioninverse)<br/>                                               | Computes the inverse of a quaternion.<br/>                                                                |
| [**XMQuaternionIsIdentity**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionisidentity)<br/>                                         | Tests whether a specific quaternion is the identity quaternion.<br/>                                      |
| [**XMQuaternionIsInfinite**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionisinfinite)<br/>                                         | Test whether any component of a quaternion is either positive or negative infinity.<br/>                  |
| [**XMQuaternionIsNaN**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionisnan)<br/>                                                   | Test whether any component of a quaternion is a NaN.<br/>                                                 |
| [**XMQuaternionLength**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionlength)<br/>                                                 | Computes the magnitude of a quaternion.<br/>                                                              |
| [**XMQuaternionLengthSq**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionlengthsq)<br/>                                             | Computes the square of the magnitude of a quaternion.<br/>                                                |
| [**XMQuaternionLn**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionln)<br/>                                                         | Computes the natural logarithm of a given unit quaternion.<br/>                                           |
| [**XMQuaternionMultiply**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionmultiply)<br/>                                             | Computes the product of two quaternions.<br/>                                                             |
| [**XMQuaternionNormalize**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionnormalize)<br/>                                           | Normalizes a quaternion.<br/>                                                                             |
| [**XMQuaternionNormalizeEst**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionnormalizeest)<br/>                                     | Estimates the normalized version of a quaternion.<br/>                                                    |
| [**XMQuaternionNotEqual**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionnotequal)<br/>                                             | Tests whether two quaternions are not equal.<br/>                                                         |
| [**XMQuaternionReciprocalLength**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionreciprocallength)<br/>                             | Computes the reciprocal of the magnitude of a quaternion.<br/>                                            |
| [**XMQuaternionRotationAxis**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionrotationaxis)<br/>                                     | Computes a rotation quaternion about an axis.<br/>                                                        |
| [**XMQuaternionRotationMatrix**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionrotationmatrix)<br/>                                 | Computes a rotation quaternion from a rotation matrix.<br/>                                               |
| [**XMQuaternionRotationNormal**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionrotationnormal)<br/>                                 | Computes the rotation quaternion about a normal vector.<br/>                                              |
| [**XMQuaternionRotationRollPitchYaw**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionrotationrollpitchyaw)<br/>                     | Computes a rotation quaternion based on the pitch, yaw, and roll (Euler angles).<br/>                     |
| [**XMQuaternionRotationRollPitchYawFromVector**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionrotationrollpitchyawfromvector)<br/> | Computes a rotation quaternion based on a vector containing the Euler angles (pitch, yaw, and roll).<br/> |
| [**XMQuaternionSlerp**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionslerp)<br/>                                                   | Interpolates between two unit quaternions, using spherical linear interpolation.<br/>                     |
| [**XMQuaternionSlerpV**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionslerpv)<br/>                                                 | Interpolates between two unit quaternions, using spherical linear interpolation.<br/>                     |
| [**XMQuaternionSquad**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionsquad)<br/>                                                   | Interpolates between four unit quaternions, using spherical quadrangle interpolation.<br/>                |
| [**XMQuaternionSquadSetup**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionsquadsetup)<br/>                                         | Provides addresses of setup control points for spherical quadrangle interpolation.<br/>                   |
| [**XMQuaternionSquadV**](/windows/win32/api/directxmath/nf-directxmath-xmquaternionsquadv)<br/>                                                 | Interpolates between four unit quaternions, using spherical quadrangle interpolation.<br/>                |
| [**XMQuaternionToAxisAngle**](/windows/win32/api/directxmath/nf-directxmath-xmquaterniontoaxisangle)<br/>                                       | Computes an axis and angle of rotation about that axis for a given quaternion.<br/>                       |



 

## Related topics

<dl> <dt>

[DirectXMath Library Functions](ovw-xnamath-reference-functions.md)
</dt> </dl>

 

 
