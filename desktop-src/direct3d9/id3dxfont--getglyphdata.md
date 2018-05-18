---
Description: 'Returns information about the placement and orientation of a glyph in a character cell.'
ms.assetid: '80a78e68-6f88-4cd2-bb7b-0c608ae700aa'
title: 'ID3DXFont::GetGlyphData method'
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

Type: **[**UINT**](winprog.windows_data_types)**

Glyph identifier.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](idirect3dtexture9.md)\***

Address of a pointer to a [**IDirect3DTexture9**](idirect3dtexture9.md) object that contains the glyph.

</dd> <dt>

*pBlackBox* \[out\]
</dt> <dd>

Type: **[**RECT**](gdi.rect)\***

Pointer to the smallest rectangle object that completely encloses the glyph.

</dd> <dt>

*pCellInc* \[out\]
</dt> <dd>

Type: **[**POINT**](winprog.windows_data_types)\***

Pointer to the two-dimensional vector that connects the origin of the current character cell to the origin of the next character cell. See [**POINT**](winprog.windows_data_types).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




