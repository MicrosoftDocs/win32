---
Description: 'Projects a function represented on a cube map into spherical harmonics (SH).'
ms.assetid: 'da5a3195-801e-4f1c-b52c-9eafc6e2e7b4'
title: D3DXSHProjectCubeMap function
---

# D3DXSHProjectCubeMap function

Projects a function represented on a cube map into spherical harmonics (SH).

## Syntax


```C++
HRESULT D3DXSHProjectCubeMap(
  _In_ UINT                   Order,
  _In_ LPDIRECT3DCUBETEXTURE9 pCubeMap,
  _In_ FLOAT                  *pROut,
  _In_ FLOAT                  *pGOut,
  _In_ FLOAT                  *pBOut
);
```



## Parameters

<dl> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Order of the spherical harmonic (SH) evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*pCubeMap* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DCUBETEXTURE9**](idirect3dcubetexture9.md)**

Pointer to a source cube texture. See [**IDirect3DCubeTexture9**](idirect3dcubetexture9.md).

</dd> <dt>

*pROut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to the output SH vector for the red component.

</dd> <dt>

*pGOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to the output SH vector for the green component.

</dd> <dt>

*pBOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to the output SH vector for the blue component.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[Precomputed Radiance Transfer (Direct3D 9)](precomputed-radiance-transfer.md)
</dt> </dl>

 

 




