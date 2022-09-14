---
description: Projects a function represented in a cube map into spherical harmonics.
ms.assetid: de8bc4bd-cb29-44ab-8806-33d3ffd10a7b
title: D3DX10SHProjectCubeMap function (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10SHProjectCubeMap
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10SHProjectCubeMap function

Projects a function represented in a cube map into spherical harmonics.

## Syntax


```C++
HRESULT D3DX10SHProjectCubeMap(
   UINT            Order,
   ID3D10Texture2D *pCubeMap,
   FLOAT           *pROut,
   FLOAT           *pGOut,
   FLOAT           *pBOut
);
```



## Parameters

<dl> <dt>

*Order* 
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH evaluation, generates Order^2 coefs, degree is Order-1.

</dd> <dt>

*pCubeMap* 
</dt> <dd>

Type: **[**ID3D10Texture2D**](/windows/desktop/api/D3D10/nn-d3d10-id3d10texture2d)\***

Cubemap that is going to be projected into spherical harmonics. See [**ID3D10Texture2D**](/windows/desktop/api/D3D10/nn-d3d10-id3d10texture2d).

</dd> <dt>

*pROut* 
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Output SH vector for red.

</dd> <dt>

*pGOut* 
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Output SH vector for green.

</dd> <dt>

*pBOut* 
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Output SH vector for blue.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>  |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
