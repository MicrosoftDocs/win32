---
title: ID3DX11Effect interface (D3dx11effect.h)
description: An ID3DX11Effect interface manages a set of state objects, resources, and shaders for implementing a rendering effect.
ms.assetid: 34429d51-6b45-4a62-bce1-50c4da02edac
keywords:
- ID3DX11Effect interface Direct3D 11
- ID3DX11Effect interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11Effect
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect interface

An **ID3DX11Effect** interface manages a set of state objects, resources, and shaders for implementing a rendering effect.

## Members

The **ID3DX11Effect** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX11Effect** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11Effect** interface has these methods.



| Method                                                                     | Description                                                                               |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**CloneEffect**](id3dx11effect-cloneeffect.md)                           | Creates a copy of an effect interface.<br/>                                         |
| [**GetClassLinkage**](id3dx11effect-getclasslinkage.md)                   | Gets a class linkage interface.<br/>                                                |
| [**GetConstantBufferByIndex**](id3dx11effect-getconstantbufferbyindex.md) | Get a constant buffer by index.<br/>                                                |
| [**GetConstantBufferByName**](id3dx11effect-getconstantbufferbyname.md)   | Get a constant buffer by name.<br/>                                                 |
| [**GetDesc**](id3dx11effect-getdesc.md)                                   | Get an effect description.<br/>                                                     |
| [**GetDevice**](id3dx11effect-getdevice.md)                               | Get the device that created the effect.<br/>                                        |
| [**GetGroupByIndex**](id3dx11effect-getgroupbyindex.md)                   | Gets an effect group by index.<br/>                                                 |
| [**GetGroupByName**](id3dx11effect-getgroupbyname.md)                     | Gets an effect group by name.<br/>                                                  |
| [**GetTechniqueByIndex**](id3dx11effect-gettechniquebyindex.md)           | Get a technique by index.<br/>                                                      |
| [**GetTechniqueByName**](id3dx11effect-gettechniquebyname.md)             | Get a technique by name.<br/>                                                       |
| [**GetVariableByIndex**](id3dx11effect-getvariablebyindex.md)             | Get a variable by index.<br/>                                                       |
| [**GetVariableByName**](id3dx11effect-getvariablebyname.md)               | Get a variable by name.<br/>                                                        |
| [**GetVariableBySemantic**](id3dx11effect-getvariablebysemantic.md)       | Get a variable by semantic.<br/>                                                    |
| [**IsOptimized**](id3dx11effect-isoptimized.md)                           | Test an effect to see if the reflection metadata has been removed from memory.<br/> |
| [**IsValid**](id3dx11effect-isvalid.md)                                   | Test an effect to see if it contains valid syntax.<br/>                             |
| [**Optimize**](id3dx11effect-optimize.md)                                 | Minimize the amount of memory required for an effect.<br/>                          |



 

## Remarks

An effect is created by calling [**D3DX11CreateEffectFromMemory**](d3dx11createeffectfrommemory.md).

The effect system groups the information required for rendering into an effect which contains: state objects for assigning state changes in groups, resources for supplying input data and storing output data, and programs that control how the rendering is done called shaders.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

> [!Note]
>
> If you call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on an **ID3DX11Effect** object to retrieve the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface, **QueryInterface** returns E\_NOINTERFACE. To work around this issue, use the following code:
>
> 
>
> 
| 
|
| <pre><code>    IUnknown* pIUnknown = (IUnknown*)pEffect;&gt;     pIUnknown-&gt;AddRef();</code></pre> | 

>
> 
>
>  

## Requirements

| Requirement | Value |
|-------------|-------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |

## See also

[Effects 11 Interfaces](d3d11-graphics-reference-effects11-interfaces.md)

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
