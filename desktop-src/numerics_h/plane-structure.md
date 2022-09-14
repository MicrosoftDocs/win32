---
title: plane structure (Windowsnumerics.h)
description: This structure represents a plane using a 3D vector normal and a distance value.
ms.assetid: 3C5A5EA0-8A51-4F9B-A84A-0C8E726CE3FD
keywords:
- plane structure
topic_type:
- apiref
api_name:
- plane structure
api_location:
- windowsnumerics.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# plane structure

This structure represents a plane using a 3D vector normal and a distance value.

This type is available only in C++. Its .NET equivalent is [System.Numerics.Plane](/dotnet/api/system.numerics.plane).

## Constructors

| Name | Description |
|-|-|
| `plane()` | Creates an uninitialized plane. |
| `plane(float x, float y, float z, float d)` | Creates a plane with the specified values. |
| `plane(float3 normal, float d)` | Creates a plane from a float3 and a distance. |
| `explicit plane(float4 value)` | Creates a plane from a float4. |
| `plane(Microsoft::?Graphics::?Canvas::?Numerics::?Plane const& value)` | Converts a **Microsoft.Graphics.Canvas.Numerics.Plane** to a plane. |

## Functions

| Name | Description |
|-|-|
| `plane make_plane_from_vertices(float3 const& point1, float3 const& point2, float3 const& point3)` | Creates a plane from a set of three vertex positions, which must all be different and not in a straight line. |
| `plane normalize(plane const& value)` | Changes the coefficients of the normal vector of a plane to make it of unit length. |
| `plane transform(plane const& plane, float4x4 const& matrix)` | Transforms a normalized plane by a matrix. |
| `plane transform(plane const& plane, quaternion const& rotation)` | Transforms a normalized plane by a quaternion rotation. |
| `float dot(plane const& plane, float4 const& value)` | Calculates the dot product of a plane with a vector. |
| `float dot_coordinate(plane const& plane, float3 const& value)` | Calculates the dot product of a plane with a float3 coordinate. Unlike dot\_normal, this computation includes the plane d value. |
| `float dot_normal(plane const& plane, float3 const& value)` | Calculates the dot product of a plane with a float3 normal. Unlike dot\_coordinate, this computation ignores the plane d value. |

## Operators

| Name | Description |
|-|-|
| `bool operator== (plane const& value1, plane const& value2)` | Determines whether two instances of plane are equal. |
| `bool operator!= (plane const& value1, plane const& value2)` | Determines whether two instances of plane are not equal. |
| `operator Microsoft::?Graphics::?Canvas::?Numerics::?Plane() const` | Converts a plane to a **Microsoft.Graphics.Canvas.Numerics.Plane**. |

## Fields

| Name | Description |
|-|-|
| `float3 normal` | Normal vector of the plane. |
| `float d` | Distance of the plane along its normal from the origin. |

## Requirements

| Requirement | Value |
|-|-|
| Namespace | Windows::Foundation::Numerics |
| Header | <dl> <dt>Windowsnumerics.h</dt> </dl> |

## See also

[windowsnumerics.h APIs](windowsnumerics-h-apis-portal.md)
