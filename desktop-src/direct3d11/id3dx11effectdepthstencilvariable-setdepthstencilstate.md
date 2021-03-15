---
title: ID3DX11EffectDepthStencilVariable SetDepthStencilState method (D3dx11effect.h)
description: Sets the depth stencil state.
ms.assetid: 4ece246f-4466-4790-8f38-450b67fff7c6
keywords:
- SetDepthStencilState method Direct3D 11
- SetDepthStencilState method Direct3D 11 , ID3DX11EffectDepthStencilVariable interface
- ID3DX11EffectDepthStencilVariable interface Direct3D 11 , SetDepthStencilState method
topic_type:
- apiref
api_name:
- ID3DX11EffectDepthStencilVariable.SetDepthStencilState
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectDepthStencilVariable::SetDepthStencilState method

Sets the depth stencil state.

## Syntax


```C++
HRESULT SetDepthStencilState(
   UINT                    Index,
   ID3D11DepthStencilState *pDepthStencilState
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Index into an array of depth-stencil interfaces. If there is only one depth-stencil interface, use 0.

</dd> <dt>

*pDepthStencilState* 
</dt> <dd>

Type: **[**ID3D11DepthStencilState**](/windows/desktop/api/D3D11/nn-d3d11-id3d11depthstencilstate)\***

Pointer to an [**ID3D11DepthStencilState**](/windows/desktop/api/D3D11/nn-d3d11-id3d11depthstencilstate) interface containing the new depth stencil state.

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

[ID3DX11EffectDepthStencilVariable](id3dx11effectdepthstencilvariable.md)
</dt> </dl>

 

