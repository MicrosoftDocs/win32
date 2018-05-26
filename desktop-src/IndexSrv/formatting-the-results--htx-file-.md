---
title: Formatting the Results (.Htx File)
description: Formatting the Results (.Htx File)
ms.assetid: be8af6d5-049e-4bf3-bcb3-5298b3fc7d7b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Formatting the Results (.Htx File)

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The HTML extension (.htx) file is an HTML file containing variables that refer to data in a query results set. The following example defines a page header that displays the query restriction and the documents displayed on the page that the user sees. This file is written to work with the variables in the sample .idq file.

``` syntax
<H4>
<%if CiMatchedRecordCount eq 0%>
No documents matched the query "<%EscapeHTMLCiRestriction%>".</H4>
<%else%>
<H4>Documents <%CiFirstRecordNumber%> to <%CiLastRecordNumber%> of
<%if CiMatchedRecordCount eq CiMaxRecordsInResultSet%>
the first
<%endif%>
<%CiMatchedRecordCount%> matching the query
"<%EscapeHTMLCiRestriction%>".
<%endif%>
</H4>
```

The text in the sample .htx file produces the following:

``` syntax
Documents 1 to 10 of the first 150 matching the query "cache".
```

This example shows that the .htx file is a template that formats how results are returned and displayed to the user. The file is written in HTML format with some extensions supplied by IIS and Indexing Service. These extensions include variable names and other codes for processing results. For details about the .htx file and how to format it, see [HTML Extension Files](html-extension-files.md).

 

 




