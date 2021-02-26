---
title: ID3DX11EffectVariable GetParentConstantBuffer method (D3dx11effect.h)
description: Get a constant buffer. | ID3DX11EffectVariable GetParentConstantBuffer method (D3dx11effect.h)
ms.assetid: 43b46b05-951e-4c52-8bc7-4bb5f657ea78
keywords:
- GetParentConstantBuffer method Direct3D 11
- GetParentConstantBuffer method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , GetParentConstantBuffer method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.GetParentConstantBuffer
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::GetParentConstantBuffer method

Get a constant buffer.

## Syntax


```C++
ID3DX11EffectConstantBuffer* GetParentConstantBuffer();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md)\***

A pointer to a [**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md).

## Remarks

Effect variables are read-from or written-to a constant buffer.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

 





