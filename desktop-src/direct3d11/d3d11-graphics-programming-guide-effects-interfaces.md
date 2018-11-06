---
title: Effect System Interfaces (Direct3D 11)
description: The effect system defines several interfaces for managing effect state.
ms.assetid: 5cba6055-d153-4837-9a08-96efbde5f48f
ms.topic: article
ms.date: 05/31/2018
---

# Effect System Interfaces (Direct3D 11)

The effect system defines several interfaces for managing effect state. There are two types of interfaces: those used by the runtime to render an effect and reflection interfaces for getting and setting effect variables.

-   [Effect Runtime Interfaces](#effect-runtime-interfaces)
-   [Effect Reflection Interfaces](#effect-reflection-interfaces)

## Effect Runtime Interfaces

Use runtime interfaces to render an effect.



| Runtime Interfaces                                       | Description                                                    |
|----------------------------------------------------------|----------------------------------------------------------------|
| [**ID3DX11Effect**](id3dx11effect.md)                   | Collection of one or more groups and techniques for rendering. |
| [**ID3DX11EffectPass**](id3dx11effectpass.md)           | A collection of state assignments.                             |
| [**ID3DX11EffectTechnique**](id3dx11effecttechnique.md) | A collection of one or more passes.                            |
| [**ID3DX11EffectGroup**](id3dx11effectgroup.md)         | A collection of one or more techniques.                        |



 

## Effect Reflection Interfaces

Reflection is implemented in the effect system to support reading (and writing) effect state. There are multiple ways to access effect variables.

### Setting Groups of Effect State

Use these interfaces to get and set a group of state.



| Reflection Interfaces                                                          | Description                      |
|--------------------------------------------------------------------------------|----------------------------------|
| [**ID3DX11EffectBlendVariable**](id3dx11effectblendvariable.md)               | Get and set blend state.         |
| [**ID3DX11EffectDepthStencilVariable**](id3dx11effectdepthstencilvariable.md) | Get and set depth-stencil state. |
| [**ID3DX11EffectRasterizerVariable**](id3dx11effectrasterizervariable.md)     | Get and set rasterizer state.    |
| [**ID3DX11EffectSamplerVariable**](id3dx11effectsamplervariable.md)           | Get and set sampler state.       |



 

### Setting Effect Resources

Use these interfaces to get and set resources.



| Reflection Interfaces                                                                        | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md)                           | Access data in a texture buffer or constant buffer. |
| [**ID3DX11EffectDepthStencilViewVariable**](id3dx11effectdepthstencilviewvariable.md)       | Access data in a depth-stencil resource.            |
| [**ID3DX11EffectRenderTargetViewVariable**](id3dx11effectrendertargetviewvariable.md)       | Access data in a render target.                     |
| [**ID3DX11EffectShaderResourceVariable**](id3dx11effectshaderresourcevariable.md)           | Access data in a shader resource.                   |
| [**ID3DX11EffectUnorderedAccessViewVariable**](id3dx11effectunorderedaccessviewvariable.md) | Access data in an unordered access view.            |



 

### Setting Other Effect Variables

Use these interfaces to get and set state by the variable type.



| Reflection Interfaces                                                            | Description               |
|----------------------------------------------------------------------------------|---------------------------|
| [**ID3DX11EffectClassInstanceVariable**](id3dx11effectclassinstancevariable.md) | Get a class instance.     |
| [**ID3DX11EffectInterfaceVariable**](id3dx11effectinterfacevariable.md)         | Get and set an interface. |
| [**ID3DX11EffectMatrixVariable**](id3dx11effectmatrixvariable.md)               | Get and set a matrix.     |
| [**ID3DX11EffectScalarVariable**](id3dx11effectscalarvariable.md)               | Get and set a scalar.     |
| [**ID3DX11EffectShaderVariable**](id3dx11effectshadervariable.md)               | Get a shader variable.    |
| [**ID3DX11EffectStringVariable**](id3dx11effectstringvariable.md)               | Get and set a string.     |
| [**ID3DX11EffectType**](id3dx11effecttype.md)                                   | Get a variable type.      |
| [**ID3DX11EffectVectorVariable**](id3dx11effectvectorvariable.md)               | Get and set a vector.     |



 

All reflection interfaces derive from [**ID3DX11EffectVariable**](id3dx11effectvariable.md).

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> <dt>

[Programming Guide for Direct3D 11](dx-graphics-overviews.md)
</dt> </dl>

 

 




