---
title: ID3DX11EffectDepthStencilVariable UndoSetDepthStencilState method (D3dx11effect.h)
description: Reverts a previously set depth stencil state.
ms.assetid: 558bc777-a520-4235-84d3-db2d9f1ce4b6
keywords:
- UndoSetDepthStencilState method Direct3D 11
- UndoSetDepthStencilState method Direct3D 11 , ID3DX11EffectDepthStencilVariable interface
- ID3DX11EffectDepthStencilVariable interface Direct3D 11 , UndoSetDepthStencilState method
topic_type:
- apiref
api_name:
- ID3DX11EffectDepthStencilVariable.UndoSetDepthStencilState
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectDepthStencilVariable::UndoSetDepthStencilState method

Reverts a previously set depth stencil state.

## Syntax


```C++
HRESULT UndoSetDepthStencilState(
   UINT Index
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Index into an array of depth-stencil interfaces. If there is only one depth-stencil interface, use 0.

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

 

