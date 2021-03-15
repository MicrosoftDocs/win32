---
description: Defines the attributes of a font.
ms.assetid: 6f456f26-3410-4205-a013-e3c12bf0feb1
title: D3DXFONT_DESC structure (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFONT_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9core.h
---

# D3DXFONT\_DESC structure

Defines the attributes of a font.

## Syntax


```C++
typedef struct D3DXFONT_DESC {
  INT   Height;
  UINT  Width;
  UINT  Weight;
  UINT  MipLevels;
  BOOL  Italic;
  BYTE  CharSet;
  BYTE  OutputPrecision;
  BYTE  Quality;
  BYTE  PitchAndFamily;
  TCHAR FaceName;
} D3DXFONT_DESC, *LPD3DXFONT_DESC;
```



## Members

<dl> <dt>

**Height**
</dt> <dd>

Type: **[**INT**](../winprog/windows-data-types.md)**

</dd> <dd>

Height, in logical units, of the font's character cell or character.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Width, in logical units, of characters in the font.

</dd> <dt>

**Weight**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Weight of the font in the range from 0 through 1000.

</dd> <dt>

**MipLevels**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of mip levels requested. If this value is zero or D3DX\_DEFAULT, a complete mipmap chain is created. If the value is 1, the texture space is mapped identically to the screen space.

</dd> <dt>

**Italic**
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

</dd> <dd>

Set to **TRUE** for an Italic font.

</dd> <dt>

**CharSet**
</dt> <dd>

Type: **[**BYTE**](../winprog/windows-data-types.md)**

</dd> <dd>

Character set.

</dd> <dt>

**OutputPrecision**
</dt> <dd>

Type: **[**BYTE**](../winprog/windows-data-types.md)**

</dd> <dd>

Output precision. The output precision defines how closely the output must match the requested font height, width, character orientation, escapement, pitch, and font type.

</dd> <dt>

**Quality**
</dt> <dd>

Type: **[**BYTE**](../winprog/windows-data-types.md)**

</dd> <dd>

Output quality.

</dd> <dt>

**PitchAndFamily**
</dt> <dd>

Type: **[**BYTE**](../winprog/windows-data-types.md)**

</dd> <dd>

Pitch and family of the font.

</dd> <dt>

**FaceName**
</dt> <dd>

Type: **TCHAR**

</dd> <dd>

A null-terminated string or characters that specifies the typeface name of the font. The length of the string must not exceed 32 characters, including the terminating null character. If FaceName is an empty string, the first font that matches the other specified attributes will be used. If the compiler settings require Unicode, the data type TCHAR resolves to WCHAR; otherwise, the data type resolves to CHAR. See Remarks.

</dd> </dl>

## Remarks

The compiler setting also determines the structure type. If Unicode is defined, the D3DXFONT\_DESC structure type resolves to a D3DXFONT\_DESCW; otherwise the structure type resolves to a D3DXFONT\_DESCA.

Possible values of the above members are given in the GDI [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9core.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**GetDesc**](id3dxfont--getdesc.md)
</dt> </dl>

 

 
