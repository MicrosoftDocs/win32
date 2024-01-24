---
description: LOCALE\_SDURATION
ms.assetid: 45ffd7ed-f964-4948-8679-cf960b5c1e0e
title: LOCALE_SDURATION
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SDURATION

**Windows Vista and later:** Time duration format composed of format pictures listed in the following table. The format is similar to the format for [LOCALE\_STIMEFORMAT](locale-stime-constants.md). As for LOCALE\_STIMEFORMAT, this format can also include any string of characters enclosed in single quotes. Formats can include, for example, "h:mm:ss", or "d'd 'h'h 'm'm 's.fff's'". In comparison with LOCALE\_STIMEFORMAT, there are additional format pictures for fractions of a second. Because this format is for duration, not time, it does not specify a 12- or 24-hour clock system, or include an AM/PM indicator. This constant might be used, for example, for a multi-media application that displays file time or a sporting event application that displays finish times.



| Value | Meaning                                                                                                                                                                                                                             |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| h     | Hours without leading zeros for single-digit hours                                                                                                                                                                                  |
| hh    | Hours with leading zeros for single-digit hours                                                                                                                                                                                     |
| m     | Minutes without leading zeros for single-digit minutes                                                                                                                                                                              |
| mm    | Minutes with leading zeros for single-digit minutes                                                                                                                                                                                 |
| s     | Seconds without leading zeros for single-digit seconds                                                                                                                                                                              |
| ss    | Seconds with leading zeros for single-digit seconds                                                                                                                                                                                 |
| f     | Tenths of a second                                                                                                                                                                                                                  |
| ff    | Hundredths of a second                                                                                                                                                                                                              |
| fff   | Thousandths of a second; character "f" can occur up to nine consecutive times (fffffffff), although support for frequency timers is limited to 100 nanoseconds; if nine characters are present, the last two digits are always zero |



 

 

 



