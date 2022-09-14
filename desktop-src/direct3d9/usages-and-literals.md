---
description: Usage is similar to a parameter's scope, because it defines the scope in which the parameter is valid.
ms.assetid: 9ba10dba-626f-4cb8-8dc2-1419329b199e
title: Usages and Literals (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Usages and Literals (Direct3D 9)

Usage is similar to a parameter's scope, because it defines the scope in which the parameter is valid.



| Value  | Description                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| const  | The parameter will be constant within the scope of all functions. (Note that such parameters can still be written to with either [**ID3DXEffect**](id3dxeffect.md) or [**ID3DXEffectCompiler**](id3dxeffectcompiler.md), because this occurs outside the scope of all functions.) |
| shared | The parameter will be shared in the effect pool.                                                                                                                                                                                                                                    |
| static | The parameter will be invisible to the application, that is, you cannot access them from [**ID3DXEffect**](id3dxeffect.md) or [**ID3DXEffectCompiler**](id3dxeffectcompiler.md).                                                                                                  |



 

Marking a parameter as literal indicates that its value will never change. This enables the effect compiler to do extra optimization.

Only non-shared top-level parameters can be marked as literal. Parameters can only be marked as literal with [**ID3DXEffectCompiler**](id3dxeffectcompiler.md). Literal values cannot be set with [**ID3DXEffect**](id3dxeffect.md).

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



