---
title: ID3DX11EffectGroup interface (D3dx11effect.h)
description: The ID3DX11EffectGroup interface accesses an Effect group.The lifetime of an ID3DX11EffectGroup object is equal to the lifetime of its parent ID3DX11Effect object.
ms.assetid: f5a35c47-0bac-4559-bd6c-5e8bc7699e10
keywords:
- ID3DX11EffectGroup interface Direct3D 11
- ID3DX11EffectGroup interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectGroup
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectGroup interface

The **ID3DX11EffectGroup** interface accesses an Effect group.

The lifetime of an **ID3DX11EffectGroup** object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.

-   [Methods](#methods)

### Methods

The **ID3DX11EffectGroup** interface has these methods.



| Method                                                                  | Description                                                   |
|:------------------------------------------------------------------------|:--------------------------------------------------------------|
| [**GetAnnotationByIndex**](id3dx11effectgroup-getannotationbyindex.md) | Get an annotation by index.<br/>                        |
| [**GetAnnotationByName**](id3dx11effectgroup-getannotationbyname.md)   | Get an annotation by name.<br/>                         |
| [**GetDesc**](id3dx11effectgroup-getdesc.md)                           | Gets a group description.<br/>                          |
| [**GetTechniqueByIndex**](id3dx11effectgroup-gettechniquebyindex.md)   | Get a technique by index.<br/>                          |
| [**GetTechniqueByName**](id3dx11effectgroup-gettechniquebyname.md)     | Get a technique by name.<br/>                           |
| [**IsValid**](id3dx11effectgroup-isvalid.md)                           | Test an effect to see if it contains valid syntax.<br/> |



 

## Remarks

To get an **ID3DX11EffectGroup** interface, call a method like [**ID3DX11Effect::GetGroupByName**](id3dx11effect-getgroupbyname.md).

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Interfaces](d3d11-graphics-reference-effects11-interfaces.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

 





