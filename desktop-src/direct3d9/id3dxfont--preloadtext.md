---
Description: Loads formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.
ms.assetid: f2a4e9f5-87c5-46c0-965d-ce1535a6921d
title: ID3DXFontPreloadText method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXFont::PreloadText method

Loads formatted text into video memory to improve the efficiency of rendering to the device. This method supports ANSI and Unicode strings.

## Syntax


```C++
HRESULT PreloadText(
  [in] LPCTSTR *pString,
  [in] INT     Count
);
```



## Parameters

<dl> <dt>

*pString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)\***

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

Text will not be rendered to the device; [**DrawText**](id3dxfont--drawtext.md) must still be called to render the text. However, by preloading text into video memory, **DrawText** will use substantially fewer CPU resources.

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

 

 




