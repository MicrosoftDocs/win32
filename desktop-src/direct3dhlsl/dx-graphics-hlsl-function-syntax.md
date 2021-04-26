---
title: Function Declaration Syntax
description: HLSL functions are declared with the following syntax.
ms.assetid: f8968de2-7b2d-4a2e-8312-cec5b652f700
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Function Declaration Syntax

HLSL functions are declared with the following syntax.



|                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------|
| \[*StorageClass*\] \[clipplanes()\] \[precise\] Return\_Value *Name* ( \[*ArgumentList*\] ) \[: *Semantic*\] {   \[*StatementBlock*\] }; |



 

## Parameters

<dl> <dt>

<span id="StorageClass"></span><span id="storageclass"></span><span id="STORAGECLASS"></span>*StorageClass*
</dt> <dd>

Modifier that redefines a function declaration. **inline** is currently the only modifier value. The modifier value must be **inline** because it is also the default value. Therefore, a function is inline regardless of whether you specify **inline**, and all functions in HLSL are inline. An inline function generates a copy of the function body (when compiling) for each function call. This is done to decrease the overhead of calling the function.

</dd> <dt>

<span id="Clipplanes"></span><span id="clipplanes"></span><span id="CLIPPLANES"></span>*Clipplanes*
</dt> <dd>

Optional list of clip planes, which is up to 6 user-specified clip planes. This is an alternate mechanism for [SV\_ClipDistance](dx-graphics-hlsl-semantics.md) that works on [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 9\_x and higher.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*
</dt> <dd>

An ASCII string that uniquely identifies the name of the shader function.

</dd> <dt>

<span id="ArgumentList"></span><span id="argumentlist"></span><span id="ARGUMENTLIST"></span>*ArgumentList*
</dt> <dd>

Optional argument list, which is a comma-separated list of [arguments](dx-graphics-hlsl-function-parameters.md) passed into a function.

</dd> <dt>

<span id="Semantic"></span><span id="semantic"></span><span id="SEMANTIC"></span>*Semantic*
</dt> <dd>

Optional string that identifies the intended usage of the return data (see [Semantics (DirectX HLSL)](dx-graphics-hlsl-semantics.md)).

</dd> <dt>

<span id="StatementBlock"></span><span id="statementblock"></span><span id="STATEMENTBLOCK"></span>*StatementBlock*
</dt> <dd>

Optional [statements](dx-graphics-hlsl-statement-blocks.md) that make up the body of the function. A function defined without a body is called a function prototype; the body of a prototype function must be defined elsewhere before the function can be called.

</dd> </dl>

## Return Value

The return type can be any one of these [HLSL types](dx-graphics-hlsl-data-types.md).

## Remarks

The syntax on this page describes almost every type of HLSL function, this includes vertex shaders, pixel shaders, and helper functions. While a geometry shader is also implemented with a function, its syntax is a little more complicated, so there is a separate page that defines a geometry shader function declaration (see [Geometry-Shader Object (DirectX HLSL)](dx-graphics-hlsl-geometry-shader.md)).

A function can be overloaded as long as it is given a unique combination of parameter types and/or parameter order. HLSL also implements a number of built in, or [**intrinsic functions**](dx-graphics-hlsl-intrinsic-functions.md).

You can specify user-specific clip planes with the **clipplanes** attribute. Windows applies these clip planes to all of the primitives drawn. The **clipplanes** attribute works like [SV\_ClipDistance](dx-graphics-hlsl-semantics.md) but works on all hardware [feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 9\_x and higher. For more info, see [User clip planes on feature level 9 hardware](/windows/desktop/direct3dhlsl/user-clip-planes-on-10level9).

## Examples

This example is from BasicHLSL10.fx from the [BasicHLSL10 Sample](https://msdn.microsoft.com/library/Ee416395(v=VS.85).aspx).


```hlsl
struct VS_OUTPUT
{
    float4 Position   : SV_POSITION; 
    float4 Diffuse    : COLOR0;
    float2 TextureUV  : TEXCOORD0;
};

VS_OUTPUT RenderSceneVS( float4 vPos : POSITION,
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD,
                         uniform int nNumLights,
                         uniform bool bTexture,
                         uniform bool bAnimate )
{
    VS_OUTPUT Output;
    ...
    return Output;    
}
```



This example from AdvancedParticles.fx from the [AdvancedParticles Sample](https://msdn.microsoft.com/library/Ee416394(v=VS.85).aspx), illustrates using a semantic for the return type.


```hlsl
//
// PS for particles
//
float4 PSPointSprite(PSSceneIn input) : SV_Target
{   
    return g_txDiffuse.Sample( g_samLinear, input.tex ) * input.color;
}
```



## Related topics

<dl> <dt>

[Functions (DirectX HLSL)](dx-graphics-hlsl-functions.md)
</dt> </dl>

 

 
