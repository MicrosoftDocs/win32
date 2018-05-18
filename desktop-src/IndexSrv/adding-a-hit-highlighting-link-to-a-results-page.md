---
title: Adding a Hit-Highlighting Link to a Results Page
description: Adding a Hit-Highlighting Link to a Results Page
ms.assetid: 'e1a9a89c-0528-463a-9f78-1d5e9adf781b'
---

# Adding a Hit-Highlighting Link to a Results Page

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The hit-highlighter (Webhits.dll) comes with a ready-made results page (Query.htx). This results page includes a link to Webhits for each document returned. To add a link to an existing page, modify the .htx file by inserting the following line where you want the link to appear:


```
<a href="http://<%server_name%<execute-permission vpath/Null.htw>?CiWebhitsFile=<%escapeURL vpath%>&amp; 
CiRestriction=<%escapeURL CiRestriction%>"><b>Highlight Hits</b></a><BR>
 
```



Here, *server\_name* is a variable storing the name of the server on which the web server is located, and [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var) is the variable storing the query. You escape the restriction through the **EscapeURL** keyword, as shown in the sample query.

 

 




