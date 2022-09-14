---
description: Arabic and many other languages have classical shapes for numbers that are different from the conventional western digits most often used on computers.
ms.assetid: 6b5267d8-b102-410c-bdc9-831555ca2f84
title: Digit Shapes
ms.topic: article
ms.date: 05/31/2018
---

# Digit Shapes

Arabic and many other languages have classical shapes for numbers that are different from the conventional western digits most often used on computers. To avoid ambiguity in naming these shapes, this document uses the following names from the Unicode standard.



| Unicode name of the digits                                     | Country/region where used                                    |
|----------------------------------------------------------------|--------------------------------------------------------------|
| European digits                                                | Europe, the Americas, and many other countries/regions       |
| Arabic-Indic digits                                            | Arabic countries/regions (although many use European digits) |
| Other national digits: Indic digits, Thai digits, and the like | Various countries/regions                                    |



 

Unicode provides separate code points for each digit shape. Thus, to access special language digit shapes, your application can use the relevant Unicode character codes for the digits above, U+0030 through U+0039. These codes are always displayed with the appropriate shape, subject to font availability.

The Unicode character codes U+0030 through U+0039 nominally represent the European digits 0 through 9, but their digit shape can be altered. GDI and DirectWrite text APIs provide mechanisms for applications to control this behavior. (See, for instance, [**ScriptApplyDigitSubstitution**](/windows/desktop/api/Usp10/nf-usp10-scriptapplydigitsubstitution) or [**IDWriteTextAnalysisSink::SetNumberSubstitution**](/windows/win32/api/dwrite/nf-dwrite-idwritetextanalysissink-setnumbersubstitution).) The behavior in some shell controls and user interface frameworks may respond to user locale settings for digit substitution; the [LOCALE\_IDIGITSUBSTITUTION](locale-idigitsubstitution.md) LCTYPE can be used to obtain default digit substitution settings for different locales or the current user's desktop settings for digit substitution.

## Native Digits

Native digits are the digit shapes chosen by the user in the **Number** property sheet in the regional and language options portion of the Control Panel. To find the digit presentation preferred by the user, your application uses the [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) function with the [LOCALE\_SNATIVEDIGITS](locale-snative-constants.md) constant representing the locale information.

> [!Note]  
> Typically, Unicode digit codes are generated in runtime operating system routines. Therefore, common runtime operating systems must be upgraded for the application to inspect [LOCALE\_SNATIVEDIGITS](locale-snative-constants.md) appropriately.

 

## Digit Substitution

The application can use digit substitution to tell the operating system how to print digits U+0030 through U+0039. The [LOCALE\_IDIGITSUBSTITUTION](locale-idigitsubstitution.md) constant controls this operation.

## Digit Shaping for a Single Function

The [ExtTextOut](/windows/win32/api/wingdi/nf-wingdi-exttextouta), [GetCharacterPlacement](/windows/win32/api/wingdi/nf-wingdi-getcharacterplacementa), and [GCP\_RESULTS](/windows/win32/api/wingdi/ns-wingdi-gcp_resultsa) functions have flags that govern the substitution of Unicode codes U+0030 through U+0039 for the duration of the function call. These flags override regional settings in the Control Panel, but do not reset the settings. Also, they do not override the Unicode codes NADS and NODS. The following flags are available.



| Flags                 | Digits used                      | Used in                   |
|-----------------------|----------------------------------|---------------------------|
| ETO\_NUMERICSLATIN    | European digits                  | **ExtTextOut**            |
| ETO\_NUMERICSLOCAL    | Digits appropriate to the locale | **ExtTextOut**            |
| GCP\_NUMERICSLATIN    | European digits                  | **GetCharacterPlacement** |
| GCP\_NUMERICSLOCAL    | Digits appropriate to the locale | **GetCharacterPlacement** |
| GCPCLASS\_LATINNUMBER | European digits                  | **GCP\_RESULTS**          |
| GCPCLASS\_LOCALNUMBER | Digits appropriate to the locale | **GCP\_RESULTS**          |



 

## Related topics

<dl> <dt>

[About National Language Support](about-national-language-support.md)
</dt> <dt>

[**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa)
</dt> <dt>

[**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex)
</dt> </dl>

 

 
