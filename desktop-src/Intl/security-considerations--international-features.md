---
description: This topic provides information about security considerations related to International Support features.
ms.assetid: 4034f479-ad29-4c6f-82c6-977f420c4d4d
title: 'Security Considerations: International Features'
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations: International Features

This topic provides information about security considerations related to International Support features. You can use it as a starting point and then see the documentation for the international technology of interest for technology-specific security considerations.

This topic contains the following sections.

-   [Security Considerations for Character Conversion Functions](#security-considerations-for-character-conversion-functions)
-   [Security Considerations for Comparison Functions](#security-considerations-for-comparison-functions)
-   [Security Considerations for Character Sets in File Names](#security-considerations-for-character-sets-in-file-names)
-   [Security Considerations for Internationalized Domain Names](#security-considerations-for-internationalized-domain-names)
-   [Security Considerations for ANSI Functions](#security-considerations-for-ansi-functions)
-   [Security Considerations for Unicode Normalization](#security-considerations-for-unicode-normalization)

## Security Considerations for Character Conversion Functions

[**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) are the Unicode and character set functions most commonly used to convert characters between ANSI and Unicode. These functions have the potential of causing security risks because they count the elements of the input and output buffers differently. For example, [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) takes an input buffer counted in bytes and puts the converted characters into a buffer sized in Unicode characters. When your application uses this function, it must size the buffers correctly to avoid a buffer overrun.

[**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) defaults to "best fit" mapping for code pages, such as 1252. However, this type of mapping allows multiple representations of the same string, potentially leaving your application vulnerable to attack. For example, Latin capital letter A with dieresis ("Ä") might map to Latin capital letter A ("A"); a Unicode character in an Asian language might map to a slash ("/"). The use of the WC\_NO\_BEST\_FIT\_CHARS flag is preferred from a security perspective.

Some code pages, for example, the 5022x (iso-2022-x) code pages, are inherently insecure because they allow multiple representations of the same string. Properly written code performs security checks in the Unicode form, but these types of code pages expand the attack susceptibility of your applications and should be avoided if possible.

## Security Considerations for Comparison Functions

String comparisons can potentially present security issues. Because all comparison functions are slightly different, one function might report two strings as equal, while another function might consider them distinct. The following are several functions your applications can use to compare strings:

-   [lstrcmpi](/windows/win32/api/winbase/nf-winbase-lstrcmpia). Compares two character strings according to the rules of the locale, without case-sensitivity. The function compares the strings by checking the first characters against each other, the second characters against each other, and so on, until it finds an inequality or reaches the ends of the strings.
-   [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa). Compares strings using techniques similar to those of [lstrcmpi](/windows/win32/api/winbase/nf-winbase-lstrcmpia). The only difference is that [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa) performs a case-sensitive string comparison.
-   [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) (Windows Vista and later). Perform a string comparison on an application-supplied locale. [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) is similar to [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw), but it identifies a locale by [locale name](locale-names.md) instead of [locale identifier](locale-identifiers.md). These functions are similar to [lstrcmpi](/windows/win32/api/winbase/nf-winbase-lstrcmpia) and [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa) except that they operate on a specific locale instead of a user-selected locale.
-   [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) (Windows Vista and later). Compares two Unicode strings to test binary equivalence. Except for the option of being case-insensitive, this function disregards all non-binary equivalences, and tests all code points for equality, including code points that are not given any weight in linguistic [sorting](sorting.md) schemes. Note that the other comparison functions mentioned in this topic do not test all code points for equality.
-   [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex) (Windows Vista and later). Locate a Unicode string in another Unicode string. [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex) is similar to [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), except that it identifies a locale by locale name instead of locale identifier.
-   [**FindStringOrdinal**](/windows/desktop/api/Libloaderapi/nf-libloaderapi-findstringordinal) (Windows 7 and later). Locates one Unicode string in another Unicode string. The application should use this function instead of [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring) for all non-linguistic comparisons.

Like [lstrcmpi](/windows/win32/api/winbase/nf-winbase-lstrcmpia) and [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa), [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) evaluates strings character by character. However, many languages have multiple-character elements, for example, the two-character element "CH" in traditional Spanish. Because [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) uses the locale furnished by the application to identify multiple-character elements and [lstrcmpi](/windows/win32/api/winbase/nf-winbase-lstrcmpia) and [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa) use the thread locale, identical strings might not compare as equal.

[**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) ignores undefined characters, and thus returns zero (indicating equal strings) for many string pairs that are quite distinct. A string might contain values that do not map to any character or it might contain characters with semantics outside the domain of the application, such as control characters in a URL. Applications using this function should provide error handlers and test strings to make sure that they are valid before using them.

> [!Note]  
> For Windows Vista and later, [**CompareStringEx**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringex) is similar to [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw). The security issues are identical for these functions.

 

Similar security issues apply to functions, such as [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring), that make implicit comparisons. Depending on the flags that are set, the results of calling [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring) to search for one string within another string can differ considerably.

> [!Note]  
> For Windows Vista and later, [**FindNLSStringEx**](/windows/desktop/api/Winnls/nf-winnls-findnlsstringex) is similar to [**FindNLSString**](/windows/desktop/api/Winnls/nf-winnls-findnlsstring). The security issues are identical for these functions.

 

## Security Considerations for Character Sets in File Names

Windows code page and OEM character sets used on Japanese-language systems contain the Yen symbol (¥) instead of a backslash (\\). Thus, the Yen character is a prohibited character for NTFS and FAT file systems. When mapping Unicode to a Japanese-language code page, conversion functions map both backslash (U+005C) and the normal Unicode Yen symbol (U+00A5) to this same character. For security reasons, your applications should not typically allow the character U+00A5 in a Unicode string that might be converted for use as a FAT file name.

## Security Considerations for Internationalized Domain Names

Internationalized Domain Names (IDNs) are specified by Network Working Group [RFC 3490: Internationalizing Domain Names in Applications (IDNA)](http://www.faqs.org/rfcs/rfc3490.html). The standard introduces a number of security issues.

Glyphs representing certain characters from different scripts might appear similar or even identical. For example, in many fonts, Cyrillic lowercase A ("a") is indistinguishable from Latin lowercase A ("a"). There is no way to tell visually that "example.com" and "example.com" are two different domain names,one with a Latin lowercase A in the name, the other with a Cyrillic lowercase A. An unscrupulous host site can use this visual ambiguity to pretend to be another site in a spoofing attack.

The extended character set that IDNA allows for IDNs also has spoofing potential within a particular script. For example, there is a strong resemblance among the hyphen-minus ("-" U+002D), the hyphen ("—" U+2010), the non-breaking hyphen ("‑" U+2011), the figure dash ("‒" U+2012), the en dash ("–" U+2013), and the minus sign ("−" U+2212).

Similar issues arise from certain compatibility compositions. For example, the single Unicode character NUMBER TWENTY FULL STOP ("⒛", U+249B) is converted to "20." (U+0032 U+0030 U+002E) in a NamePrep step, prior to conversion to Punycode. In other words, this composition inserts a period (full stop). Such compositions have spoofing potential.

Mixing of different scripts in an IDN does not necessarily indicate spoofing or deceptive intent. [Technical Report \#36: Unicode Security Considerations](https://www.unicode.org/reports/tr36/#international_domain_names) gives several examples of reasonable IDNs that contain a mix of scripts, such as XML-Документы.com ("Документы" is Russian for "documents").

Spoofing attacks are not restricted to IDNs. For example, "rnicrosoft.com" looks much like "microsoft.com", yet it is an ASCII name. Additionally, a spoofing attack can be made by corruption of a name. Adding extra labels after a well-known brand name, or including the brand name in the path of a URL labeled as secure, can confuse novice users, regardless of the use of the IDN. For some locales, IDNs are required and the Punycode form of these names is unacceptable, since it makes the names look like gibberish.

For more information about the security issues mentioned here, plus a large number of other issues relevant to IDNA, see [Technical Report \#36: Unicode Security Considerations](https://www.unicode.org/reports/tr36/#international_domain_names). Along with detailed discussions of IDNA-related security issues, this report offers suggestions for dealing with suspect IDNs in your applications.

## Security Considerations for ANSI Functions

> [!Note]  
> You are recommended to use Unicode in your globalized applications, particularly new ones, if at all possible. You should use ANSI functions only if you have overriding reasons for not using Unicode, for example, conformance to an older protocol that does not support Unicode.

 

Many National Language Support (NLS) functions, such as [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) and [**GetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoa), have specific ANSI versions, in this case, **GetLocaleInfoA** and **GetCalendarInfoA**, respectively. When your application uses the ANSI version of a function with a Unicode-based operating system, such as Windows NT, Windows 2000, Windows XP, or Windows Vista, the function can fail or produce undefined results. If you have a compelling reason to use ANSI functions with such an operating system, ensure that the data passed by your application is valid for ANSI.

## Security Considerations for Unicode Normalization

Since Unicode normalization can change the form of a string, security mechanisms or character validation algorithms should usually be implemented after normalization. For example, consider an application with a Web interface that accepts a file name, but does not accept a path name. A full-width U+FF43 U+FF1A U+FF3C U+FF57 U+FF49 U+FF4E U+FF44 U+FF4F U+FF57 U+FF53 `(c : \ w i n d o w s)` changes to U+0063 U+001A U+003C U+0077 U+0069 U+006E U+0064 U+006F U+0077 U+0073 `(c:\windows)` with form KC normalization. If an application tests for the presence of the colon and backslash characters before it implements normalization, the result can be unintentional file access.

While Unicode normalization is an element in making operating systems secure, remember that normalization is not a replacement for a comprehensive security policy.

## Related topics

<dl> <dt>

[Character Sets Used in File Names](character-sets-used-in-file-names.md)
</dt> <dt>

[Conventions for Function Prototypes](conventions-for-function-prototypes.md)
</dt> <dt>

[Handling Sorting in Your Applications](handling-sorting-in-your-applications.md)
</dt> <dt>

[Handling Internationalized Domain Names (IDNs)](handling-internationalized-domain-names--idns.md)
</dt> <dt>

[Unicode](unicode.md)
</dt> </dl>

 

 
