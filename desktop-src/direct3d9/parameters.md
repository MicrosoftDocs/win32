---
description: Parameters are effect variables.
ms.assetid: 'vs|directx_sdk|~\parameters.htm'
title: Parameters (Direct3D 9)
ms.topic: reference
ms.date: 05/31/2018
---

# Parameters (Direct3D 9)

Parameters are effect variables.

## Syntax

*usage type ID* \[: *semantic*\] \[<*annotation(s)*>\] \[= *expression*\];

Parameters can be read from and written to by the application with [**ID3DXEffect**](id3dxeffect.md) or [**ID3DXEffectCompiler**](id3dxeffectcompiler.md).

Parameters can be referenced in functions and in techniques (specifically, in the right side of state assignments).



| Item                                                                                 | Description                                                                                                                                                     |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="usage"></span><span id="USAGE"></span>*usage*<br/>                   | Scope of the parameter. See [Usages and Literals (Direct3D 9)](usages-and-literals.md).<br/>                                                             |
| <span id="type"></span><span id="TYPE"></span>*type*<br/>                      | Any valid [Reference for HLSL](../direct3dhlsl/dx-graphics-hlsl-reference.md) type.<br/>                                                                        |
| <span id="ID"></span><span id="id"></span>*ID*<br/>                            | A unique name.<br/>                                                                                                                                       |
| <span id="semantic"></span><span id="SEMANTIC"></span>*semantic*<br/>          | A tag following identifier rules that typically indicates the usage of the parameter. Must be a particular type.<br/>                                     |
| <span id="annotations"></span><span id="ANNOTATIONS"></span>*annotations*<br/> | Zero or more pieces of user-specific information. May be any type. See [Add Information to Effect Parameters with Annotations](using-an-effect.md).<br/> |
| <span id="expression"></span><span id="EXPRESSION"></span>*expression*<br/>    | Initializes the parameter's value. See [Expressions (Direct3D 9)](expressions.md).<br/>                                                                  |



 

Parameters can be initialized to any valid [Reference for HLSL](../direct3dhlsl/dx-graphics-hlsl-reference.md) expression that reduces to a literal value.

Parameter values are not changed by the execution of state assignment or function calls.

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 
