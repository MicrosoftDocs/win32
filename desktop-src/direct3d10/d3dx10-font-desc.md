---
description: Defines font attributes.
ms.assetid: 66e8a320-2b83-4766-a9a7-5571ee6c9f2a
title: D3DX10_FONT_DESC structure (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_FONT_DESC
api_type: 
- HeaderDef
api_location: 
- D3DX10.h
---

# D3DX10\_FONT\_DESC structure

Defines font attributes.

## Syntax


```C++
typedef struct D3DX10_FONT_DESC {
  INT   Height;
  UINT  Width;
  UINT  Weight;
  UINT  MipLevels;
  BOOL  Italic;
  BYTE  CharSet;
  BYTE  OutputPrecision;
  BYTE  Quality;
  BYTE  PitchAndFamily;
  TCHAR FaceName[LF_FACESIZE];
} D3DX10_FONT_DESC, *LPD3DX10_FONT_DESC;
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

Number of mipmap levels requested. If this value is zero or D3DX\_DEFAULT, a complete mipmap chain is created. If the value is 1, the texture space is mapped identically to the screen space.

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

**FaceName\[LF\_FACESIZE\]**
</dt> <dd>

Type: **TCHAR**

</dd> <dd>

A NULL-terminated string that specifies the typeface name of the font. The length of the string must not exceed 32 characters, including the terminating **NULL** character. If FaceName is an empty string, the first font that matches the other specified attributes will be used. If the compiler settings require Unicode, the data type TCHAR resolves to WCHAR; otherwise, the data type resolves to CHAR. See Remarks.

</dd> </dl>

## Remarks

The compiler setting also determines the structure type. If Unicode is defined, the D3DX10\_FONT\_DESC structure type resolves to a D3DX10\_FONT\_DESCW; otherwise the structure type resolves to a D3DX10\_FONT\_DESCA.

Possible values of the above members are given in the GDI [LOGFONT](/previous-versions//ms533931(v=vs.85)) structure.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 
