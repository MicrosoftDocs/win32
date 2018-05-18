---
Description: 'Load formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.'
ms.assetid: '0e5380fc-7a01-4e09-9c18-22087be56780'
title: 'ID3DX10Font::PreloadText method'
---

# ID3DX10Font::PreloadText method

Load formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.

## Syntax


```C++
HRESULT PreloadText(
  [in] LPCSTR pString,
  [in] INT    Count
);
```



## Parameters

<dl> <dt>

*pString* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to a string of characters to be loaded into video memory. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR; otherwise, the data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**INT**](winprog.windows_data_types)**

Number of characters in the text string.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to PreloadTextW. Otherwise, the function call resolves to PreloadTextA because ANSI strings are being used.

This method generates textures that contain glyphs that represent the input text. The glyphs are drawn as a series of triangles.

Text will not be rendered to the device; ID3DX10Font::DrawText must still be called to render the text. However, by preloading text into video memory, ID3DX10Font::DrawText will use substantially fewer CPU resources.

This method internally converts characters to glyphs using the GDI function [GetCharacterPlacement](http://msdn2.microsoft.com/en-us/library/ms534004.aspx).

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

 

 




