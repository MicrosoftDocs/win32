---
title: float2 structure (Windowsnumerics.h)
description: A vector with two components.
ms.assetid: 1A23C1E3-F34F-4249-80EA-92A13CD4B34F
keywords:
- float2 structure
topic_type:
- apiref
api_name:
- float2 structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# float2 structure

A vector with two components.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Vector2](/dotnet/api/system.numerics.vector2).

## Constructors

| Name | Description |
|-|-|
| `float2()` | Creates an uninitialized float2. |
| `float2(float x, float y)` | Creates a float2 with the specified values. |
| `explicit float2(float value)` | Creates a float2 with all components set to the specified value. |
| `float2(Microsoft::Graphics::Canvas::Numerics::Vector2 const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Vector2** to a float2. |
| `float2(Windows::Foundation::Point const& value)` | Converts a [**Windows.Foundation.Point**](/uwp/api/Windows.Foundation.Point) to a float2. |
| `float2(Windows::Foundation::Size const& value)` | Converts a [**Windows.Foundation.Size**](/uwp/api/Windows.Foundation.Size) to a float2. |

## Functions

| Name | Description |
|-|-|
| `float length(float2 const& value)` | Calculates the length, or Euclidean distance, of the vector. |
| `float length_squared(float2 const& value)` | Calculates the length, or Euclidean distance, of the vector squared. |
| `float distance(float2 const& value1, float2 const& value2)` | Calculates the Euclidean distance between two vectors. |
| `float distance_squared(float2 const& value1, float2 const& value2)` | Calculates the Euclidean distance between two vectors squared. |
| `float dot(float2 const& value1, float2 const& value2)` | Calculates the dot product of two vectors. |
| `float2 normalize(float2 const& value)` | Creates a unit vector from the specified vector. |
| `float2 reflect(float2 const& vector, float2 const& normal)` | Determines the reflect vector of the given vector and normal. |
| `float2 min(float2 const& value1, float2 const& value2)` | Returns a vector that contains the lowest value from each matching pair of components. |
| `float2 max(float2 const& value1, float2 const& value2)` | Returns a vector that contains the highest value from each matching pair of components. |
| `float2 clamp(float2 const& value1, float2 const& min, float2 const& max)` | Restricts a value to be within a specified range. |
| `float2 lerp(float2 const& value1, float2 const& value2, float amount)` | Performs a linear interpolation between two vectors. |
| `float2 transform(float2 const& position, float3x2 const& matrix)` | Transforms the vector (x, y, 0, 1) by the specified matrix. |
| `float2 transform(float2 const& position, float4x4 const& matrix)` | Transforms the vector (x, y, 0, 1) by the specified matrix. |
| `float2 transform_normal(float2 const& normal, float3x2 const& matrix)` | Transforms the normal vector (x, y, 0, 0) by the specified matrix. |
| `float2 transform_normal(float2 const& normal, float4x4 const& matrix)` | Transforms the normal vector (x, y, 0, 0) by the specified matrix. |
| `float2 transform(float2 const& value, quaternion const& rotation)` | Transforms a float2 by the given quaternion. |

## Methods

| Name | Description |
|-|-|
| `static float2 zero()` | Returns a float2 with all of its components set to zero. |
| `static float2 one()` | Returns a float2 with all of its components set to one. |
| `static float2 unit_x()` | Returns the float2 (1, 0). |
| `static float2 unit_y()` | Returns the float2 (0, 1). |

## Operators

| Name | Description |
|-|-|
| `operator Windows::Foundation::Point() const` | Converts a float2 to a [**Windows.Foundation.Point**](/uwp/api/Windows.Foundation.Point). |
| `operator Windows::Foundation::Size() const` | Converts a float2 to a [**Windows.Foundation.Size**](/uwp/api/Windows.Foundation.Size). |
| `float2 operator+ (float2 const& value1, float2 const& value2)` | Adds two vectors. |
| `float2 operator- (float2 const& value1, float2 const& value2)` | Subtracts a vector from a vector. |
| `float2 operator* (float2 const& value1, float2 const& value2)` | Multiplies the components of two vectors by each other. |
| `float2 operator* (float2 const& value1, float value2)` | Multiplies a vector by a scalar. |
| `float2 operator* (float value1, float2 const& value2)` | Multiplies a vector by a scalar. |
| `float2 operator/ (float2 const& value1, float2 const& value2)` | Divides the components of a vector by the components of another vector. |
| `float2 operator/ (float2 const& value1, float value2)` | Divides a vector by a scalar value. |
| `float2 operator- (float2 const& value)` | Returns a vector pointing in the opposite direction. |
| `float2& operator+= (float2& value1, float2 const& value2)` | In-place adds two vectors. |
| `float2& operator-= (float2& value1, float2 const& value2)` | In-place subtracts a vector from a vector. |
| `float2& operator*= (float2& value1, float2 const& value2)` | In-place multiplies the components of two vectors by each other. |
| `float2& operator*= (float2& value1, float value2)` | In-place multiplies a vector by a scalar. |
| `float2& operator/= (float2& value1, float2 const& value2)` | In-place divides the components of a vector by the components of another vector. |
| `float2& operator/= (float2& value1, float value2)` | In-place divides a vector by a scalar value. |
| `bool operator== (float2 const& value1, float2 const& value2)` | Determines whether two instances of float2 are equal. |
| `bool operator!= (float2 const& value1, float2 const& value2)` | Determines whether two instances of float2 are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Vector2() const` | Converts a float2 to a **Microsoft.Graphics.Canvas.Numerics.Vector2**. |

## Fields

| Name | Description |
|-|-|
| `float x` | X component of the vector. |
| `float y` | Y component of the vector. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
