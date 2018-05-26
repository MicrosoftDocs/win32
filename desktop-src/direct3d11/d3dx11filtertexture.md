---
title: D3DX11FilterTexture function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the DirectXTex library, GenerateMipMaps and GenerateMipMaps3D. Generates mipmap chain using a particular texture filter.
ms.assetid: 52ae3228-f9d7-4944-b49c-55df1816f1f7
keywords:
- D3DX11FilterTexture function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11FilterTexture
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX11FilterTexture function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, **GenerateMipMaps** and **GenerateMipMaps3D**.

 

Generates mipmap chain using a particular texture filter.

## Syntax


```C++
HRESULT D3DX11FilterTexture(
   ID3D11DeviceContext *pContext,
   ID3D11Resource      *pTexture,
   UINT                SrcLevel,
   UINT                MipFilter
);
```



## Parameters

<dl> <dt>

*pContext* 
</dt> <dd>

Type: **[**ID3D11DeviceContext**](/windows/win32/D3D11/nn-d3d11-id3d11devicecontext?branch=master)\***

A pointer to an [**ID3D11DeviceContext**](/windows/win32/D3D11/nn-d3d11-id3d11devicecontext?branch=master) object.

</dd> <dt>

*pTexture* 
</dt> <dd>

Type: **[**ID3D11Resource**](/windows/win32/D3D11/nn-d3d11-id3d11resource?branch=master)\***

The texture object to be filtered. See [**ID3D11Resource**](/windows/win32/D3D11/nn-d3d11-id3d11resource?branch=master).

</dd> <dt>

*SrcLevel* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The mipmap level whose data is used to generate the rest of the mipmap chain.

</dd> <dt>

*MipFilter* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags controlling how each miplevel is filtered (or D3DX11\_DEFAULT for D3DX11\_FILTER\_LINEAR). See [**D3DX11\_FILTER\_FLAG**](d3dx11-filter-flag.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





