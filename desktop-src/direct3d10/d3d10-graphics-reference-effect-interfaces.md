---
Description: 'This section contains information about the following effect-system interfaces:'
ms.assetid: 'ebe0afc7-6261-4c96-a54e-9b491e240c03'
title: 'Effect Interfaces (Direct3D 10)'
---

# Effect Interfaces (Direct3D 10)

This section contains information about the following effect-system interfaces:



| Interfaces                                                                                     | Description                                                      |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**ID3D10EffectBlendVariable Interface**](id3d10effectblendvariable.md)                       | Accesses blend state.                                            |
| [**ID3D10EffectConstantBuffer Interface**](id3d10effectconstantbuffer.md)                     | Accesses a texture-buffer or a constant-buffer.                  |
| [**ID3D10EffectDepthStencilVariable Interface**](id3d10effectdepthstencilvariable.md)         | Accesses depth-stencil state.                                    |
| [**ID3D10EffectDepthStencilViewVariable Interface**](id3d10effectdepthstencilviewvariable.md) | Accesses a depth-stencil view.                                   |
| [**ID3D10Effect Interface**](id3d10effect.md)                                                 | Encapsulates pipeline state in one or more rendering techniques. |
| [**ID3D10Include Interface**](id3d10include.md)                                               | User-implemented methods for reading include files.              |
| [**ID3D10EffectMatrixVariable Interface**](id3d10effectmatrixvariable.md)                     | Accesses a matrix.                                               |
| [**ID3D10EffectPass Interface**](id3d10effectpass.md)                                         | Encapsulates effect state in a pass.                             |
| [**ID3D10EffectPool Interface**](id3d10effectpool.md)                                         | Identifies shared-effect variables.                              |
| [**ID3D10EffectRasterizerVariable Interface**](id3d10effectrasterizervariable.md)             | Accesses rasterizer state.                                       |
| [**ID3D10EffectRenderTargetViewVariable Interface**](id3d10effectrendertargetviewvariable.md) | Accesses a render target.                                        |
| [**ID3D10EffectSamplerVariable Interface**](id3d10effectsamplervariable.md)                   | Accesses sampler state.                                          |
| [**ID3D10EffectScalarVariable Interface**](id3d10effectscalarvariable.md)                     | Accesses a scalar variable.                                      |
| [**ID3D10EffectShaderResourceVariable Interface**](id3d10effectshaderresourcevariable.md)     | Accesses a shader resource.                                      |
| [**ID3D10EffectShaderVariable Interface**](id3d10effectshadervariable.md)                     | Accesses a shader variable.                                      |
| [**ID3D10EffectStringVariable Interface**](id3d10effectstringvariable.md)                     | Accesses a string.                                               |
| [**ID3D10EffectTechnique Interface**](id3d10effecttechnique.md)                               | Encapsulates one or more passes.                                 |
| [**ID3D10EffectType Interface**](id3d10effecttype.md)                                         | Implements methods for accessing effect variables.               |
| [**ID3D10EffectVectorVariable Interface**](id3d10effectvectorvariable.md)                     | Accesses a vector.                                               |



 

There are two kinds of interfaces in the effect framework: rendering interfaces for rendering an effect and reflection interfaces for getting and setting effect variables with the API. All reflection interfaces derive from [**ID3D10EffectVariable Interface**](id3d10effectvariable.md).

## Related topics

<dl> <dt>

[Effect Reference](d3d10-graphics-reference-effect.md)
</dt> </dl>

 

 



