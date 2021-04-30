---
description: A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.
ms.assetid: dae4a28d-0332-4bb2-b040-13a959c7945e
title: Factoids Common Across Languages
ms.topic: article
ms.date: 05/31/2018
---

# Factoids Common Across Languages

A number of factoids describe input that is common to all language recognizers and need not have different formats for different languages. The following table lists factoids that are common across all languages.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Factoid</th>
<th>Definition</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Digit</strong></td>
<td>Sets bias for a single digit. The recognizer is biased toward returning only single digits when this factoid is set.<br/></td>
<td>0-9<br/></td>
</tr>
<tr class="even">
<td><strong>Email</strong></td>
<td>Sets bias for an email address.<br/></td>
<td>someone@example.com<br/></td>
</tr>
<tr class="odd">
<td><strong>Web</strong></td>
<td>Sets bias for various URL formats.<br/>
<blockquote>
[!Note]<br />
The default settings for the recognizer include the <strong>Web</strong> factoid. Because of this, you may not notice a large difference between the <strong>Web</strong> factoid and the default setting. However, the <strong>Web</strong> factoid does help eliminate spaces between words in a URL.
</blockquote>
<br/></td>
<td>http:\\microsoft.net<br/> https://microsoft.us/<br/> https:\\www.microsoft.au\<br/> https://microsoft.com<br/> www.microsoft_world.com<br/> www.microsoft.us\<br/> http:\\www.microsoft.com\myfile.htm<br/> http:\\www.microsoft.com\myfile.html<br/> http:\\www.microsoft.com\myfile.asp<br/> http:\\www.microsoft.uk<br/> http:\\www.microsoft.info<br/> www.microsoft.biz<br/></td>
</tr>
<tr class="even">
<td><strong>Default</strong></td>
<td>Returns the recognizer to its default settings.<br/></td>
<td>The default setting for factoids for western languages includes the system dictionary, user dictionary, various punctuations, and the <strong>Web</strong> and <strong>Number</strong> factoids.<br/> The default setting for factoids for East Asian languages includes all characters supported by the recognizer.<br/></td>
</tr>
<tr class="odd">
<td><strong>None</strong></td>
<td>Disables all factoids, dictionaries, and the language model.<br/></td>
<td>This factoid should be used only when you do not want the recognizer to use any grammar rules or dictionaries, including the system dictionary. This factoid is useful for input of random strings such as product codes. Do not use the Coerce flag with this factoid.<br/></td>
</tr>
</tbody>
</table>



 

 

 




