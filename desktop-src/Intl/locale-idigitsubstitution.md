---
description: LOCALE\_IDIGITSUBSTITUTION
ms.assetid: f3f7d7ac-8f1e-4bfa-84f0-dfe8cff568c3
title: LOCALE_IDIGITSUBSTITUTION
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_IDIGITSUBSTITUTION

**Windows 2000:** The shape of digits. For example, Arabic, Thai, and Indic digits have classical shapes different from European digits. For locales with [LOCALE\_SNATIVEDIGITS](locale-snative-constants.md) specified as values other than ASCII 0-9, this value specifies whether preference should be given to those other digits for display purposes. For example, if a value of 2 is chosen, the digits specified by LOCALE\_SNATIVEDIGITS are always used. If a 1 is chosen, the ASCII 0-9 digits are always used. If a 0 is chosen, ASCII is used in some circumstances and the digits specified by LOCALE\_SNATIVEDIGITS are used in others, depending on the context.



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
<td>0</td>
<td>Context-based substitution. Digits are displayed based on the previous text in the same output. European digits follow Latin scripts, Arabic-Indic digits follow Arabic text, and other national digits follow text written in various other scripts. When there is no preceding text, the locale and the displayed reading order determine digit substitution, as shown in the following table.
<table>
<thead>
<tr class="header">
<th>Locale</th>
<th>Reading order</th>
<th>Digits used</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Arabic</td>
<td>Right-to-left</td>
<td>Arabic-Indic</td>
</tr>
<tr class="even">
<td>Thai</td>
<td>Left-to-right</td>
<td>Thai digits</td>
</tr>
<tr class="odd">
<td>All others</td>
<td>Any</td>
<td>No substitution used</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>1</td>
<td>No substitution used. Full Unicode compatibility.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Native digit substitution. National shapes are displayed according to LOCALE_SNATIVEDIGITS.</td>
</tr>
</tbody>
</table>



 

 

 



