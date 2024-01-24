---
description: Use SasHostParameterValue Collection to define the collection of host application values, as well as their type and members, exposed to effects.
ms.assetid: 3fef353d-323a-4cc1-a8c9-2bf154754835
title: Data Binding
ms.topic: article
ms.date: 05/31/2018
---

# Data Binding

Use [SasHostParameterValue Collection](#sashostparametervalue-collection) to define the collection of host application values, as well as their type and members, exposed to effects. Use the [SasBindAddress](#sasbindaddress) annotation in an effect file to associate an effect parameter with its corresponding parameter in the host application.

## SasHostParameterValue Collection

The SasHostParameterValue is defined using effect file (.fx) syntax. While the syntax is very similar to the effect file syntax, some differences exist. For example, object types, such as texture2d, samplers, and strings, are not valid in actual effect files, but are valid in the SasHostParameterValue. A host application can implement SasHostParameterValue in any way so long as it conforms to the description below; the actual definition is located in the DXSAS standard effect include file (\[SDK Root\]/Utilities/Source/Sas/Sas.fxh).

Note that arrays in the SasHostParameterValue such as Lights or Cameras have unbounded length. This means that effects can bind to any arbitrary index in those arrays and host applications must provide meaningful defaults in the cases where no application value can be provided.

Some types and constants are required to be defined in the DXSAS standard include, as noted in the definition of the standard include. This allows effects to easily bind aggregated values from the SasHostParameterValue to structured effect parameters.



| SasHostParameterValue Collection    | Type            | Member                                       |
|-------------------------------------|-----------------|----------------------------------------------|
| [Time](#time)                       | float           | Sas.Time.Now                                 |
|                                     | float           | Sas.Time.Last                                |
|                                     | int             | Sas.Time.FrameNumber                         |
| [Environment Map](#environment-map) | textureCUBE     | Sas.EnvironmentMap                           |
| [Camera](#camera)                   | SasCamera       | Sas.Camera                                   |
|                                     | float4x4        | Sas.Camera.WorldToView                       |
|                                     | float4x4        | Sas.Camera.Projection                        |
|                                     | float2          | Sas.Camera.NearFarClipping                   |
| [Light](#light)                     | SasAmbientLight | AmbientLight\[ZeroOrMore\];                  |
|                                     | int             | Sas.NumAmbientLights                         |
|                                     | SasAmbientLight | DirectionalLight\[ZeroOrMore\];              |
|                                     | int             | Sas.NumDirectionalLights                     |
|                                     | SasAmbientLight | PointLight\[ZeroOrMore\];                    |
|                                     | int             | Sas.NumPointLights                           |
|                                     | SasAmbientLight | SpotLight\[ZeroOrMore\];                     |
|                                     | int             | Sas.NumSpotLights                            |
| [Shadow](#shadow)                   | float4x4        | Sas.Shadow\[ZeroOrMore\].WorldToShadow       |
|                                     | texture2D       | Sas.Shadow\[ZeroOrMore\].ShadowMap           |
| [Skeleton](#skeleton)               | float4x4        | Sas.Skeleton.MeshToJointToWorld\[OneOrMore\] |
|                                     | int             | Sas.Skeleton.NumJoints                       |



 

### Time

The host application's virtual clock or time value. Members include:

-   Sas.Time.Now - the value of the host application virtual clock at the point at which the effect will be rendered.
-   Sas.Time.Last - the value of Now at the previous render.
-   Sas.Time.FrameNumber - the counter value that is incremented once per rendered frame.

Effects must properly handle the fact that the values of these members can potentially wrap around during extremely long execution times. Now and Last may have very large values.

### Environment Map

A cubic environment map. Host applications must provide a valid cube texture if an effect attempts to bind to Sas.EnvironmentMap.

### Camera

The camera currently being rendered. Members include:

-   Sas.Camera.WorldToView - the composite world-view matrix for the camera.
-   Sas.Camera.Projection - the projection matrix for the camera.
-   Sas.Camera.NearFarClipping - the values of the near and far clipping planes.

### Light

One or more scene lights. The collection of lights is declared as an array where:

-   Color - an RGB color. The default value is (0,0,0).
-   Direction - the light direction. The default value is (0,0,0).
-   Range - the distance from the light where the light rays have no effect on the scene. The default value is 0.
-   Theta - the inner cone angle of a spotlight, measured in radians. The default value is 0.
-   Phi - the outer cone angle of a spotlight, measured in radians. The default value is 0.

The number of lights must be set to the number of lights bound into the associated array. Effects can choose to ignore the number of lights and bind to any element of one of the light arrays. Therefore, host applications must provide a valid binding for elements beyond the number of lights in the array.

ZeroOrMore implies that the array may have any number of elements.

### Shadow

Shadow buffers which consists of:

-   WorldToShadow - an array of matrices.
-   ShadowMap - a 2D texture file.

ZeroOrMore implies that the array may have any number of elements (zero means an empty array).

An effect would declare a sampler as follows:


```
texture2D Shadow 
<
  string SasBindAddress = "Sas.Shadow[0].ShadowMap";
>;

sampler ShadowSampler = shadow_sampler(Shadow);
```



### Skeleton

The set of frames that compose the currently rendering object. Frame examples are bones and transforms. This includes:

-   MeshToJointToWorld - an array of matrices.
-   NumJoints - the number of joints in the skeleton.

OneOrMore implies that the array has at least one and may contain any number of elements.

The definition supports both rigid and skinned mesh objects using the same set of [SasHostParameterValue Collection](#sashostparametervalue-collection) values with different interpretation.

## SasBindAddress

This annotation is added to the top of an effect file to associate an effect parameter with its corresponding parameter defined in the [SasHostParameterValue Collection](#sashostparametervalue-collection). The annotation is declared like this:


```
string SasBindAddress = "SasHostParameterValue";
```



This example binds the effect world matrix to the MeshToJointToWorld matrix:


```
float4x3 World
<
  string SasBindAddress = "Sas.Skeleton.MeshToJointToWorld[0]";
>;
```



This annotation tells the host application that it needs to set the value of the effect world matrix using the data in the MeshToJointToWorld matrix.

The bind address annotation syntax was defined to be very similar with the syntax used by [**ID3DXEffect**](id3dxeffect.md) to get and set effect parameters. The only difference between the DXSAS grammar and **ID3DXEffect** methods is the addition of the asterisk index token. Here is another example using the asterisk index:


```
float3 LightColors[6]
<
  string SasBindAddress = "Sas.Light[*].Color";
>;
```



The asterisk index token denotes that all elements of the particular host envirnmant value array (color in this case) should be bound in the associated parameter. Multiple asterisk index tokens allow effects to bind to sub-elements of an array of structures without the need to bind the entire structure itself. This example binds the color values of the first six lights to an effect parameter.

## Related topics

<dl> <dt>

[DirectX Standard Annotations and Semantics Reference](dx9-graphics-reference-effects-dxsas.md)
</dt> </dl>

 

 



