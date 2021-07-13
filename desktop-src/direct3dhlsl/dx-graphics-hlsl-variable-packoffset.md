---
title: packoffset
description: Optional shader constant packing keyword, which uses the following syntax
ms.assetid: f0a3031b-d385-430d-83ee-7a8142334ad7
keywords:
- packoffset HLSL
topic_type:
- apiref
api_name:
- packoffset
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# packoffset

Optional shader constant packing keyword, which uses the following syntax:

: packoffset( c\[Subcomponent\]\[.component\] )



 

## Parameters



| Item                                                                                                                                                                                 | Description                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="packoffset"></span><span id="PACKOFFSET"></span>**packoffset**<br/>                                                                                                  | Required keyword.<br/>                                                                                                                         |
| <span id="c"></span><span id="C"></span>**c**<br/>                                                                                                                             | Packing applies to constant registers (c) only. <br/>                                                                                          |
| <span id="_Subcomponent__.component_"></span><span id="_subcomponent__.component_"></span><span id="_SUBCOMPONENT__.COMPONENT_"></span>**\[Subcomponent\]\[.component\]**<br/> | Optional subcomponents and components. A subcomponent is a register number, which is an integer. A component is in the form of \[.xyzw\].<br/> |



 

## Remarks

Use this keyword to manually pack a shader constant when [declaring a variable type](dx-graphics-hlsl-variable-syntax.md).

When packing a constant, you cannot mix constant types.

The compiler behaves slightly differently for global constants and uniform constants:

-   A global constant. A global variable is added as a global constant to a *$Global* cbuffer by the compiler. Automatically packed elements (those declared without packoffset) will appear after the last manually packed variable. You may mix types when packing global constants.
-   A uniform constant. A uniform parameter in the parameter list of a function will be added to a *$Param* constant buffer by the compiler when the shader is compiled outside of the effects framework. When compiled inside the effect framework, a uniform constant must resolve to a uniform variable defined in global scope. A uniform constant cannot be manually offset; their recommend use is only for specialization of shaders where they alias back to globals, not as a means of passing application data into the shader.

Here are some additional examples: [packing constants using shader model 4](dx-graphics-hlsl-packing-rules.md).

## Examples

Here are several examples of manually packing shader constants.

Pack subcomponents of vectors and scalars whose size is large enough to prevent crossing register boundaries. For example, these are all valid:


```
cbuffer MyBuffer
{
    float4 Element1 : packoffset(c0);
    float1 Element2 : packoffset(c1);
    float1 Element3 : packoffset(c1.y);
}
```



## See also

<dl> <dt>

[Variable Syntax](dx-graphics-hlsl-variable-syntax.md)
</dt> <dt>

[Variables (DirectX HLSL)](dx-graphics-hlsl-variables.md)
</dt> </dl>

 

 





