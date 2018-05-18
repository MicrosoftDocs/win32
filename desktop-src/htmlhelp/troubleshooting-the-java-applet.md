---
title: Troubleshooting the Java Applet
description: Troubleshooting the Java Applet
ms.assetid: '63095C5B-1567-4392-BD0F-4EDAD65B6C11'
---

# Troubleshooting the Java Applet

The following table lists problems that might arise when using the HTML Help Java Applet, along with possible solutions.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>If this happens</th>
<th>Try this</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cannot find _______.class.</td>
<td>Check that the <strong>CODEBASE</strong> parameter in the &lt;APPLET&gt; tag points to a directory that contains the following files:
<ul>
<li>HHCtrl.class</li>
<li>TreeView.class</li>
<li>TreeCanvas.class</li>
<li>sitemapParser.class</li>
<li>IndexPanel.class</li>
<li>ElementList.class</li>
<li>Element.class</li>
<li>DialogLayout.class</li>
<li>RelatedDialog.class</li>
<li>cntimage.gif</li>
</ul></td>
</tr>
<tr class="even">
<td>Images don't display in the table of contents.</td>
<td>Make sure that cntimage.gif is in the directory specified by the <strong>CODEBASE</strong> parameter of the &lt;APPLET&gt; tag. If your contents (.hhc) file specifies a custom image strip, then make sure that the image file is in the same directory as the HTML file containing the applet.</td>
</tr>
<tr class="odd">
<td>Contents files take a long time to load.</td>
<td>If your contents files take too long to load, try breaking them up into multiple sections using the MERGE keyword.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[About the HTML Help Java Applet](about-the-html-help-java-applet.md)
</dt> </dl>

 

 




