---
description: Creates a mesh containing the specified text, using the font associated with the device context.
ms.assetid: 1c8b0dc6-51b8-45bf-b4c0-b67e3d128097
title: D3DXCreateText function (D3dx9shape.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateText
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreateText function

Creates a mesh containing the specified text, using the font associated with the device context.

## Syntax


```C++
HRESULT D3DXCreateText(
  _In_  LPDIRECT3DDEVICE9   pDevice,
  _In_  HDC                 hDC,
  _In_  LPCTSTR             pText,
  _In_  FLOAT               Deviation,
  _In_  FLOAT               Extrusion,
  _Out_ LPD3DXMESH          *ppMesh,
  _Out_ LPD3DXBUFFER        *ppAdjacency,
  _Out_ LPGLYPHMETRICSFLOAT pGlyphMetrics
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to the device that created the mesh.

</dd> <dt>

*hDC* \[in\]
</dt> <dd>

Type: **HDC**

Device context, containing the font for output. The font selected by the device context must be a TrueType font.

</dd> <dt>

*pText* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string that specifies the text to generate. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*Deviation* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Maximum chordal deviation from TrueType font outlines.

</dd> <dt>

*Extrusion* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Amount to extrude text in the negative z-direction.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Pointer to the returned mesh.

</dd> <dt>

*ppAdjacency* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to a buffer containing adjacency information. May be **NULL**.

</dd> <dt>

*pGlyphMetrics* \[out\]
</dt> <dd>

Type: **[**LPGLYPHMETRICSFLOAT**](/windows/win32/api/wingdi/ns-wingdi-glyphmetricsfloat)**

Pointer to an array of [**GLYPHMETRICSFLOAT**](/windows/win32/api/wingdi/ns-wingdi-glyphmetricsfloat) structures that contain the glyph metric data. Each element contains information about the position and orientation of the corresponding glyph in the string. The number of elements in the array should be equal to the number of characters in the string. Note that the origin in each structure is not relative to the entire string, but rather is relative to that character cell. To compute the entire bounding box, add the increment for each glyph while traversing the string. If you are not concerned with the glyph sizes, set this parameter to **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateTextW. Otherwise, the function call resolves to D3DXCreateTextA because ANSI strings are being used.

This function creates a mesh with the D3DXMESH\_MANAGED creation option and [D3DFVF\_XYZ \| D3DFVF\_NORMAL](d3dfvf.md) flexible vertex format (FVF).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9shape.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>    |



## See also

<dl> <dt>

[Shape Drawing Functions](dx9-graphics-reference-d3dx-functions-shape.md)
</dt> </dl>

 

 
