---
title: Server Variables
description: Server Variables
ms.assetid: 7f0a2b29-0b97-4c76-b69c-3434a2680dbb
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Server Variables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example shows how the QUERY\_STRING or form variables can be parsed from VBScript without the [**SetQueryFromURL**](iixssoquery-setqueryfromurl.md) method.


```VB
<%
    NewQuery = FALSE
    UseSavedQuery = FALSE
    SearchString = ""
    if Request.ServerVariables("REQUEST_METHOD") = "POST" then
        SearchString = Request.Form("SearchString")
        SortBy = Request.Form("SortBy")
        Colset = Request.Form("ColChoice")
        Catalog = Request.Form("Catalog")
        ' NOTE: this will be true only if the button is actually pushed.
        if Request.Form("Action") = "New Query" then
            NewQuery = TRUE
        end if
    end if
    if Request.ServerVariables("REQUEST_METHOD") = "GET" then
        SearchString = Request.QueryString("qu")
        SortBy = Request.QueryString("so")
        Colset = Request.QueryString("co")
        Catalog = Request.QueryString("ct")
        if Request.QueryString("pg") <> "" then
            NextPageNumber = Request.QueryString("pg")
            NewQuery = FALSE
            UseSavedQuery = TRUE
        else
            NewQuery = SearchString <> ""
        end if
    end if
 %>
```



 

 




