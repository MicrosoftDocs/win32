---
title: ID3DX11EffectConstantBuffer SetTextureBuffer method
description: Set a texture-buffer.
ms.assetid: 'b8c327e4-52ff-498e-81e9-187e58bbe5d2'
keywords: ["SetTextureBuffer method Direct3D 11", "SetTextureBuffer method Direct3D 11 , ID3DX11EffectConstantBuffer interface", "ID3DX11EffectConstantBuffer interface Direct3D 11 , SetTextureBuffer method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectConstantBuffer.SetTextureBuffer
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectConstantBuffer::SetTextureBuffer method

Set a texture-buffer.

## Syntax


```C++
HRESULT SetTextureBuffer(
   ID3D11ShaderResourceView *pTextureBuffer
);
```



## Parameters

<dl> <dt>

*pTextureBuffer* 
</dt> <dd>

Type: **[**ID3D11ShaderResourceView**](id3d11shaderresourceview.md)\***

A pointer to a shader-resource-view interface for accessing a texture buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectConstantBuffer](id3dx11effectconstantbuffer.md)
</dt> </dl>

 

 





