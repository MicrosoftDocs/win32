---
Description: Return information about the placement and orientation of a glyph in a character cell.
ms.assetid: 1114b06a-c0f0-4c2a-86ad-2ed72bee4049
title: ID3DX10Font::GetGlyphData method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**UINT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Glyph identifier.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderResourceView**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview)\*\***

Address of a pointer to a ID3D10Texture object that contains the glyph.

</dd> <dt>

*pBlackBox* \[in\]
</dt> <dd>

Type: **[**RECT**](https://msdn.microsoft.com/windows/desktop/9439cb6c-f2f7-4c27-b1d7-8ddf16d81fe8)\***

Pointer to the smallest rectangle object that completely encloses the glyph. See [RECT](http://msdn2.microsoft.com/en-us/library/ms536136.aspx).

</dd> <dt>

*pCellInc* \[in\]
</dt> <dd>

Type: **POINT\***

Pointer to the two-dimensional vector that connects the origin of the current character cell to the origin of the next character cell. See [POINT](http://msdn2.microsoft.com/en-us/library/ms536119.aspx).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




