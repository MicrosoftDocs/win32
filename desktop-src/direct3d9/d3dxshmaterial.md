---
Description: Spherical harmonic (SH) precomputed radiance transfer (PRT) material characteristics.
ms.assetid: 2be49f96-ac61-46aa-8d56-d8eee8dca9ed
title: D3DXSHMATERIAL structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DXSHMATERIAL structure

Spherical harmonic (SH) precomputed radiance transfer (PRT) material characteristics.

## Syntax


```C++
typedef struct D3DXSHMATERIAL {
  D3DCOLORVALUE Diffuse;
  BOOL          bMirror;
  BOOL          bSubSurf;
  FLOAT         RelativeIndexOfRefraction;
  D3DCOLORVALUE Absorption;
  D3DCOLORVALUE ReducedScattering;
} D3DXSHMATERIAL, *LPD3DXSHMATERIAL;
```



## Members

<dl> <dt>

**Diffuse**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

Diffuse albedo of the surface. This value is ignored if the object is a mirror.

</dd> <dt>

**bMirror**
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Must be set to **FALSE**.

</dd> <dt>

**bSubSurf**
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Set to **TRUE** to enable subsurface scattering; any object that does subsurface scattering cannot be a mirror.

</dd> <dt>

**RelativeIndexOfRefraction**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Relative index of refraction is the ratio between two absolute indexes of refraction. An index of refraction is the ratio of the sine of the angle of incidence to the sine of the angle of refraction.

</dd> <dt>

**Absorption**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

The absorption coefficient is a parameter to the volume rendering equation used to model light propagation in a participating medium.

</dd> <dt>

**ReducedScattering**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

The reduced scattering coefficient is a parameter to the volume rendering equation used to model light propagation in a participating medium.

</dd> </dl>

## Remarks

Non-spectral scenes use the red channel from the materials instead of the luminance value.

For more information about PRT see:

-   Jensen, Henrik Wann, et al. Siggraph Proceedings: A Practical Model for Subsurface Light Transport, 2001.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




