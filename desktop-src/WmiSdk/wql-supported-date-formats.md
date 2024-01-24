---
description: Describes date formats supported for use in the WQL WHERE clause.
ms.assetid: 24d70b7f-681b-4a36-bb67-beaf69f4919f
ms.tgt_platform: multiple
title: WQL-Supported Date Formats
ms.topic: article
ms.date: 05/31/2018
---

# WQL-Supported Date Formats

In addition to the WMI **DATETIME** format, the following date formats are supported for use in the WQL **WHERE** clause.

The displayed time format is different for different locales. Scripts that connect to remote computers must specify time in the format appropriate for the locale of the target computer.

For example, the United States date and time format is MM-DD-YYYY. If a script on a US computer connects to a target computer in a locale where the format is DD-MM-YYYY, then queries are processed on the target computer as DD-MM-YYYY. To avoid different results between locales, use the [**DATETIME**](datetime.md) format. For more information, see [Date and Time Format](date-and-time-format.md).



<table>
<thead>
<tr class="header">
<th>Format</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mon[th] dd[,] [yy]yy</td>
<td>Month (either spelled-out or abbreviated in three letters), day, optional comma, and two or four-digit year.<br/> <dl> January 21, 1932<br />
January 21, 32<br />
Jan 21 1932<br />
Jan 21 32<br />
</dl></td>
</tr>
<tr class="even">
<td>Mon[th][,] yyyy</td>
<td>Month (either spelled-out or abbreviated in three letters), optional comma, and four-digit year.<br/> <dl> January 1932<br />
Jan 1932<br />
</dl></td>
</tr>
<tr class="odd">
<td>Mon[th] [yy]yy dd</td>
<td>Month (either spelled-out or abbreviated in three letters), two or four digit year, and day.<br/> <dl> January 1932 21<br />
Jan 32 21<br />
</dl></td>
</tr>
<tr class="even">
<td>dd Mon[th][,][ ][yy]yy</td>
<td>Day of the month, month (either spelled-out or abbreviated in three letters), optional comma, optional space, and two or four-digit year.<br/> <dl> 21 January, 1932<br />
21 Jan32<br />
</dl></td>
</tr>
<tr class="odd">
<td>dd [yy]yy Mon[th]</td>
<td>Day of the month, two or four-digit year, and month (either spelled-out or abbreviated in three letters).<br/> <dl> 21 1932 January<br />
</dl></td>
</tr>
<tr class="even">
<td>[yy]yy Mon[th] dd</td>
<td>Two or four-digit year, month (either spelled-out or abbreviated in three letters), and day.<br/> <dl> 1932 January 21<br />
</dl></td>
</tr>
<tr class="odd">
<td>yyyy Mon[th]</td>
<td>Two or four-digit year and month (either spelled-out or abbreviated in three letters).<br/> <dl> 1932 Jan<br />
</dl></td>
</tr>
<tr class="even">
<td>yyyy dd Mon[th]</td>
<td>Two or four-digit year, day, and month (either spelled-out or abbreviated in three letters).<br/> <dl> 1932 21 January<br />
</dl></td>
</tr>
<tr class="odd">
<td>[M]M{/-.}dd{/-.}[yy]yy</td>
<td>Month, day, and two or four-digit year. Note that the separators must be the same.<br/></td>
</tr>
<tr class="even">
<td>dd{/-.}[M]M{/-.}[yy]yy</td>
<td>Day of the month, month, and two or four-digit year. Note that the separators must be the same.<br/></td>
</tr>
<tr class="odd">
<td>[M]M{/-.}[yy]yy{/-.}dd</td>
<td>Month, two or four-digit year, and day. Note that the separators must be the same.<br/></td>
</tr>
<tr class="even">
<td>dd{/-.}[yy]yy{/-.}[M]M</td>
<td>Day of the month, two or four-digit year, and month. Note that the separators must be the same.<br/></td>
</tr>
<tr class="odd">
<td>[yy]yy{/-.}dd{/-.}[M]M</td>
<td>Two or four digit year, day, and month. Note that the separators must be the same.<br/></td>
</tr>
<tr class="even">
<td>[yy]yy{/-.}[M]M{/-.}dd</td>
<td>Two or four digit year, month, and day. Note that the separators must be the same.<br/></td>
</tr>
<tr class="odd">
<td>[yy]yyMMdd</td>
<td>Two or four digit year, month, and day, without spaces.<br/></td>
</tr>
<tr class="even">
<td>yyyy[MM[dd]]</td>
<td>Two or four digit year, optional month, and optional day, without spaces.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




