---
title: ID3DX11EffectDepthStencilViewVariable SetDepthStencil method
description: Set a depth-stencil-view resource.
ms.assetid: '35cbcd3b-6fc8-448d-a82e-724f91038d07'
keywords: ["SetDepthStencil method Direct3D 11", "SetDepthStencil method Direct3D 11 , ID3DX11EffectDepthStencilViewVariable interface", "ID3DX11EffectDepthStencilViewVariable interface Direct3D 11 , SetDepthStencil method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectDepthStencilViewVariable.SetDepthStencil
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectDepthStencilViewVariable::SetDepthStencil method

Set a depth-stencil-view resource.

## Syntax


```C++
HRESULT SetDepthStencil(
   ID3D11DepthStencilView *pResource
);
```



## Parameters

<dl> <dt>

*pResource* 
</dt> <dd>

Type: **[**ID3D11DepthStencilView**](id3d11depthstencilview.md)\***

A pointer to a depth-stencil-view interface. See [**ID3D11DepthStencilView**](id3d11depthstencilview.md).

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

[ID3DX11EffectDepthStencilViewVariable](id3dx11effectdepthstencilviewvariable.md)
</dt> </dl>

 

 





