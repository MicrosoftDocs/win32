---
title: Controlling an Active Server Pages Search
description: Controlling an Active Server Pages Search
ms.assetid: 195067e0-1ea3-40e1-9dee-e890b0df6fe9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Controlling an Active Server Pages Search

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section shows how to control searches with an ASP page. The code displayed here is equivalent in function to an .idq file.


```
<BR>
 
<%
 
if SearchString <> "" then
  if NewQuery then
    set Session("Query") = nothing
    set Session("Recordset") = nothing
    NextRecordNumber = 1
 
    set Q = Server.CreateObject("ixsso.Query")
    set util = Server.CreateObject("ixsso.util")
    Q.Query = SearchString
    Q.SortBy = "rank[d]"
    Q.Columns = "DocTitle, vpath, path, filename, size, write, characterization"
    util.AddScopeToQuery Q, "/Myfiles", "deep"
 
    set RS = Q.CreateRecordSet("nonsequential")
 
    RS.PageSize = 10
    ActiveQuery = TRUE
 
  elseif UseSavedQuery then
    if IsObject( Session("Query") ) And IsObject( Session("RecordSet") ) then
      set Q = Session("Query")
      set RS = Session("RecordSet")
 
      if RS.RecordCount <> -1 and NextPageNumber <> -1 then
        RS.AbsolutePage = NextPageNumber
        NextRecordNumber = RS.AbsolutePosition
      end if
 
      ActiveQuery = TRUE
    else
      Response.Write "ERROR - No saved query"
    end if
  end if
%>
```



This section is executed only if the *SearchString* variable has been set (that is, only if you have typed a query into the form and clicked the **New Query** button). This section contains many of the same elements as the sample .idq file in [Controlling the Search (.Idq File)](controlling-the-search--idq-file-.md). Notice the differences in syntax.

<dl> <dt>

<span id="set_Q___Server.CreateObject__ixsso.Query___and_set_util___Server.CreateObject__ixsso.util__"></span><span id="set_q___server.createobject__ixsso.query___and_set_util___server.createobject__ixsso.util__"></span><span id="SET_Q___SERVER.CREATEOBJECT__IXSSO.QUERY___AND_SET_UTIL___SERVER.CREATEOBJECT__IXSSO.UTIL__"></span>set Q = Server.CreateObject("ixsso.Query") and set util = Server.CreateObject("ixsso.util")
</dt> <dd>

These lines define the server-side [**Query**](iixssoquery.md) and [**Utility**](iixssoutil.md) objects. The rest of the commands in this group can then refer to these objects.

</dd> <dt>

<span id="Q.Query___SearchString"></span><span id="q.query___searchstring"></span><span id="Q.QUERY___SEARCHSTRING"></span>Q.Query = SearchString
</dt> <dd>

Sets the query string (restriction) used to search all virtual directories on the server.

</dd> <dt>

<span id="Q.SortBy____rank_d__"></span><span id="q.sortby____rank_d__"></span><span id="Q.SORTBY____RANK_D__"></span>Q.SortBy = "rank\[d\]"
</dt> <dd>

Sorts the results of searches in rank-descending order (highest rank first).

</dd> <dt>

<span id="Q.Columns____DocTitle__vpath__path__filename__size__write__characterization_"></span><span id="q.columns____doctitle__vpath__path__filename__size__write__characterization_"></span><span id="Q.COLUMNS____DOCTITLE__VPATH__PATH__FILENAME__SIZE__WRITE__CHARACTERIZATION_"></span>Q.Columns = "DocTitle, vpath, path, filename, size, write, characterization"
</dt> <dd>

Indicates the kind of information returned in the results.

</dd> <dt>

<span id="util.AddScopeToQuery_Q____Myfiles____deep_"></span><span id="util.addscopetoquery_q____myfiles____deep_"></span><span id="UTIL.ADDSCOPETOQUERY_Q____MYFILES____DEEP_"></span>util.AddScopeToQuery Q, "/Myfiles", "deep"
</dt> <dd>

Restricts the scope to the listed virtual directories. In this example, Indexing Service searches documents in the directory Myfiles, as well as all its subdirectories ("deep").

</dd> </dl>

 

 




