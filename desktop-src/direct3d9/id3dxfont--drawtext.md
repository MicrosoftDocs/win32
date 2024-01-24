---
description: Draws formatted text. This method supports ANSI and Unicode strings.
ms.assetid: c1c3657e-632e-46a5-91da-e102ac8ef9bb
title: ID3DXFont::DrawText method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXFont.DrawText
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont::DrawText method

Draws formatted text. This method supports ANSI and Unicode strings.

## Syntax


```C++
INT DrawText(
  [in] LPD3DXSPRITE pSprite,
  [in] LPCTSTR      pString,
  [in] INT          Count,
  [in] LPRECT       pRect,
  [in] DWORD        Format,
  [in] D3DCOLOR     Color
);
```



## Parameters

<dl> <dt>

*pSprite* \[in\]
</dt> <dd>

Type: **[**LPD3DXSPRITE**](id3dxsprite.md)**

Pointer to an [**ID3DXSprite**](id3dxsprite.md) object that contains the string. Can be **NULL**, in which case Direct3D will render the string with its own sprite object. To improve efficiency, a sprite object should be specified if **DrawText** is to be called more than once in a row.

</dd> <dt>

*pString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string to draw. If the Count parameter is -1, the string must be null-terminated.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**INT**](../winprog/windows-data-types.md)**

Specifies the number of characters in the string. If Count is -1, then the pString parameter is assumed to be a pointer to a null-terminated string and **DrawText** computes the character count automatically.

</dd> <dt>

*pRect* \[in\]
</dt> <dd>

Type: **[**LPRECT**](../winprog/windows-data-types.md)**

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that contains the rectangle, in logical coordinates, in which the text is to be formatted. The coordinate value of the rectangle's right side must be greater than that of its left side. Likewise, the coordinate value of the bottom must be greater than that of the top.

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the method of formatting the text. It can be any combination of the following values:



| Value                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DT_BOTTOM"></span><span id="dt_bottom"></span><dl> <dt>**DT\_BOTTOM**</dt> </dl>             | Justifies the text to the bottom of the rectangle. This value must be combined with DT\_SINGLELINE.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="DT_CALCRECT"></span><span id="dt_calcrect"></span><dl> <dt>**DT\_CALCRECT**</dt> </dl>       | Determines the width and height of the rectangle. If there are multiple lines of text, **DrawText** uses the width of the rectangle pointed to by the pRect parameter and extends the base of the rectangle to bound the last line of text. If there is only one line of text, **DrawText** modifies the right side of the rectangle so that it bounds the last character in the line. In either case, **DrawText** returns the height of the formatted text but does not draw the text.<br/> |
| <span id="DT_CENTER"></span><span id="dt_center"></span><dl> <dt>**DT\_CENTER**</dt> </dl>             | Centers text horizontally in the rectangle.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_EXPANDTABS"></span><span id="dt_expandtabs"></span><dl> <dt>**DT\_EXPANDTABS**</dt> </dl> | Expands tab characters. The default number of characters per tab is eight.<br/>                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="DT_LEFT"></span><span id="dt_left"></span><dl> <dt>**DT\_LEFT**</dt> </dl>                   | Aligns text to the left.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="DT_NOCLIP"></span><span id="dt_noclip"></span><dl> <dt>**DT\_NOCLIP**</dt> </dl>             | Draws without clipping. **DrawText** is somewhat faster when DT\_NOCLIP is used.<br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="DT_RIGHT"></span><span id="dt_right"></span><dl> <dt>**DT\_RIGHT**</dt> </dl>                | Aligns text to the right.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="DT_RTLREADING"></span><span id="dt_rtlreading"></span><dl> <dt>**DT\_RTLREADING**</dt> </dl> | Displays text in right-to-left reading order for bidirectional text when a Hebrew or Arabic font is selected. The default reading order for all text is left-to-right.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="DT_SINGLELINE"></span><span id="dt_singleline"></span><dl> <dt>**DT\_SINGLELINE**</dt> </dl> | Displays text on a single line only. Carriage returns and line feeds do not break the line.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_TOP"></span><span id="dt_top"></span><dl> <dt>**DT\_TOP**</dt> </dl>                      | Top-justifies text.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="DT_VCENTER"></span><span id="dt_vcenter"></span><dl> <dt>**DT\_VCENTER**</dt> </dl>          | Centers text vertically (single line only).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_WORDBREAK"></span><span id="dt_wordbreak"></span><dl> <dt>**DT\_WORDBREAK**</dt> </dl>    | Breaks words. Lines are automatically broken between words if a word would extend past the edge of the rectangle specified by the pRect parameter. A carriage return/line feed sequence also breaks the line.<br/>                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

*Color* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

Color of the text. For more information, see [**D3DCOLOR**](d3dcolor.md).

</dd> </dl>

## Return value

Type: **[**INT**](../winprog/windows-data-types.md)**

If the function succeeds, the return value is the height of the text in logical units. If DT\_VCENTER or DT\_BOTTOM is specified, the return value is the offset from pRect (top to the bottom) of the drawn text. If the function fails, the return value is zero.

## Remarks

The parameters of this method are very similar to those of the GDI [**DrawText**](/windows/win32/api/winuser/nf-winuser-drawtext) function.

This method supports both ANSI and Unicode strings.

This method must be called inside a [**BeginScene**](/windows/desktop/api) ... [**EndScene**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-endscene) block. The only exception is when an application calls **DrawText** with DT\_CALCRECT to calculate the size of a given block of text.

Unless the DT\_NOCLIP format is used, this method clips the text so that it does not appear outside the specified rectangle. All formatting is assumed to have multiple lines unless the DT\_SINGLELINE format is specified.

If the selected font is too large for the rectangle, this method does not attempt to substitute a smaller font.

This method supports only fonts whose escapement and orientation are both zero.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 
