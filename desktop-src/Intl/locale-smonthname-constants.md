---
description: LOCALE\_SMONTHNAME\* Constants
ms.assetid: 81269282-bea8-4a5d-929d-c68af34bd1ac
title: LOCALE_SMONTHNAME* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SMONTHNAME\* Constants

This topic defines the LOCALE\_SMONTHNAME\* constants used by NLS.




| Value | Meaning | 
|-------|---------|
| LOCALE_SMONTHNAME1 | Native long name for January. The maximum number of characters allowed for this string is 80, including a terminating null character.<blockquote>[!Note]<br />Calling the <a href="/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa"><strong>GetLocaleInfo</strong></a> or <a href="/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex"><strong>GetLocaleInfoEx</strong></a> function with a LOCALE_SMONTHNAME* constant returns the standalone, or nominative, form of the month name. To get the genitive form of the month name, the application calls <a href="/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata">GetDateFormat</a> or <a href="/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex">GetDateFormatEx</a> with a date picture of ddMMMM and removes the two digits from the beginning of the retrieved string.</blockquote><br /> | 
| LOCALE_SMONTHNAME2 | Native long name for February. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME3 | Native long name for March. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME4 | Native long name for April. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME5 | Native long name for May. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME6 | Native long name for June. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME7 | Native long name for July. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME8 | Native long name for August. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME9 | Native long name for September. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME10 | Native long name for October. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME11 | Native long name for November. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME12 | Native long name for December. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 
| LOCALE_SMONTHNAME13 | Native name for a 13th month, if it exists. The maximum number of characters allowed for this string is 80, including a terminating null character. See note for LOCALE_SMONTHNAME1. | 




 

 

 




