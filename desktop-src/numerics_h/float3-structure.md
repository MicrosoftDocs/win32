---
title: float3 structure (Windowsnumerics.h)
description: A vector with three components.
ms.assetid: CAA10ADA-C5A8-4B75-A0A9-5C5B3FDD9A07
keywords:
- float3 structure
topic_type:
- apiref
api_name:
- float3 structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# float3 structure

A vector with three components.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Vector3](/dotnet/api/system.numerics.vector3?view=netframework-4.8).

## Constructors

| Name | Description |
|-|-|
| `float3()` | Creates an uninitialized float3. |
| `float3(float x, float y, float z)` | Creates a float3 with the specified values. |
| `float3(float2 value, float z)` | Creates a float3 with x and y copied from a float2 plus the specified z value. |
| `explicit float3(float value)` | Creates a float3 with all components set to the specified value. |
| `float3(Microsoft::Graphics::Canvas::Numerics::Vector3 const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Vector3** to a float3. |

## Functions

| Name | Description |
|-|-|
| `float length(float3 const& value)` | Calculates the length, or Euclidean distance, of the vector. |
| `float length_squared(float3 const& value)` | Calculates the length, or Euclidean distance, of the vector squared. |
| `float distance(float3 const& value1, float3 const& value2)` | Calculates the Euclidean distance between two vectors. |
| `float distance_squared(float3 const& value1, float3 const& value2)` | Calculates the Euclidean distance between two vectors squared. |
| `float dot(float3 const& vector1, float3 const& vector2)` | Calculates the dot product of two vectors. |
| `float3 normalize(float3 const& value)` | Creates a unit vector from the specified vector. |
| `float3 cross(float3 const& vector1, float3 const& vector2)` | Calculates the cross product of two vectors. |
| `float3 reflect(float3 const& vector, float3 const& normal)` | Determines the reflect vector of the given vector and normal. |
| `float3 min(float3 const& value1, float3 const& value2)` | Returns a vector that contains the lowest value from each matching pair of components. |
| `float3 max(float3 const& value1, float3 const& value2)` | Returns a vector that contains the highest value from each matching pair of components. |
| `float3 clamp(float3 const& value1, float3 const& min, float3 const& max)` | Restricts a value to be within a specified range. |
| `float3 lerp(float3 const& value1, float3 const& value2, float amount)` | Performs a linear interpolation between two vectors. |
| `float3 transform(float3 const& position, float4x4 const& matrix)` | Transforms the vector (x, y, z, 1) by the specified matrix. |
| `float3 transform_normal(float3 const& normal, float4x4 const& matrix)` | Transforms the normal vector (x, y, z, 0) by the specified matrix. |
| `float3 transform(float3 const& value, quaternion const& rotation)` | Transforms a float3 by the given quaternion. |

## Methods

| Name | Description |
|-|-|
| `static float3 zero()` | Returns a float3 with all of its components set to zero. |
| `static float3 one()` | Returns a float3 with all of its components set to one. |
| `static float3 unit_x()` | Returns the float3 (1, 0, 0). |
| `static float3 unit_y()` | Returns the float3 (0, 1, 0). |
| `static float3 unit_z()` | Returns the float3 (0, 0, 1). |

## Operators

| Name | Description |
|-|-|
| `float3 operator+ (float3 const& value1, float3 const& value2)` | Adds two vectors. |
| `float3 operator- (float3 const& value1, float3 const& value2)` | Subtracts a vector from a vector. |
| `float3 operator* (float3 const& value1, float3 const& value2)` | Multiplies the components of two vectors by each other. |
| `float3 operator* (float3 const& value1, float value2)` | Multiplies a vector by a scalar. |
| `float3 operator* (float value1, float3 const& value2)` | Multiplies a vector by a scalar. |
| `float3 operator/ (float3 const& value1, float3 const& value2)` | Divides the components of a vector by the components of another vector. |
| `float3 operator/ (float3 const& value1, float value2)` | Divides a vector by a scalar value. |
| `float3 operator- (float3 const& value)` | Returns a vector pointing in the opposite direction. |
| `float3& operator+= (float3& value1, float3 const& value2)` | In-place adds two vectors. |
| `float3& operator-= (float3& value1, float3 const& value2)` | In-place subtracts a vector from a vector. |
| `float3& operator*= (float3& value1, float3 const& value2)` | In-place multiplies the components of two vectors by each other. |
| `float3& operator*= (float3& value1, float value2)` | In-place multiplies a vector by a scalar. |
| `float3& operator/= (float3& value1, float3 const& value2)` | In-place divides the components of a vector by the components of another vector. |
| `float3& operator/= (float3& value1, float value2)` | In-place divides a vector by a scalar value. |
| `bool operator== (float3 const& value1, float3 const& value2)` | Determines whether two instances of float3 are equal. |
| `bool operator!= (float3 const& value1, float3 const& value2)` | Determines whether two instances of float3 are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Vector3() const` | Converts a float3 to a **Microsoft.Graphics.Canvas.Numerics.Vector3**. |

## Fields

| Name | Description |
|-|-|
| `float x` | X component of the vector. |
| `float y` | Y component of the vector. |
| `float z` | Z component of the vector. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
