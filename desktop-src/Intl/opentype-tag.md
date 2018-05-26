---
Description: Defines a 4-byte array that contains four 8-bit ASCII values of space, A-Z, or a-z to identify OpenType script, language, and font feature tags.
ms.assetid: 188ad9a1-e0eb-411f-b6df-8c394d122d6f
title: OPENTYPE\_TAG
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

[**ScriptGetFontAlternateGlyphs**](/windows/win32/Usp10/nf-usp10-scriptgetfontalternateglyphs?branch=master)
</dt> <dt>

[**ScriptGetFontFeatureTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontfeaturetags?branch=master)
</dt> <dt>

[**ScriptGetFontLanguageTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontlanguagetags?branch=master)
</dt> <dt>

[**ScriptGetFontScriptTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontscripttags?branch=master)
</dt> <dt>

[**ScriptItemizeOpenType**](/windows/win32/usp10/nf-usp10-scriptitemizeopentype?branch=master)
</dt> <dt>

[**ScriptPlaceOpenType**](/windows/win32/Usp10/nf-usp10-scriptplaceopentype?branch=master)
</dt> <dt>

[**ScriptPositionSingleGlyph**](/windows/win32/Usp10/nf-usp10-scriptpositionsingleglyph?branch=master)
</dt> <dt>

[**ScriptShapeOpenType**](/windows/win32/Usp10/nf-usp10-scriptshapeopentype?branch=master)
</dt> <dt>

[**ScriptSubstituteSingleGlyph**](/windows/win32/Usp10/nf-usp10-scriptsubstitutesingleglyph?branch=master)
</dt> </dl>

 

 




