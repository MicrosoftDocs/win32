---
title: float4 structure (Windowsnumerics.h)
description: A vector with four components.
ms.assetid: AC07C6D0-E7FD-4582-B40D-4838F49FB8B4
keywords:
- float4 structure
topic_type:
- apiref
api_name:
- float4 structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# float4 structure

A vector with four components.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Vector4](/dotnet/api/system.numerics.vector4?view=netframework-4.8).

## Constructors

| Name | Description |
|-|-|
| `float4()` | Creates an uninitialized float4. |
| `float4(float x, float y, float z, float w)` | Creates a float4 with the specified values. |
| `float4(float2 value, float z, float w)` | Creates a float4 with x and y copied from a float2 plus the specified z and w values. |
| `float4(float3 value, float w)` | Creates a float4 with x, y and z copied from a float3 plus the specified w value. |
| `explicit float4(float value)` | Creates a float4 with all com.ents set to the specified value. |
| `float4(Microsoft::?Graphics::?Canvas::?Numerics::?Vector4 const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Vector4** to a float4. |

## Functions

| Name | Description |
|-|-|
| `float length(float4 const& value)` | Calculates the length, or Euclidean distance, of the vector. |
| `float length_squared(float4 const& value)` | Calculates the length, or Euclidean distance, of the vector squared. |
| `float distance(float4 const& value1, float4 const& value2)` | Calculates the Euclidean distance between two vectors. |
| `float distance_squared(float4 const& value1, float4 const& value2)` | Calculates the Euclidean distance between two vectors squared. |
| `float dot(float4 const& vector1, float4 const& vector2)` | Calculates the dot product of two vectors. |
| `float4 normalize(float4 const& vector)` | Creates a unit vector from the specified vector. |
| `float4 min(float4 const& value1, float4 const& value2)` | Returns a vector that contains the lowest value from each matching pair of components. |
| `float4 max(float4 const& value1, float4 const& value2)` | Returns a vector that contains the highest value from each matching pair of components. |
| `float4 clamp(float4 const& value1, float4 const& min, float4 const& max)` | Restricts a value to be within a specified range. |
| `float4 lerp(float4 const& value1, float4 const& value2, float amount)` | Performs a linear interpolation between two vectors. |
| `float4 transform(float4 const& vector, float4x4 const& matrix)` | Transforms a float4 by the given matrix. |
| `float4 transform4(float3 const& position, float4x4 const& matrix)` | Transforms a float3 by the given matrix, returning a float4. |
| `float4 transform4(float2 const& position, float4x4 const& matrix)` | Transforms a float2 by the given matrix, returning a float4. |
| `float4 transform(float4 const& value, quaternion const& rotation)` | Transforms a float4 by the given quaternion. |
| `float4 transform4(float3 const& value, quaternion const& rotation)` | Transforms a float3 by the given quaternion, returning a float4. |
| `float4 transform4(float2 const& value, quaternion const& rotation)` | Transforms a float2 by the given quaternion, returning a float4. |

## Methods

| Name | Description |
|-|-|
| `static float4 zero()` | Returns a float4 with all of its components set to zero. |
| `static float4 one()` | Returns a float4 with all of its components set to one. |
| `static float4 unit_x()` | Returns the float4 (1, 0, 0, 0). |
| `static float4 unit_y()` | Returns the float4 (0, 1, 0, 0). |
| `static float4 unit_z()` | Returns the float4 (0, 0, 1, 0). |
| `static float4 unit_w()` | Returns the float4 (0, 0, 0, 1). |

## Operators

| Name | Description |
|-|-|
| `float4 operator+ (float4 const& value1, float4 const& value2)` | Adds two vectors. |
| `float4 operator- (float4 const& value1, float4 const& value2)` | Subtracts a vector from a vector. |
| `float4 operator* (float4 const& value1, float4 const& value2)` | Multiplies the components of two vectors by each other. |
| `float4 operator* (float4 const& value1, float value2)` | Multiplies a vector by a scalar. |
| `float4 operator* (float value1, float4 const& value2)` | Multiplies a vector by a scalar. |
| `float4 operator/ (float4 const& value1, float4 const& value2)` | Divides the components of a vector by the components of another vector. |
| `float4 operator/ (float4 const& value1, float value2)` | Divides a vector by a scalar value. |
| `float4 operator- (float4 const& value)` | Returns a vector pointing in the opposite direction. |
| `float4& operator+= (float4& value1, float4 const& value2)` | In-place adds two vectors. |
| `float4& operator-= (float4& value1, float4 const& value2)` | In-place subtracts a vector from a vector. |
| `float4& operator*= (float4& value1, float4 const& value2)` | In-place multiplies the components of two vectors by each other. |
| `float4& operator*= (float4& value1, float value2)` | In-place multiplies a vector by a scalar. |
| `float4& operator/= (float4& value1, float4 const& value2)` | In-place divides the components of a vector by the components of another vector. |
| `float4& operator/= (float4& value1, float value2)` | In-place divides a vector by a scalar value. |
| `bool operator== (float4 const& value1, float4 const& value2)` | Determines whether two instances of float4 are equal. |
| `bool operator!= (float4 const& value1, float4 const& value2)` | Determines whether two instances of float4 are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Vector4() const` | Converts a float4 to a **Microsoft.Graphics.Canvas.Numerics.Vector4**. |

## Fields

| Name | Description |
|-|-|
| `float x` | X component of the vector. |
| `float y` | Y component of the vector. |
| `float z` | Z component of the vector. |
| `float w` | W component of the vector. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
