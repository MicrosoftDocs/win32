---
description: Creates a font object for a device and font.Note  Instead of using this function, we recommend that you use DirectWrite and the DirectXTK library, SpriteFont class.
ms.assetid: a0dd02f1-c512-46d3-9e83-a785ac3ad7ee
title: D3DX10CreateFont function (D3DX10Core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10CreateFont
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10CreateFont function

Creates a font object for a device and font.

> [!Note]  
> Instead of using this function, we recommend that you use [DirectWrite](../directwrite/direct-write-portal.md) and the [DirectXTK](https://github.com/Microsoft/DirectXTK) library, **SpriteFont** class.

 

## Syntax


```C++
HRESULT D3DX10CreateFont(
  _In_  ID3D10Device *pDevice,
  _In_  INT          Height,
  _In_  UINT         Width,
  _In_  UINT         Weight,
  _In_  UINT         MipLevels,
  _In_  BOOL         Italic,
  _In_  UINT         CharSet,
  _In_  UINT         OutputPrecision,
  _In_  UINT         Quality,
  _In_  UINT         PitchAndFamily,
  _In_  LPCTSTR      pFaceName,
  _Out_ LPD3DX10FONT *ppFont
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\***

Pointer to an ID3D10Device interface, the device to be associated with the font object.

</dd> <dt>

*Height* \[in\]
</dt> <dd>

Type: **[**INT**](../winprog/windows-data-types.md)**

The height of the characters in logical units.

</dd> <dt>

*Width* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The width of the characters in logical units.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Typeface weight. One example is bold.

</dd> <dt>

*MipLevels* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of mipmap levels.

</dd> <dt>

*Italic* \[in\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

True for italic font, false otherwise.

</dd> <dt>

*CharSet* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The character set of the font.

</dd> <dt>

*OutputPrecision* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Specifies how Windows should attempt to match the desired font sizes and characteristics with actual fonts. Use OUT\_TT\_ONLY\_PRECIS for instance, to ensure that you always get a TrueType font.

</dd> <dt>

*Quality* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Specifies how Windows should match the desired font with a real font. It applies to raster fonts only and should not affect TrueType fonts.

</dd> <dt>

*PitchAndFamily* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Pitch and family index.

</dd> <dt>

*pFaceName* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

String containing the typeface name. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*ppFont* \[out\]
</dt> <dd>

Type: **[**LPD3DX10FONT**](id3dx10font.md)\***

Returns a pointer to an ID3DX10Font interface, representing the created font object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateFontW. Otherwise, the function call resolves to D3DXCreateFontA because ANSI strings are being used.

If you want more information about font parameters, see [The Logical Font](/previous-versions//ms533985(v=vs.85)).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 
