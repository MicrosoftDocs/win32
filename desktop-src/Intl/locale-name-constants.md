---
description: LOCALE\_NAME\* Constants
ms.assetid: 63e2e368-af2f-4af0-bbea-2b27d1939394
title: LOCALE_NAME* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_NAME\* Constants

This topic defines the LOCALE\_NAME\* constants used by NLS.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LOCALE_NAME_INVARIANT</td>
<td>Name of an invariant locale that provides stable locale and calendar data.</td>
</tr>
<tr class="even">
<td>LOCALE_NAME_MAX_LENGTH</td>
<td>Maximum length of a locale name. The maximum number of characters allowed for this string is 85, including a terminating null character.
<blockquote>
[!Note]<br />
Your application must use the constant for the maximum locale name length, instead of hard-coding the value &quot;85&quot;.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>LOCALE_NAME_SYSTEM_DEFAULT</td>
<td>Name of the current operating system locale.</td>
</tr>
<tr class="even">
<td>LOCALE_NAME_USER_DEFAULT</td>
<td>Name of the current user locale, matching the preference set in the regional and language options portion of Control Panel. This locale can be different from the locale for the current user interface language.</td>
</tr>
</tbody>
</table>



 

 

 




