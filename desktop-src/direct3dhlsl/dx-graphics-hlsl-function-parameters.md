---
title: Function Arguments
description: A function takes one or more input arguments; use the following syntax to declare each argument.
ms.assetid: 80e0dbc8-26b7-4250-bb01-6856fc70f6b8
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Function Arguments

A function takes one or more input arguments; use the following syntax to declare each argument.



|                                                                                             |
|---------------------------------------------------------------------------------------------|
| **\[InputModifier\] Type Name \[: Semantic\] \[InterpolationModifier\] \[= Initializers\]** |



 

\[Modifier\] Type Name \[: Semantic\] \[: Interpolation Modifier\] \[= Initializer(s)\]

If there are multiple function arguments, they are separated by commas.

## Parameters



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="InputModifier"></span><span id="inputmodifier"></span><span id="INPUTMODIFIER"></span><strong>InputModifier</strong><br/></td>
<td>Optional term that identifies an argument as an input, an output, or both.<br/> 
<table>
<tbody>
<tr class="odd">
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td><strong>in</strong></td>
<td>Input only</td>
</tr>
<tr class="odd">
<td><strong>inout</strong></td>
<td>Input and an output</td>
</tr>
<tr class="even">
<td><strong>out</strong></td>
<td>Output only</td>
</tr>
<tr class="odd">
<td><strong>uniform</strong></td>
<td>Input only constant data</td>
</tr>
</tbody>
</table>

<p> </p>
<p>Parameters are always passed by value. in indicates that the value of the parameter should be copied in from the calling application before the function begins. out indicates that the last value of the parameter should be copied out, and returned to the calling application when the function returns. inout is a shorthand for specifying both.</p>
<p>A uniform value comes from a constant register; each vertex shader or pixel shader invocation see the same initial value for a uniform variable. Global variables are treated as if they are declared uniform. For non-top-level functions, uniform is synonymous with <strong>in</strong>. If no parameter usage is specified, the parameter usage is assumed to be <strong>in</strong>.</p></td>
</tr>
<tr class="even">
<td><p><span id="Type"></span><span id="type"></span><span id="TYPE"></span><strong>Type</strong></p></td>
<td><p>The argument type; can be any valid HLSL <a href="dx-graphics-hlsl-data-types.md">type</a>.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Name"></span><span id="name"></span><span id="NAME"></span><strong>Name</strong></p></td>
<td><p>An ASCII string that uniquely identifies the name of the shader function.</p></td>
</tr>
<tr class="even">
<td><p><span id="Semantic"></span><span id="semantic"></span><span id="SEMANTIC"></span><strong>Semantic</strong></p></td>
<td><p>Optional string that identifies the intended usage of the data (see <a href="dx-graphics-hlsl-semantics.md">Semantics (DirectX HLSL)</a>).</p></td>
</tr>
<tr class="odd">
<td><p><span id="InterpolationModifier"></span><span id="interpolationmodifier"></span><span id="INTERPOLATIONMODIFIER"></span><strong>InterpolationModifier</strong></p></td>
<td><p>Optional <a href="dx-graphics-hlsl-struct.md">interpolation modifier</a> which allows a shader to determine the method of interpolation. An interpolation modifier on a function argument only applies to an argument used as an input to a pixel shader function.</p></td>
</tr>
<tr class="even">
<td><p><span id="Initializers"></span><span id="initializers"></span><span id="INITIALIZERS"></span><strong>Initializers</strong></p></td>
<td><p>Optional values for initialization; multiple values are required to initialize multi-component data types.</p></td>
</tr>
</tbody>
</table>



 

## Remarks

Function arguments are listed in a comma-separated argument list in a function declaration. As in C functions, each argument must have a parameter name and type declared; an argument to an HLSL function optionally can include a semantic, an initial value, and a pixel shader input can include an interpolation type.

The *Type* of a function argument could be a structure, which could include a per-member interpolation modifier. If the function argument also has an interpolation modifier, the function argument modifier overrides interpolation modifiers declared within the Type.

## Examples

This example (from the [BasicHLSL10 Sample](https://msdn.microsoft.com/library/Ee416395(v=VS.85).aspx)) illustrates uniform and non-uniform inputs to a vertex shader function.


```
VS_OUTPUT RenderSceneVS( 
  float4 vPos : POSITION,
  float3 vNormal : NORMAL,
  float2 vTexCoord0 : TEXCOORD,
  uniform int nNumLights,
  uniform bool bTexture,
  uniform bool bAnimate )
{
  ...
}
```



This example (from the [ContentStreaming Sample](https://msdn.microsoft.com/library/Ee416397(v=VS.85).aspx)) uses an input structure to pass arguments to a pixel shader function.


```
VSBasicIn input
struct VSBasicIn
{
  float4 Pos    : POSITION;
  float3 Norm   : NORMAL;
  float2 Tex    : TEXCOORD0;
};

PSBasicIn VSBasic(VSBasicIn input)
{
  ...
}
```



## Related topics

<dl> <dt>

[Functions (DirectX HLSL)](dx-graphics-hlsl-functions.md)
</dt> </dl>

 

 





