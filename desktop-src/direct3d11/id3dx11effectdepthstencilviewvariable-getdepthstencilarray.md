---
title: ID3DX11EffectDepthStencilViewVariable GetDepthStencilArray method
description: Get an array of depth-stencil-view resources.
ms.assetid: '92b2d9b1-6cf8-4523-88e0-bcd09b95477c'
keywords: ["GetDepthStencilArray method Direct3D 11", "GetDepthStencilArray method Direct3D 11 , ID3DX11EffectDepthStencilViewVariable interface", "ID3DX11EffectDepthStencilViewVariable interface Direct3D 11 , GetDepthStencilArray method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectDepthStencilViewVariable.GetDepthStencilArray
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectDepthStencilViewVariable::GetDepthStencilArray method

Get an array of depth-stencil-view resources.

## Syntax


```C++
HRESULT GetDepthStencilArray(
   ID3D11DepthStencilView **ppResources,
   UINT                   Offset,
   UINT                   Count
);
```



## Parameters

<dl> <dt>

*ppResources* 
</dt> <dd>

Type: **[**ID3D11DepthStencilView**](id3d11depthstencilview.md)\*\***

A pointer to an array of depth-stencil-view interfaces. See [**ID3D11DepthStencilView**](id3d11depthstencilview.md).

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The zero-based array index to get the first interface.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of elements in the array.

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

 

 





