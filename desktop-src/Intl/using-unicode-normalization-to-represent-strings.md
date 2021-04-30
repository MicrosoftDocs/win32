---
description: Applications can use Unicode to represent strings in multiple forms.
ms.assetid: 027c9ef5-4012-4d1c-b78c-a4d3f1ccbf35
title: Using Unicode Normalization to Represent Strings
ms.topic: article
ms.date: 05/31/2018
---

# Using Unicode Normalization to Represent Strings

Applications can use Unicode to represent strings in multiple forms. As Unicode acceptance has grown, especially via the Internet, the need has arisen to eliminate non-essential differences in Unicode strings. Multiple representations for a combination of characters complicate software, for example, when a Web server responds to a page request or a linker seeks a particular identifier in a library.

> [!Caution]  
> Different Unicode strings can appear to be visually identical, raising security concerns. For more information, see [Security Considerations: International Features](security-considerations--international-features.md).

 

In response to this requirement, the Unicode Consortium has defined a process called "normalization," which produces one binary representation for any of the equivalent binary representations of a character. Once normalized, two strings are equivalent if and only if they have identical binary representations. The normalization eliminates some differences but preserves case.

To use Unicode normalization, an application can call the [**NormalizeString**](/windows/desktop/api/Winnls/nf-winnls-normalizestring) and [**IsNormalizedString**](/windows/desktop/api/Winnls/nf-winnls-isnormalizedstring) functions for rearrangement of strings acccording to Unicode 4.0 TR\#15. Normalization can help improve security by reducing alternate string representations that have the same linguistic meaning. Remember, however, that normalization cannot eliminate alternate representations entirely.

For a detailed description of the Unicode standards for normalization, refer to [Unicode Standard Annex \#15: Unicode Normalization Forms](https://www.unicode.org/reports/tr15) (UAX \#15).

> [!Caution]  
> Because normalization can change the form of a string, security mechanisms or character validation algorithms should usually be implemented after normalization. For more information, see [Security Considerations: International Features](security-considerations--international-features.md).

 

## Provide Multiple Representations of the Same String

In many cases, Unicode allows multiple representations of what is, linguistically, the same string. For example:

-   Capital A with dieresis (umlaut) can be represented either as a single Unicode code point "Ä" (U+00C4) or the combination of Capital A and the combining Dieresis character ("A" + "¨", that is, U+0041 U+0308). Similar considerations apply for many other characters with diacritic marks.
-   Capital A itself can be represented either in the usual manner (Latin Capital Letter A, U+0041) or by Fullwidth Latin Capital Letter A (U+FF21). Similar considerations apply for the other simple Latin letters (both uppercase and lowercase) and for the katakana characters used in writing Japanese.
-   The string "fi" can be represented either by the characters "f" and "i" (U+0066 U+0069) or by the ligature "ﬁ" (U+FB01). Similar considerations apply for many other combinations of characters for which Unicode defines ligatures.

## Use the Four Defined Normalization Forms

Your applications can perform Unicode normalization using several algorithms, called "normalization forms," that obey different rules. The Unicode Consortium has defined four normalization forms: NFC (form C), NFD (form D), NFKC (form KC), and NFKD (form KD). Each form eliminates some differences but preserves case. Win32 and the .NET Framework support all four normalization forms.

The NLS enumeration type [**NORM\_FORM**](/windows/desktop/api/Winnls/ne-winnls-norm_form) supports the four standard Unicode normalization forms. Forms C and D provide canonical forms for strings. Non-canonical forms KC and KD provide further compatibility, and can reveal certain semantic equivalences that are not apparent in forms C and D. However, they do so at the expense of a certain loss of information, and generally should not be used as a canonical way to store strings.

Of the two canonical forms, form C is a "composed" form and form D is a "decomposed" form. For example, form C uses the single Unicode code point "Ä" (U+00C4), while form D uses ("A" + "¨", that is U+0041 U+0308). These render identically, because "¨" (U+0308) is a combining character. Form D can use any number of code points to represent a single code point used by form C.

If two strings are identical in either form C or form D, they are identical in the other form. Furthermore, when correctly rendered, they display indistinguishably from one another and from the original non-normalized string.

Once normalized, strings cannot be consistently returned to their original representation. For example, if a string with a mixture of composed and decomposed character representations is converted to a normalized form, there is no way to un-normalize it to the original mixed string. Therefore, if an application requires the original representation of the string, it must store that representation explicitly. However, converting between the two canonical forms is reversible. A string in form C can be converted to form D and then back to form C, and the result is identical to the original form C string.

Forms KC and KD are similar to forms C and D, respectively, but these "compatibility forms" have additional mappings of compatible characters to the basic form of each character. Such mappings can cause minor character variations to be lost. They combine certain characters that are visually distinct. For example, they combine full-width and half-width characters with the same semantic meaning, or different forms of the same Arabic letter, or the ligature "ﬁ" (U+FB01) and the character pair "fi" (U+0066 U+0069). They also combine some characters that might sometimes have a different semantic meaning, such as a digit written as a superscript, as a subscript, or enclosed in a circle. Because of this information loss, forms KC and KD generally should not be used as canonical forms of strings, but they are useful for certain applications.

Form KC is a composed form and form KD is a decomposed form. The application can go back and forth between forms KC and KD, but there is no consistent way to go from form KC or KD back to the original string, even if the original string is in form C or D.

Windows, Microsoft applications, and the .NET Framework generally generate characters in form C using normal input methods. For most purposes on Windows, form C is the preferred form. For example, characters in form C are produced by Windows keyboard input. However, characters imported from the Web and other platforms can introduce other normalization forms into the data stream.

The following examples are drawn from UAX \#15, and illustrate the differences among the four normalization forms.



<table>
<thead>
<tr class="header">
<th>Original</th>
<th>Form D</th>
<th>Form C</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&quot;Äffin&quot;</td>
<td>&quot;A\u0308ffin&quot;</td>
<td>&quot;Äffin&quot;</td>
<td rowspan="2">The ffi_ligature (U+FB03) is not decomposed, because it has a compatibility mapping, not a canonical mapping.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>&quot;Ä\uFB03n&quot;</td>
<td>&quot;A\u0308\uFB03n&quot;</td>
<td>&quot;Ä\uFB03n&quot;</td>

</tr>
<tr class="odd">
<td>&quot;Henry IV&quot;</td>
<td>&quot;Henry IV&quot;</td>
<td>&quot;Henry IV&quot;</td>
<td rowspan="2">The ROMAN NUMERAL IV (U+2163) is not decomposed.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>&quot;Henry \u2163&quot;</td>
<td>&quot;Henry \u2163&quot;</td>
<td>&quot;Henry \u2163&quot;</td>

</tr>
<tr class="odd">
<td>ga</td>
<td>ka +ten</td>
<td>ga</td>
<td rowspan="5">Different compatibility equivalents of a single Japanese character do not result in the same string in form C.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>ka +ten</td>
<td>ka +ten</td>
<td>ga</td>

</tr>
<tr class="odd">
<td>hw_ka +hw_ten</td>
<td>hw_ka +hw_ten</td>
<td>hw_ka +hw_ten</td>

</tr>
<tr class="even">
<td>ka +hw_ten</td>
<td>ka +hw_ten</td>
<td>ka +hw_ten</td>

</tr>
<tr class="odd">
<td>hw_ka +ten</td>
<td>hw_ka +ten</td>
<td>hw_ka +ten</td>

</tr>
<tr class="even">
<td>kaks</td>
<td>k <sub>i</sub> + a ₘ + ks <sub>f</sub></td>
<td>kaks</td>
<td>Hangul syllables are maintained under normalization.<br/></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>Original</th>
<th>Form KD</th>
<th>Form KC</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&quot;Äffin&quot;</td>
<td>&quot;A\u0308ffin&quot;</td>
<td>&quot;Äffin&quot;</td>
<td rowspan="2">The ffi_ligature (U+FB03) is decomposed in form KC, but not in form C.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>&quot;Ä\uFB03n&quot;</td>
<td>&quot;A\u0308ffin&quot;</td>
<td>&quot;Äffin&quot;</td>

</tr>
<tr class="odd">
<td>&quot;Henry IV&quot;</td>
<td>&quot;Henry IV&quot;</td>
<td>&quot;Henry IV&quot;</td>
<td rowspan="2">The resulting strings here are identical in form KC.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>&quot;Henry \u2163&quot;</td>
<td>&quot;Henry IV&quot;</td>
<td>&quot;Henry IV&quot;</td>

</tr>
<tr class="odd">
<td>ga</td>
<td>ka +ten</td>
<td>ga</td>
<td rowspan="5">Different compatibility equivalents of a single Japanese character result in the same string in form KC.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>ka +ten</td>
<td>ka +ten</td>
<td>ga</td>

</tr>
<tr class="odd">
<td>hw_ka +hw_ten</td>
<td>ka +ten</td>
<td>ga</td>

</tr>
<tr class="even">
<td>ka +hw_ten</td>
<td>ka +ten</td>
<td>ga</td>

</tr>
<tr class="odd">
<td>hw_ka +ten</td>
<td>ka +ten</td>
<td>ga</td>

</tr>
<tr class="even">
<td>kaks</td>
<td>k <sub>i</sub> + a ₘ + ks <sub>f</sub></td>
<td>kaks</td>
<td>Hangul syllables are maintained under normalization. In earlier Unicode versions, jamo characters like ks <sub>f</sub> had compatibility mappings to k <sub>f</sub> + s <sub>f</sub>. These mappings were removed in Unicode 2.1.9 to ensure that Hangul syllables are maintained.<br/></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> The two tables above have a copyright of © 1998-2006 Unicode, Inc. All Rights Reserved.

 

## Use Composed Forms for Single Glyphs

Many character sequences that correspond to a single glyph do not have composed forms. Even when normalized by form C, a single visual glyph or logical text element can be composed of multiple Unicode code points. For example, several characters used in writing Lithuanian have double diacritics, as they have only decomposed forms. An example is lowercase U with macron and tilde ("ū̃", U+016b U+0303, where the first code point is a lowercase U with macron and the second is a combining acute accent).

## Example

A relevant example can be found in [NLS: Unicode Normalization Sample](nls--unicode-normalization-sample.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Security Considerations: International Features](security-considerations--international-features.md)
</dt> <dt>

[**IsNormalizedString**](/windows/desktop/api/Winnls/nf-winnls-isnormalizedstring)
</dt> <dt>

[**NormalizeString**](/windows/desktop/api/Winnls/nf-winnls-normalizestring)
</dt> </dl>

 

 




