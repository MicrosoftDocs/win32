---
title: Item Parameter
description: The Item parameter is dependent on the specified command. For usage information, see the individual commands that use this parameter.
ms.assetid: 3E9A7781-0CBC-4e99-BB37-BC2BB4FD721A
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Item Parameter

The **Item** parameter is dependent on the specified command. For usage information, see the individual commands that use this parameter.

## Applies to

-   [ALink](alink.md)
-   [Contents](contents.md)
-   [Index](index.md)
-   [KLink](klink.md)
-   [Related Topics](related-topics.md)
-   [Shortcut](shortcut.md)
-   [Splash](splash.md)
-   [TCard](tcard.md)
-   [WinHelp](winhelp.md)

## Valid Values



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Syntax</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre data-space="preserve"><code>&lt;PARAM name=&quot;Item1&quot; value=&quot; &quot;&gt;
&lt;PARAM name=&quot;Item2&quot; value=&quot; &quot;&gt;
&lt;PARAM name=&quot;Item3&quot; value=&quot; &quot;&gt;</code></pre>
<blockquote>
[!Note]<br />
Valid values depend on which [command](about-commands.md) is specified.
</blockquote>
<br/></td>
<td><ul>
<li><strong>Alink</strong>: Specifies the .chm file path and one or more ALink names to look up.</li>
<li><strong>Contents</strong>: Specifies the .hhc file path.</li>
<li><strong>Index</strong>: Specifies the .hhk file path.</li>
<li><strong>KLink</strong>: Specifies the .chm file path and one or more keywords to look up.</li>
<li><strong>Related Topics</strong>: Specifies an entry in the Related Topics list.</li>
<li><strong>Shortcut</strong>: Specifies the program to open. Depending on the functionality you want to implement with the <strong>Shortcut</strong> command, you may need to supply additional information.</li>
<li><strong>Splash</strong>: Specifies the image file path and length of time the image will appear.</li>
<li><strong>TCard</strong>: Specifies the <em>wPARAM</em> and <em>lPARAM</em> values to pass to the Windows <strong>WM_TCARD</strong> message. Depending on the functionality you want to implement with TCard, you may need to supply additional information.</li>
<li><strong>WinHelp</strong>: Specifies the .hlp file path and topic ID (or map number).</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[About Parameters](parameters.md)
</dt> </dl>

 

 





