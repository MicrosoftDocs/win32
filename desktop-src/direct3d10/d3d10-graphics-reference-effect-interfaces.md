---
Description: This section contains information about the following effect-system interfaces
ms.assetid: ebe0afc7-6261-4c96-a54e-9b491e240c03
title: Effect Interfaces (Direct3D 10)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Effect Interfaces (Direct3D 10)

This section contains information about the following effect-system interfaces:



| Interfaces                                                                                     | Description                                                      |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**ID3D10EffectBlendVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectblendvariable?branch=master)                       | Accesses blend state.                                            |
| [**ID3D10EffectConstantBuffer Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectconstantbuffer?branch=master)                     | Accesses a texture-buffer or a constant-buffer.                  |
| [**ID3D10EffectDepthStencilVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilvariable?branch=master)         | Accesses depth-stencil state.                                    |
| [**ID3D10EffectDepthStencilViewVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectdepthstencilviewvariable?branch=master) | Accesses a depth-stencil view.                                   |
| [**ID3D10Effect Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effect?branch=master)                                                 | Encapsulates pipeline state in one or more rendering techniques. |
| [**ID3D10Include Interface**](/windows/win32/D3D10Shader/?branch=master)                                               | User-implemented methods for reading include files.              |
| [**ID3D10EffectMatrixVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectmatrixvariable?branch=master)                     | Accesses a matrix.                                               |
| [**ID3D10EffectPass Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectpass?branch=master)                                         | Encapsulates effect state in a pass.                             |
| [**ID3D10EffectPool Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectpool?branch=master)                                         | Identifies shared-effect variables.                              |
| [**ID3D10EffectRasterizerVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectrasterizervariable?branch=master)             | Accesses rasterizer state.                                       |
| [**ID3D10EffectRenderTargetViewVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectrendertargetviewvariable?branch=master) | Accesses a render target.                                        |
| [**ID3D10EffectSamplerVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectsamplervariable?branch=master)                   | Accesses sampler state.                                          |
| [**ID3D10EffectScalarVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectscalarvariable?branch=master)                     | Accesses a scalar variable.                                      |
| [**ID3D10EffectShaderResourceVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectshaderresourcevariable?branch=master)     | Accesses a shader resource.                                      |
| [**ID3D10EffectShaderVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectshadervariable?branch=master)                     | Accesses a shader variable.                                      |
| [**ID3D10EffectStringVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectstringvariable?branch=master)                     | Accesses a string.                                               |
| [**ID3D10EffectTechnique Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effecttechnique?branch=master)                               | Encapsulates one or more passes.                                 |
| [**ID3D10EffectType Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effecttype?branch=master)                                         | Implements methods for accessing effect variables.               |
| [**ID3D10EffectVectorVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectvectorvariable?branch=master)                     | Accesses a vector.                                               |



 

There are two kinds of interfaces in the effect framework: rendering interfaces for rendering an effect and reflection interfaces for getting and setting effect variables with the API. All reflection interfaces derive from [**ID3D10EffectVariable Interface**](/windows/win32/D3D10Effect/nn-d3d10effect-id3d10effectvariable?branch=master).

## Related topics

<dl> <dt>

[Effect Reference](d3d10-graphics-reference-effect.md)
</dt> </dl>

 

 



