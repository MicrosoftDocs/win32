---
description: LOCALE\_RETURN\* Constants
ms.assetid: c6aadf84-c597-4cbd-a715-b68325ce5117
title: LOCALE_RETURN* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_RETURN\* Constants

This topic defines the LOCALE\_RETURN\* constants used by NLS.




| Value | Meaning | 
|-------|---------|
| LOCALE_RETURN_GENITIVE_NAMES | <strong>Windows 7 and later:</strong> Retrieve the genitive names of months, which are the names used when the month names are combined with other items. For example, in Ukrainian the equivalent of January is written "Січень" when the month is named alone. However, when the month name is used in combination, for example, in a date such as January 5th, 2003, the genitive form of the name is used. For the Ukrainian example, the genitive month name is displayed as "5 січня 2003". The list of genitive month names begins with January and is semicolon-delimited. If there is no 13th month, use a semicolon in its place at the end of the list.<blockquote>[!Note]<br />Genitive month names do not exist in all languages.</blockquote><br /><br /> | 
| LOCALE_RETURN_NUMBER | <strong>Windows Me/98, Windows NT 4.0 and later:</strong> Retrieve a number. This constant causes <a href="/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa"><strong>GetLocaleInfo</strong></a> or <a href="/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex"><strong>GetLocaleInfoEx</strong></a> to retrieve a value as a number instead of as a string. The buffer that receives the value must be at least the length of a DWORD value. This constant can be combined with any other constant having a name that begins with "LOCALE_I". | 




 

 

 




