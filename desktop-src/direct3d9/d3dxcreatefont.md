---
description: Creates a font object for a device and font.
ms.assetid: 3e65dfdc-9608-420c-9672-c38289d13ab1
title: D3DXCreateFont function (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateFont
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreateFont function

Creates a font object for a device and font.

## Syntax


```C++
HRESULT D3DXCreateFont(
  _In_  LPDIRECT3DDEVICE9 pDevice,
  _In_  INT               Height,
  _In_  UINT              Width,
  _In_  UINT              Weight,
  _In_  UINT              MipLevels,
  _In_  BOOL              Italic,
  _In_  DWORD             CharSet,
  _In_  DWORD             OutputPrecision,
  _In_  DWORD             Quality,
  _In_  DWORD             PitchAndFamily,
  _In_  LPCTSTR           pFacename,
  _Out_ LPD3DXFONT        *ppFont
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface, the device to be associated with the font object.

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

Type: **[**DWORD**](../winprog/windows-data-types.md)**

The character set of the font.

</dd> <dt>

*OutputPrecision* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies how Windows should attempt to match the desired font sizes and characteristics with actual fonts. Use OUT\_TT\_ONLY\_PRECIS for instance, to ensure that you always get a TrueType font.

</dd> <dt>

*Quality* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies how Windows should match the desired font with a real font. It applies to raster fonts only and should not affect TrueType fonts.

</dd> <dt>

*PitchAndFamily* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Pitch and family index.

</dd> <dt>

*pFacename* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

String containing the typeface name. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*ppFont* \[out\]
</dt> <dd>

Type: **[**LPD3DXFONT**](id3dxfont.md)\***

Returns a pointer to an [**ID3DXFont**](id3dxfont.md) interface, representing the created font object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The creation of an ID3DXFont object requires that the device supports 32-bit color.

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXCreateFontW. Otherwise, the function call resolves to D3DXCreateFontA because ANSI strings are being used.

If you want more information about font parameters, see [The Logical Font](../gdi/creating-a-logical-font.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](dx9-graphics-reference-d3dx-functions-general-purpose.md)
</dt> </dl>

 

 
