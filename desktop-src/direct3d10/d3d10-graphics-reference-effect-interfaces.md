---
description: 'This section contains information about the following effect-system interfaces:'
ms.assetid: ebe0afc7-6261-4c96-a54e-9b491e240c03
title: Effect Interfaces (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Effect Interfaces (Direct3D 10)

This section contains information about the following effect-system interfaces:



| Interfaces                                                                                     | Description                                                      |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**ID3D10EffectBlendVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectblendvariable)                       | Accesses blend state.                                            |
| [**ID3D10EffectConstantBuffer Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectconstantbuffer)                     | Accesses a texture-buffer or a constant-buffer.                  |
| [**ID3D10EffectDepthStencilVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilvariable)         | Accesses depth-stencil state.                                    |
| [**ID3D10EffectDepthStencilViewVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilviewvariable) | Accesses a depth-stencil view.                                   |
| [**ID3D10Effect Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)                                                 | Encapsulates pipeline state in one or more rendering techniques. |
| [**ID3D10Include Interface**](/previous-versions/windows/desktop/legacy/bb173775(v=vs.85))                                               | User-implemented methods for reading include files.              |
| [**ID3D10EffectMatrixVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectmatrixvariable)                     | Accesses a matrix.                                               |
| [**ID3D10EffectPass Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpass)                                         | Encapsulates effect state in a pass.                             |
| [**ID3D10EffectPool Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectpool)                                         | Identifies shared-effect variables.                              |
| [**ID3D10EffectRasterizerVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectrasterizervariable)             | Accesses rasterizer state.                                       |
| [**ID3D10EffectRenderTargetViewVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectrendertargetviewvariable) | Accesses a render target.                                        |
| [**ID3D10EffectSamplerVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectsamplervariable)                   | Accesses sampler state.                                          |
| [**ID3D10EffectScalarVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectscalarvariable)                     | Accesses a scalar variable.                                      |
| [**ID3D10EffectShaderResourceVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectshaderresourcevariable)     | Accesses a shader resource.                                      |
| [**ID3D10EffectShaderVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectshadervariable)                     | Accesses a shader variable.                                      |
| [**ID3D10EffectStringVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectstringvariable)                     | Accesses a string.                                               |
| [**ID3D10EffectTechnique Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effecttechnique)                               | Encapsulates one or more passes.                                 |
| [**ID3D10EffectType Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effecttype)                                         | Implements methods for accessing effect variables.               |
| [**ID3D10EffectVectorVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectvectorvariable)                     | Accesses a vector.                                               |



 

There are two kinds of interfaces in the effect framework: rendering interfaces for rendering an effect and reflection interfaces for getting and setting effect variables with the API. All reflection interfaces derive from [**ID3D10EffectVariable Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effectvariable).

## Related topics

<dl> <dt>

[Effect Reference](d3d10-graphics-reference-effect.md)
</dt> </dl>

 

 
