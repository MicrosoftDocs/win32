---
title: Effects 11 Interfaces
description: This section contains reference information for the component object model (COM) interfaces of the Effects 11 source.
ms.assetid: 1b997513-73f7-423a-8af3-1c9fa0d2f469
ms.topic: article
ms.date: 05/31/2018
---

# Effects 11 Interfaces

This section contains reference information for the component object model (COM) interfaces of the Effects 11 source.


## In this section



| Topic                                                                                                   | Description                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3DX11Effect**](id3dx11effect.md)<br/>                                                       | An [**ID3DX11Effect**](id3dx11effect.md) interface manages a set of state objects, resources, and shaders for implementing a rendering effect.<br/>                                                                                                                                                    |
| [**ID3DX11EffectBlendVariable**](id3dx11effectblendvariable.md)<br/>                             | The blend-variable interface accesses blend state.<br/>                                                                                                                                                                                                                                                 |
| [**ID3DX11EffectClassInstanceVariable**](id3dx11effectclassinstancevariable.md)<br/>             | Accesses a class instance.<br/>                                                                                                                                                                                                                                                                         |
| [**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md)<br/>                           | A constant-buffer interface accesses constant buffers or texture buffers.<br/>                                                                                                                                                                                                                          |
| [**ID3DX11EffectDepthStencilVariable**](id3dx11effectdepthstencilvariable.md)<br/>               | A depth-stencil-variable interface accesses depth-stencil state.<br/>                                                                                                                                                                                                                                   |
| [**ID3DX11EffectDepthStencilViewVariable**](id3dx11effectdepthstencilviewvariable.md)<br/>       | A depth-stencil-view-variable interface accesses a depth-stencil view.<br/>                                                                                                                                                                                                                             |
| [**ID3DX11EffectGroup**](id3dx11effectgroup.md)<br/>                                             | The [**ID3DX11EffectGroup**](id3dx11effectgroup.md) interface accesses an Effect group.<br/> The lifetime of an [**ID3DX11EffectGroup**](id3dx11effectgroup.md) object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.<br/>                               |
| [**ID3DX11EffectInterfaceVariable**](id3dx11effectinterfacevariable.md)<br/>                     | Accesses an interface variable.<br/>                                                                                                                                                                                                                                                                    |
| [**ID3DX11EffectMatrixVariable**](id3dx11effectmatrixvariable.md)<br/>                           | A matrix-variable interface accesses a matrix.<br/>                                                                                                                                                                                                                                                     |
| [**ID3DX11EffectPass**](id3dx11effectpass.md)<br/>                                               | An [**ID3DX11EffectPass**](id3dx11effectpass.md) interface encapsulates state assignments within a technique.<br/> The lifetime of an [**ID3DX11EffectPass**](id3dx11effectpass.md) object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.<br/>           |
| [**ID3DX11EffectRasterizerVariable**](id3dx11effectrasterizervariable.md)<br/>                   | A rasterizer-variable interface accesses rasterizer state.<br/>                                                                                                                                                                                                                                         |
| [**ID3DX11EffectRenderTargetViewVariable**](id3dx11effectrendertargetviewvariable.md)<br/>       | A render-target-view interface accesses a render target.<br/>                                                                                                                                                                                                                                           |
| [**ID3DX11EffectSamplerVariable**](id3dx11effectsamplervariable.md)<br/>                         | A sampler interface accesses sampler state.<br/>                                                                                                                                                                                                                                                        |
| [**ID3DX11EffectScalarVariable**](id3dx11effectscalarvariable.md)<br/>                           | An effect-scalar-variable interface accesses scalar values.<br/>                                                                                                                                                                                                                                        |
| [**ID3DX11EffectShaderResourceVariable**](id3dx11effectshaderresourcevariable.md)<br/>           | A shader-resource interface accesses a shader resource.<br/>                                                                                                                                                                                                                                            |
| [**ID3DX11EffectShaderVariable**](id3dx11effectshadervariable.md)<br/>                           | A shader-variable interface accesses a shader variable.<br/>                                                                                                                                                                                                                                            |
| [**ID3DX11EffectStringVariable**](id3dx11effectstringvariable.md)<br/>                           | A string-variable interface accesses a string variable.<br/>                                                                                                                                                                                                                                            |
| [**ID3DX11EffectTechnique**](id3dx11effecttechnique.md)<br/>                                     | An [**ID3DX11EffectTechnique**](id3dx11effecttechnique.md) interface is a collection of passes.<br/> The lifetime of an [**ID3DX11EffectTechnique**](id3dx11effecttechnique.md) object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.<br/>               |
| [**ID3DX11EffectType**](id3dx11effecttype.md)<br/>                                               | The [**ID3DX11EffectType**](id3dx11effecttype.md) interface accesses effect variables by type.<br/> The lifetime of an [**ID3DX11EffectType**](id3dx11effecttype.md) object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.<br/>                          |
| [**ID3DX11EffectUnorderedAccessViewVariable**](id3dx11effectunorderedaccessviewvariable.md)<br/> | Accesses an unordered access view.<br/>                                                                                                                                                                                                                                                                 |
| [**ID3DX11EffectVariable**](id3dx11effectvariable.md)<br/>                                       | The [**ID3DX11EffectVariable**](id3dx11effectvariable.md) interface is the base class for all effect variables.<br/> The lifetime of an [**ID3DX11EffectVariable**](id3dx11effectvariable.md) object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.<br/> |
| [**ID3DX11EffectVectorVariable**](id3dx11effectvectorvariable.md)<br/>                           | A vector-variable interface accesses a four-component vector.<br/>                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[Effects 11 Reference](d3d11-graphics-reference-effects11.md)
</dt> </dl>

 

 





