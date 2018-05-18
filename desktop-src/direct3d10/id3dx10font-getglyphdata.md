---
Description: 'Return information about the placement and orientation of a glyph in a character cell.'
ms.assetid: '1114b06a-c0f0-4c2a-86ad-2ed72bee4049'
title: 'ID3DX10Font::GetGlyphData method'
---

# ID3DX10Font::GetGlyphData method

Return information about the placement and orientation of a glyph in a character cell.

## Syntax


```C++
HRESULT GetGlyphData(
  [in]  UINT                     Glyph,
  [out] ID3D10ShaderResourceView **ppTexture,
  [in]  RECT                     *pBlackBox,
  [in]  POINT                    *pCellInc
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

Type: **[**ID3D10ShaderResourceView**](id3d10shaderresourceview.md)\*\***

Address of a pointer to a ID3D10Texture object that contains the glyph.

</dd> <dt>

*pBlackBox* \[in\]
</dt> <dd>

Type: **[**RECT**](gdi.rect)\***

Pointer to the smallest rectangle object that completely encloses the glyph. See [RECT](http://msdn2.microsoft.com/en-us/library/ms536136.aspx).

</dd> <dt>

*pCellInc* \[in\]
</dt> <dd>

Type: **POINT\***

Pointer to the two-dimensional vector that connects the origin of the current character cell to the origin of the next character cell. See [POINT](http://msdn2.microsoft.com/en-us/library/ms536119.aspx).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Font](id3dx10font.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




