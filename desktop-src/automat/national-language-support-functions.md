---
title: National Language Support Functions
description: Describes functions that support multiple national languages.
ms.assetid: 75744ce7-f08b-4259-8121-e921ef1c4cab
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# National Language Support Functions

The National Language Support (NLS) functions provide support for applications that use multiple locales at one time, especially applications that support Automation. Locale information is passed to allow the application to interpret both the member names and the argument data in the proper locale context. The information in this appendix applies only to 16 bit Windows systems. Other Windows systems include the NLS API is part of the system software.



| Implemented by         | Used by                                                          | Header filename     | Import library name    |
|------------------------|------------------------------------------------------------------|---------------------|------------------------|
| Ole2nls.dll<br/> | Applications that support multiple national languages<br/> | Olenls.h<br/> | Ole2nls.lib<br/> |



 

For Automation, applications need to get locale information and to compare and transform strings into the proper format for each locale.

A *locale* is simply user-preference information, represented as a list of values describing the user's language and sublanguage. National language support incorporates several disparate definitions of a locale into one coherent model. This model is designed to be general enough at a low level to support multiple, distinct, high-level functions, such as the ANSI C locale functions.

A *code page* is the mapping between character glyphs (shapes) and the 1-byte or 2-byte numeric values that are used to represent them. Microsoft Windows uses one of several code pages, depending on the installed localized version of Windows. For example, the Russian version uses code page 1251 (Cyrillic), while the English U.S. and Western European versions use code page 1252 (Multilingual). For historical reasons, the Windows code page in effect is referred to as the ANSI code page.

Because only one code page is in effect at a time, it is impossible for a computer running English U.S. Windows to display or print data correctly from the Cyrillic code page. The fonts do not contain the Cyrillic characters. However, it can still manipulate the characters internally, and they will display correctly again if moved back to a machine running Russian Windows.

All NLS functions use the locale identifier (LCID) to identify which code page a piece of text is assumed to lie in. For example, when returning locale information (such as month names) for Russian, the returned string can be meaningfully displayed in the Cyrillic code page only, because other code pages do not contain the appropriate characters. Similarly, when attempting to change the case of a string with the Russian locale, the case-mapping rules assume the characters are in the Cyrillic code page.

These functions can be divided into two categories:

-   String transformation   NLS functions support uppercasing, lowercasing, generating sort keys (all locale-dependent), and getting string type information.

-   Locale manipulation   NLS functions return information about installed locales for use in string transformations.

For more information on national language support functions, primary and secondary language identifiers and locale identifiers see [National Language Support](https://msdn.microsoft.com/library/windows/desktop/dd319078), [Locales](https://msdn.microsoft.com/library/windows/desktop/dd318716), and [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693).

 

 





