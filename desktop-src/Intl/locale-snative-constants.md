---
description: LOCALE\_SNATIVE\* Constants
ms.assetid: 560978d7-a33c-4e62-9abd-cbd3ec38f3b5
title: LOCALE_SNATIVE* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SNATIVE\* Constants

This topic defines the LOCALE\_SNATIVE\* constants used by NLS to represent native language names.



| Value                       | Meaning                                                                                                                                                                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALE\_SNATIVECOUNTRYNAME  | **Windows 7 and later:** Native name of the country/region, for example, España for Spain. The maximum number of characters allowed for this string is 80, including a terminating null character.                                                                 |
| LOCALE\_SNATIVECTRYNAME     | Deprecated for Windows 7 and later. Native name of the country/region. See LOCALE\_SNATIVECOUNTRYNAME.                                                                                                                                                             |
| LOCALE\_SNATIVECURRNAME     | **Windows Me/98, Windows 2000:** The native name of the currency associated with the locale, in the native language of the locale. There is no limit on the number of characters allowed for this string.                                                          |
| LOCALE\_SNATIVEDIGITS       | Native equivalents of ASCII 0 through 9. The maximum number of characters allowed for this string is eleven, including a terminating null character. For example, Arabic uses "٠١٢٣٤٥ ٦٧٨٩". See also [LOCALE\_IDIGITSUBSTITUTION](locale-idigitsubstitution.md). |
| LOCALE\_SNATIVEDISPLAYNAME  | **Windows 7 and later:** Display name of the locale in its native language, for example, Deutsch (Deutschland) for the locale German (Germany). <br/>                                                                                                        |
| LOCALE\_SNATIVELANGNAME     | Deprecated for Windows 7 and later. Native name of the language. See LOCALE\_SNATIVELANGUAGENAME.                                                                                                                                                                  |
| LOCALE\_SNATIVELANGUAGENAME | **Windows 7 and later:** Native name of the language, for example, Հայերեն for Armenian (Armenia). The maximum number of characters allowed for this string is 80, including a terminating null character.                                                         |



 

 

 




