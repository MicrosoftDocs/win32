---
Description: 'Loads a series of characters into video memory to improve the efficiency of rendering to the device.'
ms.assetid: 'bb49842e-99de-406b-bf4b-139d6499f96e'
title: 'ID3DXFont::PreloadCharacters method'
---

# ID3DXFont::PreloadCharacters method

Loads a series of characters into video memory to improve the efficiency of rendering to the device.

## Syntax


```C++
HRESULT PreloadCharacters(
  [in] UINT First,
  [in] UINT Last
);
```



## Parameters

<dl> <dt>

*First* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

ID of the first character to be loaded into video memory.

</dd> <dt>

*Last* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

ID of the last character to be loaded into video memory.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

This method generates textures containing glyphs that represent the input characters. The glyphs are drawn as a series of triangles.

Characters will not be rendered to the device; [**DrawText**](id3dxfont--drawtext.md) must still be called to render the characters. However, by pre-loading characters into video memory, **DrawText** will use substantially fewer CPU resources.

This method internally converts characters to glyphs using the GDI function [**GetCharacterPlacement**](gdi.getcharacterplacement).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




