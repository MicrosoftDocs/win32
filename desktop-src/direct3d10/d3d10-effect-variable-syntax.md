---
description: An effect variable is declared with the following syntax.
ms.assetid: 53939c65-3725-44cc-bec6-775c3b921770
title: Effect Variable Syntax (Direct3D 10)
ms.topic: reference
ms.date: 05/31/2018
---

# Effect Variable Syntax (Direct3D 10)

An effect variable is declared with the following syntax.

## Syntax

*DataType* *VariableName* \[ : *SemanticName* \] < *Annotations* >;



| Name         | Description                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DataType     | Any [basic](../direct3dhlsl/dx-graphics-hlsl-variable-syntax.md) or [texture](../direct3dhlsl/dx-graphics-hlsl-to-type.md) type.                                                                        |
| VariableName | An ASCII string that uniquely identifies the name of the effect variable.                                                                                                                   |
| SemanticName | A ASCII string that denotes additional information about how a variable should be used. A semantic is an ASCII string that can be either a predefined system-value or a custom-user string. |
| Annotations  | One or more pieces of user-supplied information (metadata) that is ignored by the effect system. For syntax, see [Annotation Syntax (Direct3D 10)](d3d10-effect-annotation-syntax.md).     |



 

An effect variable that is declared outside of all functions, is considered global in scope; variables declared within a function are local to that function.

## Example

The [BasicHLSL10 sample](https://msdn.microsoft.com/library/Ee416395(v=VS.85).aspx) uses global variables without semantics for material colors, light properties and transformation matrices.

This example illustrates global effect variables.


```
float4 g_MaterialAmbientColor;      // Material's ambient color
float4 g_MaterialDiffuseColor;      // Material's diffuse color
float3 g_LightDir[3];               // Light's direction in world space
float4x4 g_mWorld;                  // World matrix for object
```



This example illustrates effect variables that are local to a shader function.


```
VS_OUTPUT RenderSceneVS( ... )
{
    float3 vNormalWorldSpace;
    float4 vAnimatedPos;

    // shader body
}
```



This example illustrates function parameters that have semantics.


```
VS_OUTPUT RenderSceneVS( float4 vPos : SV_POSITION,
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD0,
                         uniform int nNumLights,
                         uniform bool bTexture,
                         uniform bool bAnimate )
{
  ...
}
```



This example illustrates declaring a texture variable.


```
Texture2D g_MeshTexture;            // Color texture for mesh
```



Sampling a texture is done with a texture sampler. To set up a sampler in an effect, see the [sampler type](../direct3dhlsl/dx-graphics-hlsl-sampler.md).

## Related topics

<dl> <dt>

[Effect Format](d3d10-effect-format.md)
</dt> </dl>

 

 
