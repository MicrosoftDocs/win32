---
title: float3x2 structure (Windowsnumerics.h)
description: A 3x2 matrix, used for 2D transforms.
ms.assetid: 5C2A4C30-3EC4-4DE9-A42A-6A19F96F8D69
keywords:
- float3x2 structure
topic_type:
- apiref
api_name:
- float3x2 structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# float3x2 structure

A 3x2 matrix, used for 2D transforms.

This matrix type uses a row vector layout. The x and y of this matrix's translation vector correspond to the fields m31, m32.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Matrix3x2](/dotnet/api/system.numerics.matrix3x2?view=netframework-4.8).

## Constructors

| Name | Description |
|-|-|
| `float3x2()` | Creates an uninitialized float3x2. |
| `float3x2(float m11, float m12, float m21, float m22, float m31, float m32)` | Creates a float3x2 with the specified values. |
| `float3x2(Microsoft::?Graphics::?Canvas::?Numerics::?Matrix3x2 const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Matrix3x2** to a float3x2. |

## Functions

| Name | Description |
|-|-|
| `float3x2 make_float3x2_translation(float2 const& position)` | Creates a translation matrix. |
| `float3x2 make_float3x2_translation(float xPosition, float yPosition)` | Creates a translation matrix. |
| `float3x2 make_float3x2_scale(float xScale, float yScale)` | Creates a scaling matrix, centered on the origin. |
| `float3x2 make_float3x2_scale(float xScale, float yScale, float2 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float3x2 make_float3x2_scale(float2 const& scales)` | Creates a scaling matrix, centered on the origin. |
| `float3x2 make_float3x2_scale(float2 const& scales, float2 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float3x2 make_float3x2_scale(float scale)` | Creates a scaling matrix, centered on the origin. |
| `float3x2 make_float3x2_scale(float scale, float2 const& centerPoint)` | Creates a scaling matrix, centered on the specified point. |
| `float3x2 make_float3x2_skew(float radiansX, float radiansY)` | Creates a skew matrix, centered on the origin. |
| `float3x2 make_float3x2_skew(float radiansX, float radiansY, float2 const& centerPoint)` | Creates a skew matrix, centered on the specified point. |
| `float3x2 make_float3x2_rotation(float radians)` | Creates a rotation matrix, centered on the origin. |
| `float3x2 make_float3x2_rotation(float radians, float2 const& centerPoint)` | Creates a rotation matrix, centered on the specified point. |
| `bool is_identity(float3x2 const& value)` | Checks whether this is an identity matrix. |
| `float determinant(float3x2 const& value)` | Calculates the determinant of the matrix. |
| `float2 translation(float3x2 const& value)` | Gets the translation vector of the matrix. |
| `bool invert(float3x2 const& matrix, _Out_ float3x2* result)` | Calculates the inverse of a matrix. Returns true if the matrix can be inverted; false otherwise. |
| `float3x2 lerp(float3x2 const& matrix1, float3x2 const& matrix2, float amount)` | Linearly interpolates between the corresponding values of two matrices. |

## Methods

| Name | Description |
|-|-|
| `static float3x2 identity()` | Returns an instance of the identity matrix. |

## Operators

| Name | Description |
|-|-|
| `float3x2 operator+ (float3x2 const& value1, float3x2 const& value2)` | Adds each component of a matrix to another matrix. |
| `float3x2 operator- (float3x2 const& value1, float3x2 const& value2)` | Subtracts each component of a matrix from another matrix. |
| `float3x2 operator* (float3x2 const& value1, float3x2 const& value2)` | Multiplies a matrix by another matrix. This has the effect of concatenating two transforms. |
| `float3x2 operator* (float3x2 const& value1, float value2)` | Multiplies each component of a matrix by a scalar value. |
| `float3x2 operator- (float3x2 const& value)` | Negates each component of a matrix. |
| `float3x2& operator+= (float3x2& value1, float3x2 const& value2)` | In-place adds each component of a matrix to another matrix. |
| `float3x2& operator-= (float3x2& value1, float3x2 const& value2)` | In-place subtracts each component of a matrix from another matrix. |
| `float3x2& operator*= (float3x2& value1, float3x2 const& value2)` | In-place multiplies a matrix by another matrix. This has the effect of concatenating two transforms. |
| `float3x2& operator*= (float3x2& value1, float value2)` | In-place multiplies each component of a matrix by a scalar value. |
| `bool operator== (float3x2 const& value1, float3x2 const& value2)` | Determines whether two instances of float3x2 are equal. |
| `bool operator!= (float3x2 const& value1, float3x2 const& value2)` | Determines whether two instances of float3x2 are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Matrix3x2() const` | Converts a float3x2 to a **Microsoft.Graphics.Canvas.Numerics.Matrix3x2**. |

## Fields

| Name | Description |
|-|-|
| `float m11` | Value at row 1 column 1 of the matrix. |
| `float m12` | Value at row 1 column 2 of the matrix. |
| `float m21` | Value at row 2 column 1 of the matrix. |
| `float m22` | Value at row 2 column 2 of the matrix. |
| `float m31` | Value at row 3 column 1 of the matrix. |
| `float m32` | Value at row 3 column 2 of the matrix. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
