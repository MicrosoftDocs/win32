---
title: quaternion structure (Windowsnumerics.h)
description: A four dimensional vector, used to represent a rotation.
ms.assetid: A6B25885-8ECB-4039-9DC6-41D5F3A02489
keywords:
- quaternion structure
topic_type:
- apiref
api_name:
- quaternion structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# quaternion Structure

A four dimensional vector, used to represent a rotation.

A quaternion can efficiently rotate an object about the (x, y, z) vector by the angle theta, where w = cos(theta/2). Quaternions are typically used for smooth interpolation between two angles, and for avoiding the gimbal lock problem that can occur with Euler angles.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Quaternion](/dotnet/api/system.numerics.quaternion?view=netframework-4.8).

## Constructors

| Name | Description |
|-|-|
| `quaternion()` | Creates an uninitialized quaternion. |
| `quaternion(float x, float y, float z, float w)` | Creates a quaternion with the specified values. |
| `quaternion(float3 vectorPart, float scalarPart)` | Creates a quaternion from a float3 and scalar. |
| `quaternion(Microsoft::?Graphics::?Canvas::?Numerics::?Quaternion const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Quaternion** to a quaternion. |

## Functions

| Name | Description |
|-|-|
| `quaternion make_quaternion_from_axis_angle(float3 const& axis, float angle)` | Creates a quaternion from a vector and an angle to rotate about the vector. |
| `quaternion make_quaternion_from_yaw_pitch_roll(float yaw, float pitch, float roll)` | Creates a quaternion from specified yaw, pitch, and roll angles. |
| `quaternion make_quaternion_from_rotation_matrix(float4x4 const& matrix)` | Creates a quaternion from a rotation matrix. |
| `bool is_identity(quaternion const& value)` | Checks whether this is an identity (no rotation) quaternion. |
| `float length(quaternion const& value)` | Calculates the length of a quaternion. |
| `float length_squared(quaternion const& value)` | Calculates the length squared of a quaternion. |
| `float dot(quaternion const& quaternion1, quaternion const& quaternion2)` | Calculates the dot product of two quaternions. |
| `quaternion normalize(quaternion const& value)` | Divides each component of a quaternion by the length of the quaternion. |
| `quaternion conjugate(quaternion const& value)` | Calculates the conjugate of a quaternion. |
| `quaternion inverse(quaternion const& value)` | Calculates the inverse of a quaternion. |
| `quaternion slerp(quaternion const& quaternion1, quaternion const& quaternion2, float amount)` | Interpolates between two quaternions, using spherical linear interpolation. |
| `quaternion lerp(quaternion const& quaternion1, quaternion const& quaternion2, float amount)` | Linearly interpolates between two quaternions. |
| `quaternion concatenate(quaternion const& value1, quaternion const& value2)` | Concatenates two quaternions; the result represents the first rotation followed by the second rotation. |

## Methods

| Name | Description |
|-|-|
| `static quaternion identity()` | Returns an instance of the identity quaternion. |

## Operators

| Name | Description |
|-|-|
| `quaternion operator+ (quaternion const& value1, quaternion const& value2)` | Adds two quaternions. |
| `quaternion operator- (quaternion const& value1, quaternion const& value2)` | Subtracts a quaternion from another quaternion. |
| `quaternion operator* (quaternion const& value1, quaternion const& value2)` | Multiplies a quaternion by another quaternion. |
| `quaternion operator* (quaternion const& value1, float value2)` | Multiplies a quaternion by a scalar value. |
| `quaternion operator/ (quaternion const& value1, quaternion const& value2)` | Divides a quaternion by another quaternion. |
| `quaternion operator- (quaternion const& value)` | Flips the sign of each component of the quaternion. |
| `quaternion& operator+= (quaternion& value1, quaternion const& value2)` | In-place adds two quaternions. |
| `quaternion& operator-= (quaternion& value1, quaternion const& value2)` | In-place subtracts a quaternion from another quaternion. |
| `quaternion& operator*= (quaternion& value1, quaternion const& value2)` | In-place multiplies a quaternion by another quaternion. |
| `quaternion& operator*= (quaternion& value1, float value2)` | In-place nultiplies a quaternion by a scalar value. |
| `quaternion& operator/= (quaternion& value1, quaternion const& value2)` | In-place divides a quaternion by another quaternion. |
| `bool operator== (quaternion const& value1, quaternion const& value2)` | Determines whether two instances of quaternion are equal. |
| `bool operator!= (quaternion const& value1, quaternion const& value2)` | Determines whether two instances of quaternion are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Quaternion() const` | Converts a quaternion to a **Microsoft.Graphics.Canvas.Numerics.Quaternion**. |

## Fields

| Name | Description |
|-|-|
| `float x` | X value of the vector component of the quaternion. |
| `float y` | Y value of the vector component of the quaternion. |
| `float z` | Z value of the vector component of the quaternion. |
| `float w` | Rotation component of the quaternion. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
