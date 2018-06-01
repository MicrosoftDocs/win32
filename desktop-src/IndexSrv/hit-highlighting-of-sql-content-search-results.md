---
Description: Hit-Highlighting of SQL Content Search Results
ms.assetid: a94ce14a-2082-483d-bdf6-c1cea8957b94
title: Hit-Highlighting of SQL Content Search Results
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hit-Highlighting of SQL Content Search Results

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Hit-highlighting is an Indexing Service feature that you can use when querying a document. Hit-highlighting generates an HTML page that contains a list of the hits showing the exact portions (if any) of the document that satisfy your query.

When using SQL to query for content, you can use the hit-highlighting feature by using Microsoft ActiveX Data Objects (ADO) to retrieve the **Query Restriction** property and using that property as the value for the [CiRestriction](https://www.bing.com/search?q=CiRestriction) parameter of Webhits.dll.

> [!Note]  
> Hit-highlighting is available only for SQL content queries (**CONTAINS** predicate) and a **vpath** recordset field must be present in the **Select\_List** statement. Get the **Query Restriction** property only after the command is executed.

 

The following example queries for documents containing the words "Index" and "Server" gets the **Query Restriction** property, and uses it to invoke the hit-highlighter (Webhits.dll):


```
<%
Set Conn = Server.CreateObject("ADODB.Connection")
Conn.ConnectionString =  "provider=msidxs;"
Conn.Open
Set AdoCommand = Server.CreateObject("ADODB.Command")
set AdoCommand.ActiveConnection = Conn
Set Recordset = Server.CreateObject("ADODB.RecordSet")
AdoCommand.Properties("Bookmarkable") = True
AdoCommand.CommandText = "select vpath, filename from scope() where contains('Index AND Server')>0"
Recordset.open AdoCommand
SearchString = AdoCommand.Properties("Query Restriction")
%>
<%if SearchString <> "" then%>
<BR>
  <%
  ' Construct the URL for hit highlighting
  WebHitsQuery = "CiWebHitsFile=" & Server.URLEncode( Recordset("vpath") )
  WebHitsQuery = WebHitsQuery & "&amp;CiRestriction=" & Server.URLEncode( SearchString )

  WebHitsQuery = WebHitsQuery & "&amp;CiBold=True"
  WebHitsQuery = WebHitsQuery & "&amp;CiUserParam3=" & QueryForm
  %>
  <a href="/iissamples/issamples/Oop/Qsumrhit.htw?<%= WebHitsQuery %>"><b>Show Highlights (condensed)</b></a> /
  <a href="/iissamples/issamples/Oop/Qfullhit.htw?<%= WebHitsQuery %>&amp;CiHiliteType=Full"><b>Show Highlights (full
text)</b></a>
<BR>
<%end if%>
```



 

 



