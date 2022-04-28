---
title: D3DX11SHProjectCubeMap function (D3DX11tex.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the Spherical Harmonics Math library, SHProjectCubeMap.
ms.assetid: 58c741a3-dd5d-4b18-b257-5e85a9b799fd
keywords:
- D3DX11SHProjectCubeMap function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11SHProjectCubeMap
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX11SHProjectCubeMap function

> [!Note]
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated and is not supported for Windows Store apps.

> [!Note]
> Instead of using this function, we recommend that you use the [Spherical Harmonics Math](https://github.com/Microsoft/DirectXMath/tree/master/SHMath) library function **SHProjectCubeMap**.



Projects a function represented in a cube map into spherical harmonics.

## Syntax


```C++
HRESULT D3DX11SHProjectCubeMap(
   ID3D11DeviceContext *pContext,
   UINT                Order,
   ID3D11Texture2D     *pCubeMap,
   FLOAT               *pROut,
   FLOAT               *pGOut,
   FLOAT               *pBOut
);
```



## Parameters

<dl> <dt>

*pContext*
</dt> <dd>

Type: **[**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext)\***

A pointer to an [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) object.

</dd> <dt>

*Order*
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Order of the SH evaluation, generates Order^2 coefficients whose degree is Order-1. Valid range is between 2 and 6.

</dd> <dt>

*pCubeMap*
</dt> <dd>

Type: **[**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d)\***

A pointer to an [**ID3D11Texture2D**](/windows/desktop/api/D3D11/nn-d3d11-id3d11texture2d) that represents a cubemap that is going to be projected into spherical harmonics.

</dd> <dt>

*pROut*
</dt> <dd>

Type: **[**FLOAT**](/windows/desktop/WinProg/windows-data-types)\***

Output SH vector for red.

</dd> <dt>

*pGOut*
</dt> <dd>

Type: **[**FLOAT**](/windows/desktop/WinProg/windows-data-types)\***

Output SH vector for green.

</dd> <dt>

*pBOut*
</dt> <dd>

Type: **[**FLOAT**](/windows/desktop/WinProg/windows-data-types)\***

Output SH vector for blue.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>
