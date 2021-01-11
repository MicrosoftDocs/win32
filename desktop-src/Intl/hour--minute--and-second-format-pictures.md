---
description: This topic describes the format types for strings used to compose the format picture for a time string. Each format picture consists of a combination of one string of each of the format types.
ms.assetid: a5e87d88-4037-4302-99b7-179bfb03fac3
title: Hour, Minute, and Second Format Pictures
ms.topic: article
ms.date: 05/31/2018
---

# Hour, Minute, and Second Format Pictures

This topic describes the format types for strings used to compose the format picture for a time string. Each format picture consists of a combination of one string of each of the format types.

> [!Note]  
> In the format types, the letters "m", "s", and "t" must be lowercase, and the letter "h" must be lowercase to denote the 12-hour clock or uppercase ("H") to denote the 24-hour clock.

Single quotation marks can be used to mark characters that should be displayed exactly as specified. If the application must display a single quotation mark, it should place two single quotation marks in a row. For example, 'abc''bar', is displayed as "abc'bar".

The following table defines the format types used to represent hours.

| String | Meaning                                                             |
|--------|---------------------------------------------------------------------|
| h      | Hours without leading zeros for single-digit hours (12-hour clock). |
| hh     | Hours with leading zeros for single-digit hours (12-hour clock).    |
| H      | Hours without leading zeros for single-digit hours (24-hour clock). |
| HH     | Hours with leading zeros for single-digit hours (24-hour clock).    |

The following table defines the format types used to represent minutes.

| String | Meaning                                                 |
|--------|---------------------------------------------------------|
| m      | Minutes without leading zeros for single-digit minutes. |
| mm     | Minutes with leading zeros for single-digit minutes.    |

The following table defines the format types used to represent seconds.

| String | Meaning                                                 |
|--------|---------------------------------------------------------|
| s      | Seconds without leading zeros for single-digit seconds. |
| ss     | Seconds with leading zeros for single-digit seconds.    |

The following table defines the format types used to represent a time marker.

| String | Meaning|
| ---    | ---    |
| t      | One-character time marker string.<br />**Note:** This format is not recommended for use with certain languages, such as Japanese (Japan). With this format, an application always takes the first character from the time marker string, defined by [LOCALE_S1159](locale-s1159.md) (AM) and [LOCALE_S2359](locale-s2359.md) (PM). Because of this, the application can create incorrect formatting with the same string used for both AM and PM.|
| tt     | Multi-character time marker string. |
