---
description: LOCALE\_IFIRSTWEEKOFYEAR
ms.assetid: 866a28b7-e0b8-4b99-96df-345791a24833
title: LOCALE_IFIRSTWEEKOFYEAR
ms.topic: article
ms.date: 03/04/2020
---

# LOCALE\_IFIRSTWEEKOFYEAR

The first week of the year.



| Value | Meaning                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------|
| 0     | Week containing 1/1 is the first week of the year. Note that this can be a single day, if 1/1 falls on the last day of the week. |
| 1     | First full week following 1/1 is the first week of the year.                                                                     |
| 2     | First week containing at least four days is the first week of the year. ISO 8601 compatible.                                     |

If LOCALE_IFIRSTWEEKOFYEAR is 2, LOCALE_IFIRSTDAYOFWEEK is 0 (Monday), and LOCALE_ICALENDARTYPE is Gregorian, then the first week follows the ISO 8601 definition where the first week is the week with the first Thursday of the Gregorian year in it.


 

 

 



