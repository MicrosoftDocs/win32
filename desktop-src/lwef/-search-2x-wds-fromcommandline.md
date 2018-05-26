---
title: Calling WDS from the Command Line
description: You can launch the Microsoft Windows Desktop Search (WDS) user interface with a specific filter, store, and query from another application or a webpage that uses the Browser Helper Object (BHO) by using the windowssearch.exe command line syntax.
ms.assetid: fd62f7c9-08a9-4e05-b0bc-e2215cfff59e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Calling WDS from the Command Line

\[Windows Search 2.x is obsolete after Windows XP. Instead, use [Windows Search](http://go.microsoft.com/fwlink/p/?linkid=198360).\]

You can launch the Microsoft Windows Desktop Search (WDS) user interface with a specific filter, store, and query from another application or a webpage that uses the Browser Helper Object (BHO) by using the windowssearch.exe command line syntax. When calling WDS from the command line, no information about the user's actions or selection in the WDS window is returned to the calling application or webpage.

The WDS installation path is specified in the InstallDir registry setting under HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows Desktop Search. The default path that windowssearch.exe is installed to is Program Files\\Windows Desktop Search.

## Command Line Syntax

The following syntax applies to the Windows Desktop Search 2.x command-line interface.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Options</th>
<th>Parameter</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/startup</td>

<td>Initializes Windows Desktop Search</td>
</tr>
<tr class="even">
<td>/indexnow</td>

<td>Turns off indexing back-off and rescans all index locations</td>
</tr>
<tr class="odd">
<td>/showstatus</td>

<td>Shows the indexing status window</td>
</tr>
<tr class="even">
<td>/launchsearchwindow or /url</td>

<td>Opens a WDS window with an empty query</td>
</tr>
<tr class="odd">
<td>/url</td>
<td>search:[store|show|query] query string</td>
<td>Opens a WDS window with a query and filter based on the following parameters:
<ul>
<li><p>store - Specifies the data source to query: files, outlook, outlookexpress. If not specified all stores will be searched. <br/></p>
<blockquote>
[!Note]<br />
While Advanced Query Syntax supports referencing Microsoft Outlook as 'oe', the store parameter on the command line must be 'outlookexpress'.
</blockquote>
<p><br/></p></li>
<li><p>show - Specifies which perceived type of results to return. See [Perceived Types](-search-2x-wds-perceivedtype.md) for a complete list of types. If not specified, all types will be returned. <br/></p>
<blockquote>
[!Note]<br />
There are three differences between the perceived type values and the values for show. For <code>show</code>, use 'documents' instead of 'doc', 'pictures' instead of 'pics', and 'textdocuments' instead of 'text'.
</blockquote>
<p><br/></p></li>
<li>query - Specifies the search criteria. This value supports [Advanced Query Syntax](-search-2x-wds-aqsreference.md) parameters to refine the results. The query parameter must be the last parameter in the URL.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Example

For example, to search all files for pictures matching the criteria 'wallpaper' use the following command:

`WindowsSearch.exe /url search:store=files&show=pictures&query=wallpaper`

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Advanced Query Syntax](-search-2x-wds-aqsreference.md)
</dt> <dt>

[Perceived Types](-search-2x-wds-perceivedtype.md)
</dt> <dt>

[Calling WDS from Web Pages](-search-2x-wds-browserhelpobject.md)
</dt> </dl>

 

 





