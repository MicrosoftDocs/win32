---
description: LOCALE\_ICONSTRUCTEDLOCALE constant description
ms.assetid: 5557ee1e-09bf-0d0b-8e73-df32d9a406dd
title: LOCALE_ICONSTRUCTEDLOCALE
ms.topic: article
ms.date: 09/01/2020
---

# LOCALE\_ICONSTRUCTEDLOCALE

Identifier to request if the locale is a "constructed" locale. Use of this LCTYPE is discouraged.

This identifies a locale for which Windows many not have complete information and has to "construct" information at runtime. Typically the information provided by LOCALE_ICONSTRUCTEDLOCALE is of limited use as Windows will provide as much data as is available for every locale. Therefore, use of this LCTYPE is discouraged.


| Value | Meaning                 |
|-------|-------------------------|
| 0     | Not constructed         |
| 1     | Is a constructed locale |


An example would be a request for "de-US", or German in the United States. NLS will use the German language data that it can find and the United States region data that it can find. 

This may not be perfect as, for example, the system will likely not have information about the name of United States in German. However, if the application or user desires a "de-US" context, then the returned data is the best available. 

Apps that use LOCALE_ICONSTRUCTEDLOCALE to reject locales and fall back to a different locale typically end up with a worse experience, such as landing on de-DE or en-US in this example. Neither of those are close to the original request for German language with a United States region.

