---
description: This topic describes how you can work with internationalized domain names (IDNs) in your applications.
ms.assetid: e0ca356e-f8c1-4845-ae1e-ce2ae8987515
title: Handling Internationalized Domain Names (IDNs)
ms.topic: article
ms.date: 05/31/2018
---

# Handling Internationalized Domain Names (IDNs)

This topic describes how you can work with internationalized domain names (IDNs) in your applications. IDNs are specified by Network Working Group [RFC 3490: Internationalizing Domain Names in Applications (IDNA)](http://www.faqs.org/rfcs/rfc3490.html). Prior to this draft standard, IDNs were limited to Latin characters without diacritics. IDNA allows IDNs to include Latin characters with diacritics, along with characters from non-Latin scripts, such as Cyrillic, Arabic, and Chinese. The standard also establishes rules for mapping IDNs to ASCII-only domain names. Thus, IDNA issues can be handled on the client side, without requiring any domain name server (DNS) changes.

> [!Caution]  
> RFC 3490 introduces a number of security issues related to the use of IDNs. For more information see the related section of [Security Considerations: International Features](security-considerations--international-features.md).

 

> [!Note]  
> IDNA is currently based on Unicode 3.2.

 

## NLS API Functions for Handling IDNs

NLS includes the following conversion functions that your application can use to convert an IDN to different representations. For an example of the use of these functions, see [NLS: Internationalized Domain Name (IDN) Conversion Sample](nls--internationalized-domain-name--idn--conversion-sample.md).

-   [**IdnToAscii**](/windows/desktop/api/Winnls/nf-winnls-idntoascii). Converts an IDN to Punycode.
-   [**IdnToNameprepUnicode**](/windows/desktop/api/Winnls/nf-winnls-idntonameprepunicode). Performs the NamePrep portion of the conversion of an IDN to an ASCII name. This function creates a canonical Unicode representation of a string.
-   [**IdnToUnicode**](/windows/desktop/api/Winnls/nf-winnls-idntounicode). Converts a Punycode string to a normal UTF-16 string.

NLS also defines several API functions that can be used to mitigate some of the security risks presented by the IDN technology. On Windows Vista and later, the following functions are used to verify that the characters in a given IDN are drawn entirely from the scripts associated with a particular locale or locales. For an example of the use of these functions, see [NLS: Internationalized Domain Name (IDN) Mitigation Sample](nls--internationalized-domain-name--idn--mitigation-sample.md).

-   [**GetStringScripts**](/windows/desktop/api/Winnls/nf-winnls-getstringscripts). Provides a list of scripts used in a particular string.
-   [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa), [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex). Retrieve locale information. Using the functions with *LCType* set to [LOCALE\_SSCRIPTS](locale-sscripts.md) provides a list of scripts normally used for a particular locale.
-   [**VerifyScripts**](/windows/desktop/api/Winnls/nf-winnls-verifyscripts). Compares lists of scripts. To verify against multiple locales, the application can make multiple calls to [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) and [**VerifyScripts**](/windows/desktop/api/Winnls/nf-winnls-verifyscripts).

For applications that run on Windows XP and Windows Server 2003, the functions [**DownlevelGetLocaleScripts**](downlevelgetlocalescripts.md), [**DownlevelGetStringScripts**](downlevelgetstringscripts.md), and [**DownlevelVerifyScripts**](downlevelverifyscripts.md) play a similar role to the functions listed above in mitigating security risk. The ["Microsoft Internationalized Domain Name (IDN) Mitigation APIs"](https://www.microsoft.com/downloads/details.aspx?FamilyID=AD6158D7-DDBA-416A-9109-07607425A815&displaylang=en) download is available at the [MSDN Download Center](https://www.microsoft.com/?ref=go).

## Handle Unicode Strings

IDNA supports the transformation of Unicode strings into legitimate host name labels, with the exception of strings containing certain prohibited characters, such as control characters, characters from the private use area (PUA), and the like. Your application can use the IDN\_USE\_STD3\_ASCII\_RULES flag with several NLS conversion functions to force the functions to fail if they encounter ASCII characters other than letters, numbers, or the hyphen-minus (-) character, or if a string begins or ends with the hyphen-minus character. These characters have always been prohibited from use in domain names, and remain prohibited in the draft standard.

## Handle Unassigned Code Points

IDNs cannot contain unassigned code points. Therefore, code points that are not associated with a character ("assigned") as of Unicode 3.2 do not have defined IDN mappings, even though the IDN\_ALLOW\_UNASSIGNED flag in certain conversion functions allows them to be mapped to Punycode. You can find a list of unassigned code points in [RFC 3454](http://www.faqs.org/rfcs/rfc3454.html).

> [!Caution]  
> If your application encodes unassigned code points as Punycode, the resulting domain names should be illegal. Security can be compromised if a later version of IDNA makes these names legal or if the application filters out the illegal characters to try to create a legal domain name.

 

Unassigned code points are not allowed in the stored strings used in protocol identifiers and named entities, such as names in digital certificates and DNS domain name parts. However, the code points are allowed in query strings, for example, user-entered names for digital certificate authorities and DNS lookups, which are used to match against stored identifiers.

> [!Caution]  
> Although query strings can use unassigned code points, you should not use them in your applications. Even a user-supplied query string presents a risk of a "spoofing" attack. In this type of attack, the unscrupulous host site reroutes users from the site they intend to access to another site that might provide sensitive information to a third party. For example, copying a string from an incoming e-mail can present the same risks as clicking on a link in a browser.

 

## Convert Domain Names to ASCII Names

Your application can use the [**IdnToAscii**](/windows/desktop/api/Winnls/nf-winnls-idntoascii) function and certain mitigation functions to convert IDNs to ASCII.

> [!Caution]  
> Because strings with very different binary representations can compare as identical, this function can raise certain security concerns. For more information, see the discussion of comparison functions in [Security Considerations: International Features](security-considerations--international-features.md).

 

## Examples

[NLS: Internationalized Domain Name (IDN) Conversion Sample](nls--internationalized-domain-name--idn--conversion-sample.md) demonstrates the use of the IDN conversion functions. [NLS: Internationalized Domain Name (IDN) Mitigation Sample](nls--internationalized-domain-name--idn--mitigation-sample.md) demonstrates the use of the IDN mitigation functions.

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Security Considerations: International Features](security-considerations--international-features.md)
</dt> </dl>

 

 



