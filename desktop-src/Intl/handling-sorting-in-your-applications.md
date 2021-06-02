---
description: Some applications, such as Microsoft Active Directory, Microsoft Exchange, and Microsoft Access, maintain a sortable database of locale and language strings indexed by name (UTF-16 string), and their associated sorting weights.
ms.assetid: c8fc32bd-02bd-4a40-a836-d9ad9f69c209
title: Handling Sorting in Your Applications
ms.topic: article
ms.date: 03/04/2020
---

# Handling Sorting in Your Applications

Some applications, such as Microsoft Active Directory, Microsoft Exchange, and Microsoft Access, maintain a sortable database of locale and language strings indexed by name (UTF-16 string), and their associated sorting weights.

[Sorting](sorting.md) is usually intuitive for users in their own locales. However, it can be non-intuitive for application developers. This topic discusses considerations for handling sorting in your applications. Sorting can be either linguistic or ordinal (non-linguistic).

## Sorting Functions

You can use a variety of sorting functions in your applications:

-   NLS string comparison functions. Examples are [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) and [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal), [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa), [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex), [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex), and [**FindStringOrdinal**](/windows/desktop/api/Libloaderapi/nf-libloaderapi-findstringordinal). See [Security Considerations: International Features](security-considerations--international-features.md) for a discussion of security issues related to the string comparison functions.
-   Wrapper functions that internally call the string comparison functions. The most common functions are [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa) and [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia), which call [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw).

Usually the sorting functions evaluate strings character by character. However, many languages have multiple-character elements, such as the two-character pair "CH" in traditional Spanish. [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) and [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) use the application-supplied locale identifier or name to identify multiple-character elements. In contrast, [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa), and [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia) use the user's locale.

Another example is Vietnamese, which contains many two-character elements, such as the valid uppercase, title case, and lowercase forms of "GI", which are "GI, "Gi", and "gi", respectively. Any of these forms is treated as a as a single sorting element and, if casing is ignored, compares as equal. However, because "gI" is not valid as a single element, [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa), and [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia) treat "gI" as two separate elements.

The functions [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa), [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia), [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa), [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex), [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), and [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex) all default to use of a "word sort" technique. For this type of sort, all punctuation marks and other nonalphanumeric characters, except for the hyphen and the apostrophe, come before any alphanumeric character. The hyphen and the apostrophe are treated differently from the other nonalphanumeric characters to ensure that words such as "coop" and "co-op" stay together in a sorted list.

Instead of a word sort, the application can request a "string sort" technique from the sorting functions by specifying the SORT\_STRINGSORT flag. A string sort treats the hyphen and apostrophe just like any other nonalphanumeric character. Their positions in the sorting sequence are before the alphanumeric characters.

The following table compares the results of a word sort with the results of a string sort. 

| Word Sort | String Sort |
|-----------|-------------|
| billet    | bill's      |
| bills     | billet      |
| bill's    | bills       |
| cannot    | can't       |
| cant      | cannot      |
| can't     | cant        |
| con       | co-op       |
| coop      | con         |
| co-op     | coop        |



 

## Sort Strings Linguistically

The [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) and [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) functions test for linguistic equality. Your applications should use these functions with the correct locale for sorting strings linguistically.

> [!Note]  
> For compatibility with Unicode, an application should prefer [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) or the Unicode version of [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw). Another reason for preferring [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) is that Microsoft is migrating toward the use of locale names instead of locale identifiers for new locales, for interoperability reasons. Any application that runs only on Windows Vista and later should use [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex).

 

Another way of testing for linguistic equality is to use [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa) or [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia), which always use a word sort. The [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia) function calls [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) with the NORM\_IGNORECASE flag, while [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa) calls it without that flag. For an overview of the use of the wrapper functions, see [**Strings**](../menurc/strings.md).

The functions retrieve linguistically appropriate results for all locales. User expectations for different locales can differ significantly in sorting behavior, as shown in the following examples.

-   Many locales equate the ae ligature (æ) with the letters ae. However, Icelandic (Iceland) considers it a separate letter and places it after Z in the sorting sequence.
-   The A Ring (Å) normally sorts with merely a diacritic difference from A. However, Swedish (Sweden) places the A Ring after Z in the sorting sequence.

The functions attempt to verify rigorously that code points defined in the Unicode standard are canonically equal to a string of equivalent code points. For example, the code point that represents a lowercase "u" with a dieresis (ü) is canonically equal to a lowercase "u" combined with the dieresis (¨). Note, however, that canonical equivalence is not always possible.

As almost all data entered using Windows keyboards and input method editors (IMEs) conforms to the form C normalization defined in the Unicode standard, converting incoming data from other platforms using the NLS Unicode normalization functions provides most consistent results, especially for locales that use the Tibetan script or the Hangul script for modern Hangul. For more information on Unicode normalization support in Windows Vista and later, see [Using Unicode Normalization to Represent Strings](using-unicode-normalization-to-represent-strings.md).

When string comparison follows the user's language preference, for example, when sorting items for an ordered ListView control, the application can do one of the following:

-   Call [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa) or [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia) with the user's locale.
-   Call [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) or [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) to define a locale for the comparison, to pass additional flags, to embed null characters, or to pass explicit lengths to match parts of a string.

When the results of the comparison should be consistent regardless of locale, for example, when comparing retrieved data against a predefined list or an internal value, the application should use [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) or [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) with the *Locale* parameter set to LOCALE\_INVARIANT. For [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), either of the following calls will match even if mystr is "INLAP". In this case, a locale-sensitive call to [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia) will fail if the current locale is Vietnamese.

On Windows XP:


```C++
int iReturn = CompareString(LOCALE_INVARIANT, NORM_IGNORECASE, mystr, -1, _T("InLap"), -1);
```



On earlier operating systems:


```C++
DWORD lcid = MAKELCID(MAKELANGID(LANG_ENGLISH, SUBLANG_ENGLISH_US), SORT_DEFAULT);
int iReturn = CompareString(lcid, NORM_IGNORECASE, mystr, -1, _T("InLap"), -1);
```



## Sort Strings Ordinally

For ordinal (non-linguistic) sorting, your applications should always use the [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) function.

> [!Note]  
> This function is only available for Windows Vista and later.

 

[**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) compares two [Unicode](unicode.md) strings to test for binary equality, as opposed to linguistic equality. Examples of such non-linguistic strings are NTFS file names, environment variables, and the names of mutexes, named pipes, or mailslots. Except for the option of case-insensitivity, this function disregards all non-binary equivalences. Unlike some other sorting functions, it tests all code points for equality, including those that are not given any weight in linguistic sorting schemes.

All of the following statements apply to [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) in binary comparisons, but not to [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**lstrcmp**](/windows/win32/api/winbase/nf-winbase-lstrcmpa), or [**lstrcmpi**](/windows/win32/api/winbase/nf-winbase-lstrcmpia).

-   Canonically equivalent sequences in Unicode, such as LATIN SMALL LETTER A WITH RING ABOVE (U+00e5) and LATIN SMALL LETTER A + COMBINING RING ABOVE (U+0061 U+030a), are not equal even though they appear identical ("å").
-   Canonically similar strings in Unicode, such as LATIN LETTER SMALL CAPITAL Y (U+028f) and LATIN CAPITAL LETTER Y (U+0059), which look very similar ("ʏ" and "Y") and vary only by some special case weights in the linguistic tables, are considered to be entirely dissimilar characters. Even if the application sets *bIgnoreCase* to **TRUE**, these strings compare as different.
-   Code points that are defined but have no linguistic sorting weight, such as ZERO WIDTH JOINER (U+200d), are treated as having their code point weights.
-   Code points that are defined in later versions of Unicode but have no weight in current linguistic tables are treated as having their code point weights.
-   Code points that are undefined by Unicode are treated as having their code point weights.
-   When the application sets *bIgnoreCase* to **TRUE**, the function maps case using the operating system uppercasing table, instead of the information in the linguistic sorting tables. Thus the mapping is independent of locale.

For more information about canonically equivalent sequences in Unicode and canonically similar strings in Unicode, see [Using Unicode Normalization to Represent Strings](using-unicode-normalization-to-represent-strings.md).

## Sort Code Points

Some Unicode code points have no weight, for example, ZERO WIDTH NON JOINER, U+200c. The sorting functions intentionally evaluate the no-weight code points as equivalent because they have no weight in sorting. On Windows Vista and later, the application can sort these code points by calling the NLS string comparison functions, particularly [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal), for evaluation of all code points in a literal, binary sense, for example, in password validation. On pre-Windows Vista operating systems, the application should use the C runtime function **strcmp** or **wcscmp**.

Sorting functions ignore diacritics, such as NON SPACING BREVE, U+0306, when the application specifies the hlink\_NONSPACE flag. Similarly, these functions ignore symbols, for example, EQUALS SIGN, U+003d , when the hlink\_SYMBOLS flag is specified. On Windows Vista and later, the application calls [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) for evaluation of diacritics and symbol code points in a literal, binary sense. On pre-Windows Vista operating systems, the application should use **strcmp** or **wcscmp**.

Some code points, such as 0xFFFF and 0x058b, are currently not assigned in Unicode. These code points do not receive any weight in sorting, and should never be passed to the sorting functions. The application should use [**IsNLSDefinedString**](/windows/desktop/api/Winnls/nf-winnls-isnlsdefinedstring) to detect non-Unicode code points in a data stream.

> [!Note]  
> Results of [**IsNLSDefinedString**](/windows/desktop/api/Winnls/nf-winnls-isnlsdefinedstring) might vary depending on the Unicode version passed if a character is added to Unicode in a later version and it is subsequently added to the Windows sorting tables. For more information, see [Use Sort Versioning](#use-sort-versioning).

 

## Sort Digits as Numbers

On Windows 7 and later, the application can call [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa), or [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex) using the SORT\_DIGITSASNUMBERS flag. This flag supports sorting that treats digits as numbers, for example, sorting of "2" before "10".

Note that the use of this flag is not appropriate for hexadecimal digits such as the following. <dl> 01AF  
1BCD  
002A  
12FA  
AB1C  
AB02  
AB12  
</dl>

In this case the "numbers" are sorted in order, but the user perceives a poorly sorted hexadecimal list.

## Map Strings

The application uses the [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) or [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex) function to map strings, if LCMAP\_SORTKEY is not specified. A mapped string is null-terminated if the source string is null-terminated.

When transforming between uppercase and lowercase, the function does not guarantee that a single character will map to a single character. For example, the LCMAP\_LOWERCASE and LCMAP\_UPPERCASE flags may map the German Sharp S ("ß") to itself. Alternatively, the LCMAP\_UPPERCASE flag may map "ß" to "SS" and the LCMAP\_LOWERCASE flag may map "SS" to "ß". The behavior depends on the NLS version.

When transforming between uppercase and lowercase, the function is not sensitive to context. For example, while the LCMAP\_UPPERCASE flag correctly maps both Greek lowercase sigma ("σ") and Greek lowercase final sigma ("ς") to Greek uppercase sigma ("Σ"), the LCMAP\_LOWERCASE flag always maps "Σ" to "σ", never to "ς".

By default, the function maps the lowercase "i" to the uppercase "I", even when the *Locale* parameter specifies Turkish or Azerbaijani. To override this behavior for Turkish or Azerbaijani, the application should specify LCMAP\_LINGUISTIC\_CASING. If this flag is specified with the appropriate locale, "ı" (lowercase dotless I) is the lowercase form of "I" (uppercase dotless I) and "i" (lowercase dotted I) is the lowercase form of "İ" (uppercase dotted I).

If the LCMAP\_HIRAGANA flag is specified to map katakana characters to hiragana characters, and LCMAP\_FULLWIDTH is not specified, [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) or [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex) only maps full-width characters to hiragana. In this case, any half-width katakana characters are placed as in the destination string, with no mapping to hiragana. The application must specify LCMAP\_FULLWIDTH to map half-width katakana characters to hiragana. The reason for this restriction is that all hiragana characters are full-width characters.

If the application needs to strip characters from the source string, it can call the mapping function with the NORM\_IGNORESYMBOLS and NORM\_IGNORENONSPACE flags set, and all other flags cleared. If the application does this with a source string that is not null-terminated, it is possible for the function to return an empty string and not return an error.

## Create Sort Keys

When the application specifies LCMAP\_SORTKEY, [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) or [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex) generates a sort key, a binary array of byte values. The sort key is not a true string and its values represent the sorting behavior of the source string, but are not meaningful display values.

> [!Note]  
> The function ignores the Arabic kashida during generation of a sort key. If an application calls the function to create a sort key for a string containing an Arabic kashida, the function creates no sort key value.

 

The sort key can contain an odd number of bytes. The LCMAP\_BYTEREV flag only reverses an even number of bytes. The last byte (odd-positioned) in the sort key is not reversed. If the terminating 0x00 byte is an odd-positioned byte, it remains the last byte in the sort key. If the terminating 0x00 byte is an even-positioned byte, it exchanges positions with the byte that precedes it.

When generating the sort key, the function treats the hyphen and apostrophe differently from other punctuation symbols, so that words such as "coop" and "co-op" stay together in a list. All punctuation symbols other than the hyphen and apostrophe sort before alphanumeric characters. The application can change this behavior by setting the SORT\_STRINGSORT flag, as described in [Sorting Functions](#sorting-functions).

When used in [memcmp](/cpp/c-runtime-library/reference/memcmp-wmemcmp), the sort key produces the same order as when the source string is used in [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) or [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex). The [memcmp](/cpp/c-runtime-library/reference/memcmp-wmemcmp) function should be used instead of [strcmp](/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp), because the sort key can have embedded null bytes.

## Use Sort Versioning

A [sorting](sorting.md) table has two numbers that identify its version: the defined version and the NLS version. Both numbers are DWORD values, composed of a major value and a minor value. The first byte of a value is reserved, the next two bytes represent the major version, and the last byte represents the minor version. In hexadecimal terms, the pattern is 0xRRMMMMmm, where R equals Reserved, M equals major, and m equals minor. For example, a major version of 3 with a minor version of 4 is represented as 0x304.

The defined version identifies the repertoire of code points and is the same for all locales. The major version increments to indicate changes to existing code points. The minor version increments to indicate that code points have been added, but that no previously existing code points have been changed.

The NLS version is specific to a [locale identifier](locale-identifiers.md) or [locale name](locale-names.md), and tracks changes to code point weights for the affected locale. The major version increments when weights are changed for code points that were already sortable. The minor version increments when new code points are assigned weights, but all other previously sortable code point weights remain unchanged.

> [!Note]  
> For a major version, one or more code points are changed so that the application must re-index all data for comparisons to be valid. For a minor version, nothing is moved but code points are added. For this type of version, the application only has to re-index strings with previously unsortable values.

 

> [!IMPORTANT]
> The major version has been changed in Windows 8. Data created under earlier versions of Windows must be re-indexed.

 

Both the defined and NLS versions apply to sortable code points retrieved using the [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) or [**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex) function with the LCMAP\_SORTKEY flag, and also used by the [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex), [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), and [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex) functions. If one or more code points in a string are unsortable, then the [**IsNLSDefinedString**](/windows/desktop/api/Winnls/nf-winnls-isnlsdefinedstring) function returns **FALSE** when that string is passed to it as a parameter.

The application can call either [**GetNLSVersion**](/windows/desktop/api/Winnls/nf-winnls-getnlsversion) or [**GetNLSVersionEx**](/windows/desktop/api/Winnls/nf-winnls-getnlsversionex) to retrieve both the defined version and the NLS version for a sorting table.

## Index the Database

For performance reasons, the application should follow this procedure when indexing the database.

**To properly index the database**

1.  For each function, store the NLS version, the sort keys of that version, and an indication of sortability for each indexed string.
2.  When the minor version increments, re-index previously unsortable strings. The strings affected in this update should be confined to the ones for which [**IsNLSDefinedString**](/windows/desktop/api/Winnls/nf-winnls-isnlsdefinedstring) has previously returned **FALSE**.
3.  When the major version increments, re-index all strings because the updated weights might change the behavior of any string. Major version releases are very infrequent.

Database indexing problems can arise for the following reasons:

-   A later operating system can define code points that are undefined for an earlier operating system, thus changing the sort.
-   Code points can have different sorting weights in different operating systems, due to corrections in language support.

To minimize the necessity to re-index the database in these circumstances, the application can use [**IsNLSDefinedString**](/windows/desktop/api/Winnls/nf-winnls-isnlsdefinedstring) to differentiate defined from undefined strings so that the application can reject strings with undefined code points. Use of [**GetNLSVersion**](/windows/desktop/api/Winnls/nf-winnls-getnlsversion) or [**GetNLSVersionEx**](/windows/desktop/api/Winnls/nf-winnls-getnlsversionex) allows the application to determine if an NLS change affects the locale used for a particular index table. If the change has no effect on the locale, the application has no need to re-index the table.

## Examples

The following table illustrates the effects of certain flags used with the sorting functions. In each case, the selection of flags determines whether two different characters are considered equal for sorting purposes.



| Character 1                                                        | Character 2                                             | Default | NORM\_IGNOREWIDTH | NORM\_IGNOREKANA | NORM\_IGNOREWIDTH\| NORMIGNOREKANA |
|--------------------------------------------------------------------|---------------------------------------------------------|---------|-------------------|------------------|------------------------------------|
| "あ"<br/> U+3042 HIRAGANA LETTER A<br/>                | "ガ"<br/> U+30A2 KATAKANA LETTER A<br/>     | Unequal | Unequal           | Equal            | Equal                              |
| "ｵ"<br/> U+FF75 HALFWIDTH KATAKANA LETTER O<br/>       | "オ"<br/> U+30AA KATAKANA LETTER O<br/>     | Unequal | Equal             | Unequal          | Equal                              |
| "Ｂ"<br/> U+FF22 FULLWIDTH LATIN CAPITAL LETTER B<br/> | "B"<br/> U+0042 LATIN CAPITAL LETTER B<br/> | Unequal | Equal             | Unequal          | Equal                              |



 

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Sorting](sorting.md)
</dt> <dt>

[Retrieving and Setting Locale Information](retrieving-and-setting-locale-information.md)
</dt> <dt>

[Using Unicode Normalization to Represent Strings](using-unicode-normalization-to-represent-strings.md)
</dt> <dt>

[Security Considerations: International Features](security-considerations--international-features.md)
</dt> <dt>

[**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw)
</dt> <dt>

[**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex)
</dt> <dt>

[**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal)
</dt> <dt>

[**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring)
</dt> <dt>

[**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex)
</dt> <dt>

[**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa)
</dt> <dt>

[**LCMapStringEx**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringex)
</dt> </dl>

 

 
