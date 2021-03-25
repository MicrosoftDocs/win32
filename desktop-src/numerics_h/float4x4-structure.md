---
title: float4x4 structure (Windowsnumerics.h)
description: A 4x4 matrix, used for 3D transforms.
ms.assetid: C0D2198A-B547-4153-AD02-9A47835FD272
keywords:
- float4x4 structure
topic_type:
- apiref
api_name:
- float4x4 structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# float4x4 structure

A 4x4 matrix, used for 3D transforms.

This matrix type uses a row vector layout. The x, y, and z of this matrix's translation vector correspond to the fields m41, m42, m43.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Matrix4x4](/dotnet/api/system.numerics.matrix4x4?view=netframework-4.8).

## Constructors

| Name | Description |
|-|-|
| `float4x4()` | Creates an uninitialized float4x4. |
| `float4x4(float m11, float m12, float m13, float m14, float m21, float m22, float m23, float m24, float m31, float m32, float m33, float m34, float m41, float m42, float m43, float m44)` | Creates a float4x4 with the specified values. |
| `explicit float4x4(float3x2 value)` | Creates a float4x4 from a float3x2. |
| `float4x4(Microsoft::?Graphics::?Canvas::?Numerics::?Matrix4x4 const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Matrix4x4** to a float4x4. |

## Functions

| Name | Description |
|-|-|
| `float4x4 make_float4x4_billboard(float3 const& objectPosition, float3 const& cameraPosition, float3 const& cameraUpVector, float3 const& cameraForwardVector)` | Creates a spherical billboard that rotates around a specified object position, using a right handed coordinate system. |
| `float4x4 make_float4x4_?constrained_billboard(float3 const& objectPosition, float3 const& cameraPosition, float3 const& rotateAxis, float3 const& cameraForwardVector, float3 const& objectForwardVector)` | Creates a cylindrical billboard that rotates around a specified axis, using a right handed coordinate system. |
| `float4x4 make_float4x4_translation(float3 const& position)` | Creates a translation matrix. |
| `float4x4 make_float4x4_translation(float xPosition, float yPosition, float zPosition)` | Creates a translation matrix. |
| `float4x4 make_float4x4_scale(float xScale, float yScale, float zScale)` | Creates a scaling matrix, centered on the origin. |
| `float4x4 make_float4x4_scale(float xScale, float yScale, float zScale, float3 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float4x4 make_float4x4_scale(float3 const& scales)` | Creates a scaling matrix, centered on the origin. |
| `float4x4 make_float4x4_scale(float3 const& scales, float3 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float4x4 make_float4x4_scale(float scale)` | Creates a scaling matrix, centered on the origin. |
| `float4x4 make_float4x4_scale(float scale, float3 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float4x4 make_float4x4_rotation_x(float radians)` | Creates an x-axis rotation matrix, centered on the origin. |
| `float4x4 make_float4x4_rotation_x(float radians, float3 const& centerPoint)` | Creates an x-axis rotation matrix, centered on the specified point. |
| `float4x4 make_float4x4_rotation_y(float radians)` | Creates a y-axis rotation matrix, centered on the origin. |
| `float4x4 make_float4x4_rotation_y(float radians, float3 const& centerPoint)` | Creates a y-axis rotation matrix, centered on the specified point. |
| `float4x4 make_float4x4_rotation_z(float radians)` | Creates a z-axis rotation matrix, centered on the origin. |
| `float4x4 make_float4x4_rotation_z(float radians, float3 const& centerPoint)` | Creates a z-axis rotation matrix, centered on the specified point. |
| `float4x4 make_float4x4_from_axis_angle(float3 const& axis, float angle)` | Creates a matrix that rotates around an arbitrary vector. |
| `float4x4 make_float4x4_?perspective_field_of_view(float fieldOfView, float aspectRatio, float nearPlaneDistance, float farPlaneDistance)` | Creates a perspective projection matrix based on a field of view, using a right handed coordinate system. |
| `float4x4 make_float4x4_perspective(float width, float height, float nearPlaneDistance, float farPlaneDistance)` | Creates a perspective projection matrix, using a right handed coordinate system. |
| `float4x4 make_float4x4_?perspective_off_center(float left, float right, float bottom, float top, float nearPlaneDistance, float farPlaneDistance)` | Creates a customized perspective projection matrix, using a right handed coordinate system. |
| `float4x4 make_float4x4_orthographic(float width, float height, float zNearPlane, float zFarPlane)` | Creates an orthographic projection matrix, using a right handed coordinate system. |
| `float4x4 make_float4x4_?orthographic_off_center(float left, float right, float bottom, float top, float zNearPlane, float zFarPlane)` | Creates a customized orthographic projection matrix, using a right handed coordinate system. |
| `float4x4 make_float4x4_look_at(float3 const& cameraPosition, float3 const& cameraTarget, float3 const& cameraUpVector)` | Creates a view matrix, using a right handed coordinate system. |
| `float4x4 make_float4x4_world(float3 const& position, float3 const& forward, float3 const& up)` | Creates a world matrix, using a right handed coordinate system. This can be used to position objects in 3D space. |
| `float4x4 make_float4x4_?from_quaternion(quaternion const& quaternion)` | Creates a rotation matrix from a quaternion. |
| `float4x4 make_float4x4_?from_yaw_pitch_roll(float yaw, float pitch, float roll)` | Creates a rotation matrix from a specified yaw, pitch, and roll. |
| `float4x4 make_float4x4_shadow(float3 const& lightDirection, plane const& plane)` | Creates a matrix that flattens geometry into a specified plane as if casting a shadow from a specified light source. |
| `float4x4 make_float4x4_reflection(plane const& value)` | Creates a matrix that reflects the coordinate system about a specified plane. |
| `bool is_identity(float4x4 const& value)` | Checks whether this is an identity matrix. |
| `float determinant(float4x4 const& value)` | Calculates the determinant of the matrix. |
| `float3 translation(float4x4 const& value)` | Gets the translation vector of the matrix. |
| `bool invert(float4x4 const& matrix, _Out_ float4x4* result)` | Calculates the inverse of a matrix. Returns true if the matrix can be inverted; false otherwise. |
| `bool decompose(float4x4 const& matrix, _Out_ float3* scale, _Out_ quaternion* rotation, _Out_ float3* translation)` | Extracts the scalar, translation, and rotation components from a 3D scale/rotate/translate (SRT) matrix. Returns true if the matrix can be decomposed; false otherwise. |
| `float4x4 transform(float4x4 const& value, quaternion const& rotation)` | Transforms a matrix by applying a quaternion rotation. |
| `float4x4 transpose(float4x4 const& matrix)` | Transposes the components of a matrix along its diagonal. |
| `float4x4 lerp(float4x4 const& matrix1, float4x4 const& matrix2, float amount)` | Linearly interpolates between the corresponding values of two matrices. |

## Methods

| Name | Description |
|-|-|
| `static float4x4 identity()` | Returns an instance of the identity matrix. |

## Operators

| Name | Description |
|-|-|
| `float4x4 operator+ (float4x4 const& value1, float4x4 const& value2)` | Adds each component of a matrix to another matrix. |
| `float4x4 operator- (float4x4 const& value1, float4x4 const& value2)` | Subtracts each component of a matrix from another matrix. |
| `float4x4 operator* (float4x4 const& value1, float4x4 const& value2)` | Multiplies a matrix by another matrix. This has the effect of concatenating two transforms. |
| `float4x4 operator* (float4x4 const& value1, float value2)` | Multiplies each component of a matrix by a scalar value. |
| `float4x4 operator- (float4x4 const& value)` | Negates each component of a matrix. |
| `float4x4& operator+= (float4x4& value1, float4x4 const& value2)` | In-place adds each component of a matrix to another matrix. |
| `float4x4& operator-= (float4x4& value1, float4x4 const& value2)` | In-place subtracts each component of a matrix from another matrix. |
| `float4x4& operator*= (float4x4& value1, float4x4 const& value2)` | In-place multiplies a matrix by another matrix. This has the effect of concatenating two transforms. |
| `float4x4& operator*= (float4x4& value1, float value2)` | In-place multiplies each component of a matrix by a scalar value. |
| `bool operator== (float4x4 const& value1, float4x4 const& value2)` | Determines whether two instances of float4x4 are equal. |
| `bool operator!= (float4x4 const& value1, float4x4 const& value2)` | Determines whether two instances of float4x4 are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Matrix4x4() const` | Converts a float4x4 to a **Microsoft.Graphics.Canvas.Numerics.Matrix4x4**. |

## Fields

| Name | Description |
|-|-|
| `float m11` | Value at row 1 column 1 of the matrix. |
| `float m12` | Value at row 1 column 2 of the matrix. |
| `float m13` | Value at row 1 column 3 of the matrix. |
| `float m14` | Value at row 1 column 4 of the matrix. |
| `float m21` | Value at row 2 column 1 of the matrix. |
| `float m22` | Value at row 2 column 2 of the matrix. |
| `float m23` | Value at row 2 column 3 of the matrix. |
| `float m24` | Value at row 2 column 4 of the matrix. |
| `float m31` | Value at row 3 column 1 of the matrix. |
| `float m32` | Value at row 3 column 2 of the matrix. |
| `float m33` | Value at row 3 column 3 of the matrix. |
| `float m34` | Value at row 3 column 4 of the matrix. |
| `float m41` | Value at row 4 column 1 of the matrix. |
| `float m42` | Value at row 4 column 2 of the matrix. |
| `float m43` | Value at row 4 column 3 of the matrix. |
| `float m44` | Value at row 4 column 4 of the matrix. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
