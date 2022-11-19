---
description: Returns information about the placement and orientation of a glyph in a character cell.
ms.assetid: 80a78e68-6f88-4cd2-bb7b-0c608ae700aa
title: ID3DXFont::GetGlyphData method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXFont.GetGlyphData
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont::GetGlyphData method

Returns information about the placement and orientation of a glyph in a character cell.

## Syntax


```C++
HRESULT GetGlyphData(
  [in]  UINT               Glyph,
  [out] LPDIRECT3DTEXTURE9 *ppTexture,
  [out] RECT               *pBlackBox,
  [out] POINT              *pCellInc
);
```



## Parameters

<dl> <dt>

*Glyph* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Glyph identifier.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9)\***

Address of a pointer to a [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) object that contains the glyph.

</dd> <dt>

*pBlackBox* \[out\]
</dt> <dd>

Type: **[**RECT**](/windows/win32/api/windef/ns-windef-rect)\***

Pointer to the smallest rectangle object that completely encloses the glyph.

</dd> <dt>

*pCellInc* \[out\]
</dt> <dd>

Type: **[**POINT**](../winprog/windows-data-types.md)\***

Pointer to the two-dimensional vector that connects the origin of the current character cell to the origin of the next character cell. See [**POINT**](../winprog/windows-data-types.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 
