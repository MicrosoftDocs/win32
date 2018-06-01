---
Description: begindetail, enddetail
ms.assetid: 7a912cbc-969f-46c5-9f96-267ee3253cae
title: begindetail, enddetail
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# begindetail, enddetail

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The &lt;%begindetail%&gt; and &lt;%enddetail%&gt; tags surround a section of the HTML extension file in which the results of the search will be merged. The section will be interpreted once for each record matching the query on the page. Within the section, the column names delimited with &lt;% and %&gt; are used to mark the position of the returned data from the query. There can be only one detail section in the HTML extension file.

For example:

``` syntax
<dl>
<%begindetail%><p>
<dt>
<%CiCurrentRecordNumber%>.
<b><a href="<%vpath%>"><%filename%></a></b>
<dd>
<b><i>Abstract: </i></b><%characterization%><br>
<font size=-1> - size <%size%> bytes - <%write%> GMT</font>
<%enddetail%></dl>
```

This query does the following:

-   Shows the name of the file where the search string originates.
-   Gives a brief abstract of the file.
-   Shows the size of the file in bytes.
-   Shows when the file was last modified.

> [!Note]  
> If there are no records returned from the query, the &lt;%begindetail%&gt; section will be skipped.

 

 

 



