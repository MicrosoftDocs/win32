---
description: LOCALE\_CUSTOM\* Constants
ms.assetid: a41a7f55-8905-47a1-86c3-74ed40b3834c
title: LOCALE_CUSTOM* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_CUSTOM\* Constants

This topic defines the LOCALE\_CUSTOM\* constants used by NLS to represent [custom locales](custom-locales.md).



| Value                       | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALE\_CUSTOM\_DEFAULT     | **Windows Vista and later:** The default custom locale. When an NLS function must return a locale identifier for a [supplemental locale](custom-locales.md) for the current user, the function returns this value instead of [LOCALE\_USER\_DEFAULT](locale-user-default.md). The value of LOCALE\_CUSTOM\_DEFAULT is 0x0C00.                                                                                                                                                                  |
| LOCALE\_CUSTOM\_UI\_DEFAULT | **Windows Vista and later:** The default custom locale for MUI. The user preferred UI languages and the system preferred UI languages can include at most a single language that is implemented by a Language Interface Pack (LIP) and for which the language identifier corresponds to a supplemental locale. If there is such a language in a list, the constant is used to refer to that language in certain contexts. The value of LOCALE\_CUSTOM\_UI\_DEFAULT is 0x1400.                    |
| LOCALE\_CUSTOM\_UNSPECIFIED | **Windows Vista and later:** An unspecified custom locale, used to identify all supplemental locales except the locale for the current user. Supplemental locales cannot be distinguished from one another by their locale identifiers, but can be distinguished by their [locale names](locale-names.md). Certain NLS functions can return this constant to indicate that they cannot provide a useful identifier for a particular locale. The value of LOCALE\_CUSTOM\_UNSPECIFIED is 0x1000. |



 

 

 



