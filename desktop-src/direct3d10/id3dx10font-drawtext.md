---
description: Draw formatted text. This method supports ANSI and Unicode strings.
ms.assetid: 205e9e23-4293-4195-9e41-d8c06dabd285
title: ID3DX10Font::DrawText method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font.DrawText
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Font::DrawText method

Draw formatted text. This method supports ANSI and Unicode strings.

## Syntax


```C++
INT DrawText(
  [in] LPD3DX10SPRITE pSprite,
  [in] LPCTSTR        pString,
  [in] INT            Count,
  [in] LPRECT         pRect,
  [in] UINT           Format,
  [in] D3DXCOLOR      Color
);
```



## Parameters

<dl> <dt>

*pSprite* \[in\]
</dt> <dd>

Type: **[**LPD3DX10SPRITE**](id3dx10sprite.md)**

Pointer to an ID3DX10Sprite object that contains the string you wish to draw. Can be **NULL**, in which case Direct3D will render the string with its own sprite object. To improve efficiency, a sprite object should be specified if ID3DX10Font::DrawText is to be called more than once in a row.

</dd> <dt>

*pString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Pointer to a string to draw. If UNICODE is defined, this parameter type resolves to an LPCWSTR, otherwise, the type resolves to an LPCSTR. If the Count parameter is -1, the string must be **NULL** terminated.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**INT**](../winprog/windows-data-types.md)**

The number of characters in the string. If Count is -1, then the pString parameter is assumed to be a pointer to a sprite containing a NULL-terminated string and ID3DX10Font::DrawText computes the character count automatically.

</dd> <dt>

*pRect* \[in\]
</dt> <dd>

Type: **LPRECT**

Pointer to a [RECT](/previous-versions//ms536136(v=vs.85)) structure that contains the rectangle, in logical coordinates, in which the text is to be formatted. As with any RECT object, the coordinate value of the rectangle's right side must be greater than that of its left side. Likewise, the coordinate value of the bottom must be greater than that of the top.

</dd> <dt>

*Format* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Specify the method of formatting the text. It can be any combination of the following values:



| Item                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DT_BOTTOM"></span><span id="dt_bottom"></span>DT\_BOTTOM<br/>             | Justify the text to the bottom of the rectangle. This value must be combined with DT\_SINGLELINE.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="DT_CALCRECT"></span><span id="dt_calcrect"></span>DT\_CALCRECT<br/>       | Tell DrawText to automatically calculate the width and height of the rectangle based on the length of the string you tell it to draw. If there are multiple lines of text, ID3DX10Font::DrawText uses the width of the rectangle pointed to by the pRect parameter and extends the base of the rectangle to bound the last line of text. If there is only one line of text, ID3DX10Font::DrawText modifies the right side of the rectangle so that it bounds the last character in the line. In either case, ID3DX10Font::DrawText returns the height of the formatted text but does not draw the text.<br/> |
| <span id="DT_CENTER"></span><span id="dt_center"></span>DT\_CENTER<br/>             | Center text horizontally in the rectangle.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_EXPANDTABS"></span><span id="dt_expandtabs"></span>DT\_EXPANDTABS<br/> | Expand tab characters. The default number of characters per tab is eight.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="DT_LEFT"></span><span id="dt_left"></span>DT\_LEFT<br/>                   | Align text to the left.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="DT_NOCLIP"></span><span id="dt_noclip"></span>DT\_NOCLIP<br/>             | Draw without clipping. ID3DX10Font::DrawText is somewhat faster when DT\_NOCLIP is used.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="DT_RIGHT"></span><span id="dt_right"></span>DT\_RIGHT<br/>                | Align text to the right.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="DT_RTLREADING"></span><span id="dt_rtlreading"></span>DT\_RTLREADING<br/> | Display text in right-to-left reading order for bidirectional text when a Hebrew or Arabic font is selected. The default reading order for all text is left-to-right.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="DT_SINGLELINE"></span><span id="dt_singleline"></span>DT\_SINGLELINE<br/> | Display text on a single line only. Carriage returns and line feeds do not break the line.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_TOP"></span><span id="dt_top"></span>DT\_TOP<br/>                      | Top-justify text.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="DT_VCENTER"></span><span id="dt_vcenter"></span>DT\_VCENTER<br/>          | Center text vertically (single line only).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="DT_WORDBREAK"></span><span id="dt_wordbreak"></span>DT\_WORDBREAK<br/>    | Break words. Lines are automatically broken between words if a word would extend past the edge of the rectangle specified by the pRect parameter. A carriage return/line feed sequence also breaks the line.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

*Color* \[in\]
</dt> <dd>

Type: **[**D3DXCOLOR**](../direct3d9/d3dxcolor.md)**

Color of the text. See [**D3DXCOLOR**](d3d10-d3dxcolor.md).

</dd> </dl>

## Return value

Type: **[**INT**](../winprog/windows-data-types.md)**

If the function succeeds, the return value is the height of the text in logical units. If DT\_VCENTER or DT\_BOTTOM is specified, the return value is the offset from pRect (top to the bottom) of the drawn text. If the function fails, the return value is zero.

## Remarks

The parameters of this method are very similar to those of the [GDI DrawText](/previous-versions//ms533909(v=vs.85)) function.

This method supports both ANSI and Unicode strings.

Unless the DT\_NOCLIP format is used, this method clips the text so that it does not appear outside the specified rectangle. All formatting is assumed to have multiple lines unless the DT\_SINGLELINE format is specified.

If the selected font is too large for the rectangle, this method does not attempt to substitute a smaller font.

This method supports only fonts whose escapement and orientation are both zero.

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

 

 
