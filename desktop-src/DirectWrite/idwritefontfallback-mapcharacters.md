---
title: IDWriteFontFallback MapCharacters method
description: Determines an appropriate font to use to render the beginning range of text.
ms.assetid: 9D3DBBF7-72D4-473D-A321-E64BC94493D5
keywords:
- MapCharacters method Direct Write
- MapCharacters method Direct Write , IDWriteFontFallback interface
- IDWriteFontFallback interface Direct Write , MapCharacters method
topic_type:
- apiref
api_name:
- IDWriteFontFallback.MapCharacters
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFontFallback::MapCharacters method

Determines an appropriate font to use to render the beginning range of text.

## Syntax


```C++
HRESULT MapCharacters(
                       IDWriteTextAnalysisSource *source,
                       UINT32                    textPosition,
                       UINT32                    textLength,
  [in, optional]       IDWriteFontCollection     *baseFontCollection,
  [in, optional] const wchar_t                   *baseFamilyName,
                       DWRITE_FONT_WEIGHT        baseWeight,
                       DWRITE_FONT_STYLE         baseStyle,
                       DWRITE_FONT_STRETCH       baseStretch,
  [out]                UINT32                    *mappedLength,
  [out]                IDWriteFont               **mappedFont,
  [out]                FLOAT                     *scale
);
```



## Parameters

<dl> <dt>

*source* 
</dt> <dd>

Type: **[**IDWriteTextAnalysisSource**](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalysissource)\***

The text source implementation holds the text and locale.

</dd> <dt>

*textPosition* 
</dt> <dd>

Type: **UINT32**

Starting position to analyze.

</dd> <dt>

*textLength* 
</dt> <dd>

Type: **UINT32**

Length of the text to analyze.

</dd> <dt>

*baseFontCollection* \[in, optional\]
</dt> <dd>

Type: **[**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection)\***

Default font collection to use.

</dd> <dt>

*baseFamilyName* \[in, optional\]
</dt> <dd>

Type: **const wchar\_t\***

Family name of the base font. If you pass null, no matching will be done against the family.

</dd> <dt>

*baseWeight* 
</dt> <dd>

Type: **[**DWRITE\_FONT\_WEIGHT**](/windows/win32/api/dwrite/ne-dwrite-dwrite_font_weight)**

The desired weight.

</dd> <dt>

*baseStyle* 
</dt> <dd>

Type: **[**DWRITE\_FONT\_STYLE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_font_style)**

The desired style.

</dd> <dt>

*baseStretch* 
</dt> <dd>

Type: **[**DWRITE\_FONT\_STRETCH**](/windows/win32/api/dwrite/ne-dwrite-dwrite_font_stretch)**

The desired stretch.

</dd> <dt>

*mappedLength* \[out\]
</dt> <dd>

Type: **UINT32\***

Length of text mapped to the mapped font. This will always be less than or equal to the text length and greater than zero (if the text length is non-zero) so the caller advances at least one character.

</dd> <dt>

*mappedFont* \[out\]
</dt> <dd>

Type: **[**IDWriteFont**](/windows/win32/api/dwrite/nn-dwrite-idwritefont)\*\***

The font that should be used to render the first *mappedLength* characters of the text. If it returns NULL, that means that no font can render the text, and *mappedLength* is the number of characters to skip (rendered with a missing glyph).

</dd> <dt>

*scale* \[out\]
</dt> <dd>

Type: **FLOAT\***

Scale factor to multiply the em size of the returned font by.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                 |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteFontFallback**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontfallback)
</dt> </dl>

 

