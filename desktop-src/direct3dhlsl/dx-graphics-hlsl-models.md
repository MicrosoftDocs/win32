---
title: Shader Models vs Shader Profiles
description: Shader Models vs Shader Profiles
ms.assetid: 6224f05e-20b1-42ea-96fb-63dd0edb720e
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Shader Models vs Shader Profiles

The High Level Shading Language for DirectX implements a series of shader models. Using HLSL, you can create C-like programmable shaders for the Direct3D pipeline. Each shader model builds on the capabilities of the model before it, implementing more functionality with fewer restrictions.

Shader model 1 started with DirectX 8 and included assembly level and C-like instructions. This model has many limitations caused by early programmable shader hardware. Shader model 2 and 3 greatly expanded on the number of instructions, and constants shaders could use. They are much more powerful than shader model 1, but still carry some of the existing limitations of the first shader model.

Starting with Windows Vista, shader model 4 is a complete redesign. It allows unlimited instructions and constants (within hardware constraints of your machine), has templated objects to make texture sampling cleaner and more efficient, and has the fewest restrictions of any shader model. It does however require the Windows Driver Model which is only available on the Windows Vista (or later) operating system.

## Shader Profiles

A shader profile is the target for compiling a shader; this table lists the shader profiles that are supported by each shader model.



| Shader model                                                   | Shader profiles                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Shader Model 1](dx-graphics-hlsl-sm1.md)         | vs\_1\_1                                                                                                                                                                                                                                                                                              |
| [Shader Model 2](dx-graphics-hlsl-sm2.md)         | ps\_2\_0, ps\_2\_x, vs\_2\_0, vs\_2\_x, ps\_4\_0\_level\_9\_0, ps\_4\_0\_level\_9\_1, ps\_4\_0\_level\_9\_3, vs\_4\_0\_level\_9\_0, vs\_4\_0\_level\_9\_1, vs\_4\_0\_level\_9\_3, lib\_4\_0\_level\_9\_1, lib\_4\_0\_level\_9\_3                                                                      |
| [Shader Model 3](dx-graphics-hlsl-sm3.md)         | ps\_3\_0, vs\_3\_0                                                                                                                                                                                                                                                                                    |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)         | cs\_4\_0, gs\_4\_0, ps\_4\_0, vs\_4\_0, cs\_4\_1, gs\_4\_1, ps\_4\_1, vs\_4\_1, lib\_4\_0, lib\_4\_1                                                                                                                                                                                                  |
| [Shader Model 5](d3d11-graphics-reference-sm5.md) | cs\_5\_0, ds\_5\_0, gs\_5\_0, hs\_5\_0, ps\_5\_0, vs\_5\_0, lib\_5\_0 (Although gs\_4\_0, gs\_4\_1, ps\_4\_0, ps\_4\_1, vs\_4\_0, and vs\_4\_1 were introduced in shader model 4.0, shader model 5 adds support to these shader profiles for structured buffers and byte address buffers.)<br/> |
| [Shader Model 6](shader-model-6-0.md)             | cs\_6\_0, ds\_6\_0, gs\_6\_0, hs\_6\_0, ps\_6\_0, vs\_6\_0, lib\_6\_0                                                                                                                                                                                                                                 |

Differences between Direct3D 9 and Direct3D 10:

- Direct3D 9 introduced shader models 1, 2, and 3.
- Direct3D 10 introduced shader model 4.
- Direct3D 10.1 introduced shader model 4.1.



 

## Effect Profiles

An effect profile is the target for compiling an effect/shader; this table lists the effect profiles that are supported by each version of Direct3D.

Differences between Direct3D 9 and Direct3D 10:

- Direct3D 9 introduced effect-framework profiles fx\_1\_0 and fx\_2\_0.
- Direct3D 10 introduced effect-framework profile fx\_4\_0.
- Direct3D 10.1 introduced effect-framework profile fx\_4\_1.
- Direct3D 11 introduced effect-framework profile fx\_5\_0.

> [!Note]  
> These legacy effects profiles are deprecated.

 

## Related topics

<dl> <dt>

[Reference for HLSL](dx-graphics-hlsl-reference.md)
</dt> </dl>

 

 





