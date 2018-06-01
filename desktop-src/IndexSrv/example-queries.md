---
Description: Example Queries
ms.assetid: 265147a4-ab99-4efb-9f64-957bf78625ec
title: Example Queries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table illustrates several example queries. The examples for the short form of Dialect 2 generally apply to Dialect 1 with the exception of the incompatibilities noted in [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md).



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Example</th>
<th>Version</th>
<th>Results</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>{prop name=Contents} apple tree {/prop}</td>
<td>Dialect 2</td>
<td>Documents with the phrase <em>apple tree</em>.</td>
</tr>
<tr class="even">
<td>{phrase} apple tree {/phrase}</td>
<td>Dialect 2</td>
<td>Documents with the phrase <em>apple tree</em>.</td>
</tr>
<tr class="odd">
<td>&quot;apple tree&quot;</td>
<td>Dialect 2, short form</td>
<td>Documents with the phrase <em>apple tree</em>.</td>
</tr>
<tr class="even">
<td>apple tree</td>
<td>Dialect 2, short form</td>
<td>Documents with either or both of the words <em>apple</em> and <em>tree</em>.</td>
</tr>
<tr class="odd">
<td>apple tree</td>
<td>Dialect 1</td>
<td>Documents with the phrase <em>apple tree</em>.</td>
</tr>
<tr class="even">
<td>apple {near dist=50, unit=word} tree</td>
<td>Dialect 2</td>
<td>Documents with the words <em>apple</em> and <em>tree</em> within 50 words of each other.</td>
</tr>
<tr class="odd">
<td>Microsoft near release and {prop name=rank} &gt; 0</td>
<td>Dialect 2</td>
<td>Documents containing the words <em>Microsoft</em> and <em>release</em> occurring near each other.</td>
</tr>
<tr class="even">
<td>Microsoft ~ release &amp; @rank &gt; 0</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents containing the words <em>Microsoft</em> and <em>release</em> occurring near each other.</td>
</tr>
<tr class="odd">
<td>$contents Why is the sky blue?</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents that match the free-text query (which are about the blue sky).</td>
</tr>
<tr class="even">
<td>@size &gt; 1000000 &amp; &lt; 2000000</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents larger than 1 million bytes but smaller than 2 million bytes.</td>
</tr>
<tr class="odd">
<td>{prop name=size} &gt; 1000000 &amp; &lt; 2000000</td>
<td>Dialect 2</td>
<td>Documents larger than 1 million bytes but smaller than 2 million bytes.</td>
</tr>
<tr class="even">
<td>@attrib ^s 32</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents with the archive attribute bit on.</td>
</tr>
<tr class="odd">
<td>@all Excel &amp; ( @size &gt; 1000 &amp; &lt; 100000 ) &amp; Microsoft</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents containing the words <em>Excel</em> and <em>Microsoft</em> that are between 1,000 and 100,000 bytes in size.</td>
</tr>
<tr class="even">
<td>{prop name=all} Excel and {prop name=size} &gt; 1000 and &lt; 100000 ) {/prop} and Microsoft</td>
<td>Dialect 2</td>
<td>Documents containing the words <em>Excel</em> and <em>Microsoft</em> that are between 1,000 and 100,000 bytes in size.</td>
</tr>
<tr class="odd">
<td>@Write &gt; -2d</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>All documents changed within the last two days.</td>
</tr>
<tr class="even">
<td>@Write &gt; 2000-1-1</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>All documents on or after the year 2000.</td>
</tr>
<tr class="odd">
<td>@filename = *.avi</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Video files. The = indicates the query contains an MS-DOS/Windows wildcard character.</td>
</tr>
<tr class="even">
<td>#filename *.avi</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Video files. The # prefix indicates the query contains a regular expression.</td>
</tr>
<tr class="odd">
<td>#filename *.|(do?|,xl?|,p?t|,mdb|)</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Microsoft Office documents.</td>
</tr>
<tr class="even">
<td>{prop name=filename} {regex}*.|(do?|,xl?|,p?t|,mdb|){/regex}</td>
<td>Dialect 2</td>
<td>Microsoft Office documents.</td>
</tr>
<tr class="odd">
<td>#path &quot;*\|[^\]|[14,|}\*&quot;</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Paths with a directory component containing fourteen or more characters.</td>
</tr>
<tr class="even">
<td>{prop name=path}{regex}&quot;*\|[^\]|[14,|}\*&quot;{/regex}</td>
<td>Dialect 2</td>
<td>Paths with a directory component containing fourteen or more characters.</td>
</tr>
<tr class="odd">
<td>{generate method=prefix} dog {/generate}</td>
<td>Dialect 2</td>
<td>All words beginning with <em>dog</em>: For example, <em>dog</em>, <em>dogs</em>, <em>doghouse</em>, <em>dogma</em>.</td>
</tr>
<tr class="even">
<td>@contents BackOffice &amp;! #vpath *\_vti_*</td>
<td>Dialect 2, short form, or Dialect 1</td>
<td>Documents containing the word <em>BackOffice</em>, but which are not in Microsoft FrontPage hidden directories. Microsoft BackOffice is a family of server software, designed to integrate various computer functions for businesses.</td>
</tr>
<tr class="odd">
<td>{prop name=contents} BackOffice AND NOT {prop name=vpath}{regex}*\_vti_*{/regex}</td>
<td>Dialect 2</td>
<td>Documents containing the word <em>BackOffice</em>, but which are not in Microsoft FrontPage hidden directories.</td>
</tr>
<tr class="even">
<td><pre data-space="preserve"><code>SELECT * FROM FILEINFO
  WHERE size &gt; 1000000</code></pre></td>
<td>SQL</td>
<td>Documents larger than 1 million bytes.</td>
</tr>
<tr class="odd">
<td><pre data-space="preserve"><code>SELECT FileName FROM SCOPE()
  WHERE CONTAINS (&#39;search&#39;)
    AND NOT CONTAINS (&#39;slow&#39;)</code></pre></td>
<td>SQL</td>
<td>Documents with the phrase <em>search</em> but not the phrase <em>slow</em>.</td>
</tr>
<tr class="even">
<td><pre data-space="preserve"><code>SELECT DocAuthor, DocTitle
FROM SCOPE()
  WHERE CONTAINS(DocAuthor,
         &#39;smith&#39;)</code></pre></td>
<td>SQL</td>
<td>Documents written by <em>Smith</em>.</td>
</tr>
<tr class="odd">
<td><pre data-space="preserve"><code>...WHERE CONTAINS(DocSubject,
         &#39;&quot;Microsoft&quot; 
          AND &quot;Indexing&quot; 
          NEAR &quot;Service&quot;&#39;)</code></pre></td>
<td>SQL</td>
<td>Documents containing the words <em>Microsoft</em> and <em>Indexing</em> near the word <em>Service</em>.</td>
</tr>
</tbody>
</table>



 

 

 



