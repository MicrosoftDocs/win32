---
description: Load a series of glyphs into video memory to improve the efficiency of rendering to the device.
ms.assetid: 7d063d52-af2c-44a6-9019-3d546acfbd4a
title: ID3DX10Font::PreloadGlyphs method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font.PreloadGlyphs
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Font::PreloadGlyphs method

Load a series of glyphs into video memory to improve the efficiency of rendering to the device.

## Syntax


```C++
HRESULT PreloadGlyphs(
  [in] UINT First,
  [in] UINT Last
);
```



## Parameters

<dl> <dt>

*First* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

ID of the first glyph to be loaded into video memory.

</dd> <dt>

*Last* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

ID of the last glyph to be loaded into video memory.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

This method generates textures that contain the input glyphs. The glyphs are drawn as a series of triangles.

Glyphs will not be rendered to the device; ID3DX10Font::DrawText must still be called to render the glyphs. However, by pre-loading glyphs into video memory, ID3DX10Font::DrawText will use substantially fewer CPU resources.

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

 

 
