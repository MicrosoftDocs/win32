---
description: Evaluates a directional light and returns spectral spherical harmonic (SH) data.
ms.assetid: 6e2e9b02-13bb-4cef-ae9d-343fbf64e5d7
title: D3DXSHEvalDirectionalLight function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHEvalDirectionalLight
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSHEvalDirectionalLight function (D3dx9math.h)

Evaluates a [directional light](light-types.md) and returns spectral spherical harmonic (SH) data.

## Syntax


```C++
HRESULT D3DXSHEvalDirectionalLight(
  _In_        UINT        Order,
  _In_  const D3DXVECTOR3 *pDir,
  _In_        FLOAT       RIntensity,
  _In_        FLOAT       GIntensity,
  _In_        FLOAT       BIntensity,
  _Out_       FLOAT       *pROut,
  _Out_       FLOAT       *pGOut,
  _Out_       FLOAT       *pBOut
);
```



## Parameters

<dl> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*pDir* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the (x, y, z) hemisphere axis direction vector in which to evaluate the SH basis functions. See Remarks.

</dd> <dt>

*RIntensity* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The red intensity of the light.

</dd> <dt>

*GIntensity* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The green intensity of the light.

</dd> <dt>

*BIntensity* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The blue intensity of the light.

</dd> <dt>

*pROut* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to the output SH vector for the red component.

</dd> <dt>

*pGOut* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Optional pointer to the output SH vector for the green component.

</dd> <dt>

*pBOut* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Optional pointer to the output SH vector for the blue component.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be: D3DERR\_INVALIDCALL.

## Remarks

The output vector is computed so that if the intensity ratio R/G/B is equal to 1, the resulting exit radiance of a point directly under the light on a diffuse object with an albedo of 1 would be 1.0. This will compute three spectral samples; *pROut* will be returned, while *pGOut* and *pBOut* may be returned.

On the sphere with unit radius, as shown in the following illustration, direction can be specified simply with theta, the angle about the z-axis in the [right-handed direction](coordinate-systems.md), and phi, the angle from z.

![illustration of a sphere with unit radius](images/spherical-coordinates.png)

The following equations show the relationship between Cartesian (x, y, z) and spherical (theta, phi) coordinates on the unit sphere. The angle theta varies over the range of 0 to 2 pi, while phi varies from 0 to pi.

![equations of the relationship between cartesian and spherical coordinates](images/spherical-coordinates-equations.png)

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[Precomputed Radiance Transfer (Direct3D 9)](precomputed-radiance-transfer.md)
</dt> </dl>

 

 
