---
title: Struct Type
description: Struct Type
ms.assetid: 896030b0-07cd-41bd-8c94-e173eabc81dd
keywords:
- Struct Type HLSL
topic_type:
- apiref
api_name:
- Struct Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Struct Type

Use the following syntax to declare a structure using HLSL.

struct *Name*{     \[*InterpolationModifier*\] *Type*\[*R*x*C*\] *MemberName*;     ... };



 

## Parameters

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*
</dt> <dd>

An ASCII string that uniquely identifies the structure name.

</dd> <dt>

<span id="_InterpolationModifier_"></span><span id="_interpolationmodifier_"></span><span id="_INTERPOLATIONMODIFIER_"></span>\[*InterpolationModifier*\]
</dt> <dd>

Optional modifier that specifies an interpolation type. See [Remarks](#remarks) for details.

</dd> <dt>

<span id="Type_RxC_"></span><span id="type_rxc_"></span><span id="TYPE_RXC_"></span>*Type*\[*R*x*C*\]
</dt> <dd>

The member type with an optional row (*R*) x column (*C*) array size. A structure contains at least one element; if it contains more than one element, the elements are all of the same type. The number of rows and columns are unsigned integers between 1 and 4 inclusive.

</dd> <dt>

<span id="MemberName"></span><span id="membername"></span><span id="MEMBERNAME"></span>*MemberName*
</dt> <dd>

An ASCII string that uniquely identifies the member name.

</dd> </dl>

## Remarks

An interpolation modifier can be specified on any structure member or on an argument to a pixel shader function. If a modifier appears in both places, the outside modifier (the pixel shader argument modifier) overrules the inside modifier (the structure modifier).

When compiling a shader or an effect, the shader compiler packs structure members according to [HLSL packing rules](dx-graphics-hlsl-packing-rules.md).

### Interpolation Modifiers Introduced in Shader Model 4

Vertex shader outputs that are used for pixel shader inputs are linearly interpolated to get per-pixel values during rasterization. To set the method of interpolation, use any of the following values, which are supported in [shader model 4](dx-graphics-hlsl-sm4.md) or later. The modifier is ignored on any vertex shader output that is not used as a pixel shader input.



| Interpolation Modifier | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **linear**             | Interpolate between shader inputs; **linear** is the default value if no interpolation modifier is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **centroid**           | Interpolate between samples that are somewhere within the covered area of the pixel (this may require extrapolating end points from a pixel center). Centroid sampling may improve antialiasing if a pixel is partially covered (even if the pixel center is not covered). The **centroid** modifier must be combined with either the **linear** or **noperspective** modifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **nointerpolation**    | Do not interpolate .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **noperspective**      | Do not perform perspective-correction during interpolation. The **noperspective** modifier can be combined with the **centroid** modifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **sample**             | **Available in shader model 4.1 and later**Interpolate at sample location rather than at the pixel center. This causes the pixel shader to execute per-sample rather than per-pixel. Another way to cause per-sample execution is to have an input with [semantic SV\_SampleIndex](dx-graphics-hlsl-semantics.md), which indicates the current sample. Only the inputs with **sample** specified (or inputting SV\_SampleIndex) differ between shader invocations in the pixel, whereas other inputs that do not specify modifiers (for example, if you mix modifiers on different inputs) still interpolate at the pixel center. Both pixel shader invocation and depth/stencil testing occur for every covered sample in the pixel. This is sometimes known as *supersampling*. In contrast, in the absence of sample frequency invocation, known as *multisampling*, the pixel shader is invoked once per pixel regardless of how many samples are covered, while depth/stencil testing occurs at sample frequency. Both modes provide equivalent edge antialiasing. However, supersampling provides better shading quality by invoking the pixel shader more frequently.<br/> |



 

<dl> 1. When using an int/uint type, the only valid option is **nointerpolation**.  
</dl>

Interpolation modifiers can be applied to structure members or [function arguments](dx-graphics-hlsl-function-parameters.md), or both.

## Examples

Here are some example structure declarations.


```
struct struct1
{
  int    a;
}
```



This declaration includes an array.


```
struct struct2
{
  int    a;
  float  b;
  int4x4 iMatrix;
}
```



This declaration includes an interpolation modifier.


```
struct In
{
  centroid float2 Texcoord;
};
```



## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





