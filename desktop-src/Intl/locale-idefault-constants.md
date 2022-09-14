---
description: This topic defines the LOCALE\_IDEFAULT\* constants used by NLS.
ms.assetid: 4fa8b5f3-8c01-44fb-b6fd-8dbf38e3d361
title: LOCALE_IDEFAULT* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_IDEFAULT\* Constants

This topic defines the LOCALE\_IDEFAULT\* constants used by NLS.



| Value                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALE\_IDEFAULTANSICODEPAGE   | The ANSI code page used by a locale for applications that do not support Unicode. The maximum number of characters allowed for this string is six, including a terminating null character. If no ANSI code page is available, only Unicode can be used for the locale. In this case, the value is CP\_ACP (0). Such a locale cannot be set as the system locale. Applications that do not support Unicode do not work correctly with locales marked as "Unicode only". For a list of ANSI and other code pages, see [Code Page Identifiers](code-page-identifiers.md). |
| LOCALE\_IDEFAULTCODEPAGE       | Original equipment manufacturer (OEM) code page associated with the country/region. The OEM code page is used for conversion from MS-DOS-based, text-mode applications. If the locale does not use an OEM code page, the value is CP\_OEMCP (1). The maximum number of characters allowed for this string is six, including a terminating null character. For a list of OEM and other code pages, see [Code Page Identifiers](code-page-identifiers.md).                                                                                                               |
| LOCALE\_IDEFAULTCOUNTRY        | Obsolete. Do not use. This value was provided so that partially specified locales could be completed with default values. Partially specified locales are now deprecated.                                                                                                                                                                                                                                                                                                                                                                                               |
| LOCALE\_IDEFAULTEBCDICCODEPAGE | **Windows 2000:** Default Extended Binary Coded Decimal Interchange Code (EBCDIC) code page associated with the locale. The maximum number of characters allowed for this string is six, including a terminating null character. For a list of EBCDIC and other code pages, see [Code Page Identifiers](code-page-identifiers.md).                                                                                                                                                                                                                                     |
| LOCALE\_IDEFAULTLANGUAGE       | Obsolete. Do not use. This value was provided so that partially specified locales could be completed with default values. Partially specified locales are now deprecated.                                                                                                                                                                                                                                                                                                                                                                                               |
| LOCALE\_IDEFAULTMACCODEPAGE    | Default Macintosh code page associated with the locale. The maximum number of characters allowed for this string is six, including a terminating null character. If the locale does not use a Macintosh code page, the value is CP\_MACCP (2). For a list of Macintosh (MAC) and other code pages, see [Code Page Identifiers](code-page-identifiers.md).                                                                                                                                                                                                              |



 

 

 



