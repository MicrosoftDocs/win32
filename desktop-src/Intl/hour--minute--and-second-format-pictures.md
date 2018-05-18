---
Description: 'This topic describes the format types for strings used to compose the format picture for a time string. Each format picture consists of a combination of one string of each of the format types.'
ms.assetid: 'a5e87d88-4037-4302-99b7-179bfb03fac3'
title: 'Hour, Minute, and Second Format Pictures'
---

# Hour, Minute, and Second Format Pictures

This topic describes the format types for strings used to compose the format picture for a time string. Each format picture consists of a combination of one string of each of the format types.

> [!Note]  
> In the format types, the letters "m", "s", and "t" must be lowercase, and the letter "h" must be lowercase to denote the 12-hour clock or uppercase ("H") to denote the 24-hour clock.

 

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



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>String</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>t</td>
<td>One-character time marker string.
<blockquote>
[!Note]<br />
You are recommended not to use this format for certain languages, for example, Japanese (Japan). With this format, an application always takes the first character from the time marker string, defined by [LOCALE_S1159](locale-s1159.md) (AM) and [LOCALE_S2359](locale-s2359.md) (PM). Because of this, the application can create incorrect formatting with the same string used for both AM and PM.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>tt</td>
<td>Multi-character time marker string.</td>
</tr>
</tbody>
</table>



 

 

 




