---
title: Setting Up the Header
description: Setting Up the Header
ms.assetid: '08fbd123-d166-4f6f-b55e-ec81bff5c78e'
---

# Setting Up the Header

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The &lt;SCRIPT LANGUAGE&gt; and &lt;/SCRIPT&gt; tags turn scripting on and off. This example turns on a Microsoft Visual Basic Scripting Edition (VBScript) command, **option explicit**.


```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 3.0//EN" "html.dtd">
<HTML>
<HEAD>
 
    <SCRIPT LANGUAGE="VBScript" RUNAT="Server">
    <!--
        option explicit
      -->
    </SCRIPT>
 
    <TITLE>Index Server Search Form</TITLE>
 
    <META NAME="<b>DESCRIPTION</b>" CONTENT="Sample ASP query form for Microsoft Index Server">
    <META NAME="<b>KEYWORDS</b>"    CONTENT="query, content, hit, asp">
    <META NAME="<b>MS.LOCALE</b>"   CONTENT="EN-US">
    <META HTTP-EQUIV="<b>Content-Type</b>" CONTENT="text/html" charset=Windows-1252">
```



In the preceding HTML code, the bold type contains a sampling of meta tags:

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Sets the abstract that a client sees in the query results.

</dd> <dt>

<span id="Keywords"></span><span id="keywords"></span><span id="KEYWORDS"></span>**Keywords**
</dt> <dd>

Lists keywords a client can search for in a query.

</dd> <dt>

<span id="MS.Locale"></span><span id="ms.locale"></span><span id="MS.LOCALE"></span>**MS.Locale**
</dt> <dd>

Sets the language code for this form. EN-US stands for American English. For a complete list of supported language codes, see [Valid Locale Identifiers](valid-locale-identifiers.md).

</dd> <dt>

<span id="Content-Type"></span><span id="content-type"></span><span id="CONTENT-TYPE"></span>**Content-Type**
</dt> <dd>

Determines the character set (charset) that is used; for example, the Latin alphabet or the Hebrew alphabet. For a complete set of supported tags, see [Recognized Character Set Tags](recognized-character-set-tags.md).

</dd> </dl>

The next section turns form variables into server-side VBScript variables. The actual query form appears later in the file. Positioning the form data here allows the form fields to be pre-initialized, which causes the text of your query to reappear in the form field after the query results are displayed.


```
<%
    NewQuery = FALSE
    UseSavedQuery = FALSE
    <b>QueryForm = Request.ServerVariables( "PATH_INFO" )</b>
    SearchString = ""
    if Request.ServerVariables("REQUEST_METHOD") = "POST" then
        SearchString = Request.Form("SearchString")
        pg = Request.Form("pg")
 
        if pg <> "" then
           NextPageNumber = pg
           NewQuery = FALSE
           UseSavedQuery = TRUE
        else
            NewQuery = SearchString <> ""
        end if
     end if
 
 %>
</HEAD>
```



Also, the line in bold type defines the query form as the current file. From that point on, the file is referred to as **QueryForm**. This line allows you to change the name of the file without having to change the name anywhere within the file.

 

 




