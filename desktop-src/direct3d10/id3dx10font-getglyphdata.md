---
description: Return information about the placement and orientation of a glyph in a character cell.
ms.assetid: 1114b06a-c0f0-4c2a-86ad-2ed72bee4049
title: ID3DX10Font::GetGlyphData method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font.GetGlyphData
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
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

Type: **[**UINT**](../winprog/windows-data-types.md)**

Glyph identifier.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderResourceView**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview)\*\***

Address of a pointer to a ID3D10Texture object that contains the glyph.

</dd> <dt>

*pBlackBox* \[in\]
</dt> <dd>

Type: **[**RECT**](/windows/win32/api/windef/ns-windef-rect)\***

Pointer to the smallest rectangle object that completely encloses the glyph. See [RECT](/previous-versions//ms536136(v=vs.85)).

</dd> <dt>

*pCellInc* \[in\]
</dt> <dd>

Type: **POINT\***

Pointer to the two-dimensional vector that connects the origin of the current character cell to the origin of the next character cell. See [POINT](/previous-versions//ms536119(v=vs.85)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Font](id3dx10font.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
