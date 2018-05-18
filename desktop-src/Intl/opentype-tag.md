---
Description: 'Defines a 4-byte array that contains four 8-bit ASCII values of space, A-Z, or a-z to identify OpenType script, language, and font feature tags.'
ms.assetid: '188ad9a1-e0eb-411f-b6df-8c394d122d6f'
title: 'OPENTYPE\_TAG'
---

# OPENTYPE\_TAG

Defines a 4-byte array that contains four 8-bit ASCII values of space, A-Z, or a-z to identify OpenType script, language, and font feature tags.


```C++
typedef ULONG OPENTYPE_TAG;
```



## Remarks

The following examples define representations of OpenType feature tags.

-   The feature tag for the ligature feature is "liga".
-   The language tags for Romanian, Urdu, and Persian are "ROM ", "URD ", and "FAR ", respectively. Note that each of these tags ends with a space.
-   The script tags for Latin and Arabic scripts are "latn" and "arab", respectively.

For more information on OpenType feature tags and the OpenType specification, see <http://www.microsoft.com/typography/otspec/featuretags.htm>.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Redistributable<br/>          | Usp10.dll version 1.600 or greater onWindows XPand later<br/>                |
| Header<br/>                   | <dl> <dt>Usp10.h</dt> </dl> |



## See also

<dl> <dt>

[Uniscribe](uniscribe.md)
</dt> <dt>

[Uniscribe Structures](uniscribe-structures.md)
</dt> <dt>

[**ScriptGetFontAlternateGlyphs**](scriptgetfontalternateglyphs.md)
</dt> <dt>

[**ScriptGetFontFeatureTags**](scriptgetfontfeaturetags.md)
</dt> <dt>

[**ScriptGetFontLanguageTags**](scriptgetfontlanguagetags.md)
</dt> <dt>

[**ScriptGetFontScriptTags**](scriptgetfontscripttags.md)
</dt> <dt>

[**ScriptItemizeOpenType**](scriptitemizeopentype.md)
</dt> <dt>

[**ScriptPlaceOpenType**](scriptplaceopentype.md)
</dt> <dt>

[**ScriptPositionSingleGlyph**](scriptpositionsingleglyph.md)
</dt> <dt>

[**ScriptShapeOpenType**](scriptshapeopentype.md)
</dt> <dt>

[**ScriptSubstituteSingleGlyph**](scriptsubstitutesingleglyph.md)
</dt> </dl>

 

 




