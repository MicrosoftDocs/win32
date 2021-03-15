---
title: ID3DX11EffectConstantBuffer GetTextureBuffer method (D3dx11effect.h)
description: Get a texture-buffer.
ms.assetid: 8d09e67c-358e-49ee-8ca4-e1f548b52c3a
keywords:
- GetTextureBuffer method Direct3D 11
- GetTextureBuffer method Direct3D 11 , ID3DX11EffectConstantBuffer interface
- ID3DX11EffectConstantBuffer interface Direct3D 11 , GetTextureBuffer method
topic_type:
- apiref
api_name:
- ID3DX11EffectConstantBuffer.GetTextureBuffer
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectConstantBuffer::GetTextureBuffer method

Get a texture-buffer.

## Syntax


```C++
HRESULT GetTextureBuffer(
   ID3D11ShaderResourceView **ppTextureBuffer
);
```



## Parameters

<dl> <dt>

*ppTextureBuffer* 
</dt> <dd>

Type: **[**ID3D11ShaderResourceView**](/windows/desktop/api/D3D11/nn-d3d11-id3d11shaderresourceview)\*\***

The address of a pointer to a shader-resource-view interface for accessing a texture buffer. See [**ID3D11ShaderResourceView**](/windows/desktop/api/D3D11/nn-d3d11-id3d11shaderresourceview).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectConstantBuffer](id3dx11effectconstantbuffer.md)
</dt> </dl>

 

 





