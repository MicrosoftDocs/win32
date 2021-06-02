---
description: 'The effect system defines several interfaces for managing effect state. There are two types of interfaces: those used by the runtime to render an effect and reflection interfaces for getting and setting effect variables.'
ms.assetid: 068d49d2-0e14-4080-9fee-20d984f22545
title: Effect System Interfaces (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Effect System Interfaces (Direct3D 10)

The effect system defines several interfaces for managing effect state. There are two types of interfaces: those used by the runtime to render an effect and reflection interfaces for getting and setting effect variables.

-   [Effect Runtime Interfaces](#effect-runtime-interfaces)
-   [Effect Reflection Interfaces](#effect-reflection-interfaces)

## Effect Runtime Interfaces

Use runtime interfaces to render an effect.



| Runtime Interfaces                                               | Description                                                          |
|------------------------------------------------------------------|----------------------------------------------------------------------|
| [**ID3D10Effect Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)                   | Collection of one or more techniques for rendering.                  |
| [**ID3D10Include Interface**](/previous-versions/windows/desktop/legacy/bb173775(v=vs.85))                 | An interface for adding custom behaviors when reading include files. |
| [**ID3D10EffectPass Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpass)           | A collection of state assignments.                                   |
| [**ID3D10EffectPool Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpool)           | Create a memory location for variables to be shared between effects. |
| [**ID3D10EffectTechnique Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effecttechnique) | A collection of one or more passes.                                  |



 

## Effect Reflection Interfaces

Reflection is implemented in the effect system to support reading (and writing) effect state. There are multiple ways to access effect variables.

### Setting Groups of Effect State

Use these interfaces to get and set a group of state.



| Reflection Interfaces                                                                  | Description                      |
|----------------------------------------------------------------------------------------|----------------------------------|
| [**ID3D10EffectBlendVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectblendvariable)               | Get and set blend state.         |
| [**ID3D10EffectDepthStencilVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilvariable) | Get and set depth-stencil state. |
| [**ID3D10EffectRasterizerVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectrasterizervariable)     | Get and set rasterizer state.    |
| [**ID3D10EffectSamplerVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectsamplervariable)           | Get and set sampler state.       |



 

### Setting Effect Resources

Use these interfaces to get and set resources.



| Reflection Interfaces                                                                          | Description                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**ID3D10EffectConstantBuffer Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectconstantbuffer)                     | Access data in a texture buffer or constant buffer. |
| [**ID3D10EffectDepthStencilViewVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilviewvariable) | Access data in a depth-stencil resource.            |
| [**ID3D10EffectRenderTargetViewVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectrendertargetviewvariable) | Access data in a render target.                     |
| [**ID3D10EffectShaderResourceVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectshaderresourcevariable)     | Access data in a shader resource.                   |



 

### Setting Other Effect Variables

Use these interfaces to get and set state by the variable type.



| Reflection Interfaces                                                      | Description                    |
|----------------------------------------------------------------------------|--------------------------------|
| [**ID3D10EffectMatrixVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectmatrixvariable) | Get and set a matrix.          |
| [**ID3D10EffectScalarVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectscalarvariable) | Get and set a scalar.          |
| [**ID3D10EffectShaderVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectshadervariable) | Get and set a shader variable. |
| [**ID3D10EffectStringVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectstringvariable) | Get and set a string.          |
| [**ID3D10EffectType Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effecttype)                     | Get a variable type.           |
| [**ID3D10EffectVectorVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectvectorvariable) | Get and set a vector.          |



 

All reflection interfaces derive from [**ID3D10EffectVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectvariable).

## Related topics

<dl> <dt>

[Effects](d3d10-graphics-programming-guide-effects.md)
</dt> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 
