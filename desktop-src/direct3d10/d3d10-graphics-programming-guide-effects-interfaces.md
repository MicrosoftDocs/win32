---
Description: 'The effect system defines several interfaces for managing effect state. There are two types of interfaces: those used by the runtime to render an effect and reflection interfaces for getting and setting effect variables.'
ms.assetid: '068d49d2-0e14-4080-9fee-20d984f22545'
title: 'Effect System Interfaces (Direct3D 10)'
---

# Effect System Interfaces (Direct3D 10)

The effect system defines several interfaces for managing effect state. There are two types of interfaces: those used by the runtime to render an effect and reflection interfaces for getting and setting effect variables.

-   [Effect Runtime Interfaces](#effect-runtime-interfaces)
-   [Effect Reflection Interfaces](#effect-reflection-interfaces)

## Effect Runtime Interfaces

Use runtime interfaces to render an effect.



| Runtime Interfaces                                               | Description                                                          |
|------------------------------------------------------------------|----------------------------------------------------------------------|
| [**ID3D10Effect Interface**](id3d10effect.md)                   | Collection of one or more techniques for rendering.                  |
| [**ID3D10Include Interface**](id3d10include.md)                 | An interface for adding custom behaviors when reading include files. |
| [**ID3D10EffectPass Interface**](id3d10effectpass.md)           | A collection of state assignments.                                   |
| [**ID3D10EffectPool Interface**](id3d10effectpool.md)           | Create a memory location for variables to be shared between effects. |
| [**ID3D10EffectTechnique Interface**](id3d10effecttechnique.md) | A collection of one or more passes.                                  |



 

## Effect Reflection Interfaces

Reflection is implemented in the effect system to support reading (and writing) effect state. There are multiple ways to access effect variables.

### Setting Groups of Effect State

Use these interfaces to get and set a group of state.



| Reflection Interfaces                                                                  | Description                      |
|----------------------------------------------------------------------------------------|----------------------------------|
| [**ID3D10EffectBlendVariable Interface**](id3d10effectblendvariable.md)               | Get and set blend state.         |
| [**ID3D10EffectDepthStencilVariable Interface**](id3d10effectdepthstencilvariable.md) | Get and set depth-stencil state. |
| [**ID3D10EffectRasterizerVariable Interface**](id3d10effectrasterizervariable.md)     | Get and set rasterizer state.    |
| [**ID3D10EffectSamplerVariable Interface**](id3d10effectsamplervariable.md)           | Get and set sampler state.       |



 

### Setting Effect Resources

Use these interfaces to get and set resources.



| Reflection Interfaces                                                                          | Description                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**ID3D10EffectConstantBuffer Interface**](id3d10effectconstantbuffer.md)                     | Access data in a texture buffer or constant buffer. |
| [**ID3D10EffectDepthStencilViewVariable Interface**](id3d10effectdepthstencilviewvariable.md) | Access data in a depth-stencil resource.            |
| [**ID3D10EffectRenderTargetViewVariable Interface**](id3d10effectrendertargetviewvariable.md) | Access data in a render target.                     |
| [**ID3D10EffectShaderResourceVariable Interface**](id3d10effectshaderresourcevariable.md)     | Access data in a shader resource.                   |



 

### Setting Other Effect Variables

Use these interfaces to get and set state by the variable type.



| Reflection Interfaces                                                      | Description                    |
|----------------------------------------------------------------------------|--------------------------------|
| [**ID3D10EffectMatrixVariable Interface**](id3d10effectmatrixvariable.md) | Get and set a matrix.          |
| [**ID3D10EffectScalarVariable Interface**](id3d10effectscalarvariable.md) | Get and set a scalar.          |
| [**ID3D10EffectShaderVariable Interface**](id3d10effectshadervariable.md) | Get and set a shader variable. |
| [**ID3D10EffectStringVariable Interface**](id3d10effectstringvariable.md) | Get and set a string.          |
| [**ID3D10EffectType Interface**](id3d10effecttype.md)                     | Get a variable type.           |
| [**ID3D10EffectVectorVariable Interface**](id3d10effectvectorvariable.md) | Get and set a vector.          |



 

All reflection interfaces derive from [**ID3D10EffectVariable Interface**](id3d10effectvariable.md).

## Related topics

<dl> <dt>

[Effects](d3d10-graphics-programming-guide-effects.md)
</dt> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 



