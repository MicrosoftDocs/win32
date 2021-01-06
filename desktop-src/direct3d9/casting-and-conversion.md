---
description: When transferring values between the host application and an effect parameter, data is written as expected when the source data type (in the host application) matches the destination data type (in the effect parameter).
ms.assetid: 4f3ef14a-7d67-45fe-9282-541221815d1f
title: Casting and Conversion
ms.topic: article
ms.date: 05/31/2018
---

# Casting and Conversion

When transferring values between the host application and an effect parameter, data is written as expected when the source data type (in the host application) matches the destination data type (in the effect parameter). When the data types differ, casting will occur as the source data is rearranged to fit the destination.

DXSAS defines the following type conversion rules. These are a superset of the effect (.fx) and HLSL type conversion rules. DXSAS also defines some [Parameter Value Modifiers](#parameter-value-modifiers) that can affect the value being transferred from the host application to a bound parameter.

## Type Casting

The following table lists the casting that will occur when one data type is transferred to another data type:



| Source Type                                  | Destination Type                             | Behavior                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| float                                        | int                                          | Round towards zero.                                                                                                                                                                                                                                                                                                                                                                                      |
| float, int                                   | bool                                         | Values not equal to 0 - based on a not-equal-to comparison to 0 (int) or 0.0 (float) - are considered to be true, otherwise the value is considered to be false.                                                                                                                                                                                                                                         |
| int                                          | float                                        |                                                                                                                                                                                                                                                                                                                                                                                                          |
| bool                                         | int, float                                   | False is converted to zero.True is converted to one.                                                                                                                                                                                                                                                                                                                                                     |
| texture1D, texture2D, texture3D, textureCUBE | texture                                      | Destination texture is treated as the source texture type.                                                                                                                                                                                                                                                                                                                                               |
| string                                       | texture1D, texture2D, texture3D, textureCUBE | String value is treated as a resource address and resolved in the same way as the [Parameter Initialization Annotation](parameter-initialization-annotation.md). If the resource address cannot be resolved, the cast is invalid and the host applications must return an error. If the resource is resolved properly, the type of the expression is treated as the same type as the resolved resource. |



 

## Class Casting

In addition to the type casting rules described above, DXSAS defines the set of casting rules necessary to convert between class types. Column matrices (N x 1), row matrices (1 x N), and numeric structures are treated as vectors.

Effect matrix parameters and HLSL matrix variables can define whether the value is a row-major or column-major matrix; however, the DirectX APIs always treat [**D3DMATRIX**](d3dmatrix.md) and [**D3DXMATRIX**](d3dxmatrix.md) as row-major.



| Source Class | Destination Class | Behavior                                                                                                                                                                                                                                                                                                                                        |
|--------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scalar       | Scalar            | Apply Type Casting.                                                                                                                                                                                                                                                                                                                             |
| Scalar       | Vector            | Replicate the scalar source value into every component of the destination vector after applying the type casting and conversion behavior described in Type Casting.                                                                                                                                                                             |
| Scalar       | Matrix            | Replicate the scalar source value into every component of the destination matrix after applying the type casting and conversion behavior described in Type Casting.                                                                                                                                                                             |
| Scalar       | Object            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Scalar       | Structure         | Valid only if the destination structure contains only numeric elements. If valid, replicate the scalar source value into every component of the destination structure after applying the type casting and conversion behavior described in Type Casting.                                                                                        |
| Vector       | Scalar            | The destination scalar receives the value of the first component of the source vector after applying the type casting and conversion behavior described in [Type Casting](#type-casting).                                                                                                                                                       |
| Vector       | Vector            | Invalid cast if the destination vector has more components than the source vector. The destination vector receives the left-most values of the source vector after applying the type casting and conversion behavior described in [Type Casting](#type-casting). The remaining right-most components of the source vector are lost.             |
| Vector       | Matrix            | Invalid cast unless the source vector has the same number of components as the destination matrix. If the cast is valid, the behavior of the vector-to-vector cast is then applied.                                                                                                                                                             |
| Vector       | Object            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Vector       | Structure         | Valid only if the destination structure has only numeric elements and does not contain more elements than the source vector has components. The destination structure's elements receive the left-most components of the source vector after applying the type casting and conversion behavior described in [Type Casting](#type-casting).      |
| Matrix       | Scalar            | The destination scalar receives the value of the upper-left-most value of the source matrix after applying the type casting and conversion behavior described in [Type Casting](#type-casting).                                                                                                                                                 |
| Matrix       | Vector            | Invalid cast unless the source matrix has the same number of components as the destination vector. If the cast is valid, the behavior of the vector-to-vector cast above is then applied.                                                                                                                                                       |
| Matrix       | Matrix            | Invalid cast if the destination matrix has more components than the source matrix. The destination matrix receives the upper-left-most values of the source matrix after applying the type casting and conversion behavior described in [Type Casting](#type-casting). The remaining lower-right-most components of the source matrix are lost. |
| Matrix       | Object            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Matrix       | Structure         | The size of the structure must be equal to the size of the matrix and all components of the structure must be numeric.                                                                                                                                                                                                                          |
| Object       | Scalar            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Object       | Vector            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Object       | Matrix            | Invalid cast. Host applications must return an error.                                                                                                                                                                                                                                                                                           |
| Object       | Object            | Valid if the types of the objects are identical and in accordance with the behavior defined in [Type Casting](#type-casting).                                                                                                                                                                                                                   |
| Structure    | Scalar            | Valid if the source structure contains at least one numeric member. The destination scalar receives the value of the source structure's first numeric member after applying the type casting and conversion behavior described in [Type Casting](#type-casting).                                                                                |
| Structure    | Vector            | The source structure must be at least the size of the vector. The first components must be numeric up to the size of the destination vector.                                                                                                                                                                                                    |
| Structure    | Matrix            | The source structure must be at least the size of the vector. The first components must be numeric up to the size of the destination vector.                                                                                                                                                                                                    |
| Structure    | Structure         | The destination structure must not be larger than the source structure. A valid cast must exist between all respective source and destination components.                                                                                                                                                                                       |



 

## Parameter Value Modifiers

Parameter modifier annotations add additional information to a parameter so the parameter's data can be interpreted properly. For instance, a vector may need to be expressed with normalized data or a length may be measured in inches. Parameter value modifier annotations express this additional information so that host applications can transform values correctly when data is transferred to an effect parameter.

These are the parameter modifiers:



| Parameter Value Modifier Annotations | Description                                    |
|--------------------------------------|------------------------------------------------|
| [SasNormalize](#sasnormalize)        | Specify whether a vector is normalized or not. |
| [SasUnits](#sasunits)                | Specify the units of measure for a parameter.  |



 

### SasNormalize

The SasNormalize annotation denotes that the associated parameter should be a normalized value whenever it is assigned. This annotation only affects float2, float3, and float4 parameters.


```
string SasNormalize = "Value";
```



where Value is either True or False.

Here is an example:


```
float3 UpNormal
<
  bool SasNormalize = "True";
>;
```



### SasUnits

The effect parameter data is in the following units:


```
string SasUnits = "Value";
```



where Value is one of the following:



| Measurement Type     | Value        | Description                    |
|----------------------|--------------|--------------------------------|
| No Units             | empty string | No units                       |
| Distance             | mm           | Millimeters                    |
|                      | cm           | Centimeters                    |
|                      | m            | Meters                         |
|                      | km           | Kilometers                     |
| Angle                | rad          | Radians                        |
| Time                 | ms           | Milliseconds                   |
|                      | sec          | Seconds                        |
|                      | min          | Minutes                        |
|                      | hr           | Hours                          |
| Linear Velocity      | mm/sec       | Millimeters per second         |
|                      | cm/sec       | Centimeters per second         |
|                      | m/sec        | Meters per second              |
|                      | m/hr         | Meters per hour                |
|                      | km/hr        | Kilometers per hour            |
| Linear Acceleration  | mm/sec²      | Millimeters per second squared |
|                      | cm/sec²      | Centimeters per second squared |
|                      | m/sec²       | Meters per second squared      |
|                      | m/hr²        | Meters per hour squared        |
|                      | km/hr²       | Kilometers per hour squared    |
| Angular Velocity     | rad/sec      | Radians per second             |
| Angular Acceleration | rad/sec²     | Radians per second squared     |
| Area                 | mm²          | Millimeters squared            |
|                      | cm²          | Centimeters squared            |
|                      | m²           | Meters squared                 |
|                      | km²          | Kilometers squared             |
| Volume               | mm³          | Millimeters cubed              |
|                      | cm³          | Centimeters cubed              |
|                      | m³           | Meters cubed                   |
|                      | km³          | Kilometers cubed               |



 

## Related topics

<dl> <dt>

[DirectX Standard Annotations and Semantics Reference](dx9-graphics-reference-effects-dxsas.md)
</dt> </dl>

 

 



