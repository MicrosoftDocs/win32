---
title: Creating Query Forms
description: Creating Query Forms
ms.assetid: '40615954-2ec8-4abc-b7d8-88e68c88e0c9'
---

# Creating Query Forms

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

With Internet Information Services (IIS) installed, you can customize the query forms that an end user fills in to initiate a search on the Web catalog.

Processing any Indexing Service query involves three steps:

-   **Presenting the Query:** Designing the HTML page or form to request a search string from a Web client, usually an end user.
-   **Controlling the Query:** Allowing the user to enter qualifications that determine how the search is controlled. You may set up defaults that are reasonable for your Web catalog and not give the novice end user control, or you may give advanced users more control over how the search is performed.
-   **Presenting the Query Results:** Format the resulting hits and allow the user to scroll through them.

Query forms for server-side scripting may be created in two ways:

-   **Active Server Pages (ASP) Query Form:** Use ASP when you do not anticipate a large number of queries against a Web catalog. Active Server Pages are easier to program and easier to change but they take more time to process by the server. All three of the above-mentioned query steps are combined into one .asp file. The [**Query**](iixssoquery.md) and [**Utility**](iixssoutil.md) objects are Indexing Service Server-Side Objects (IXSSO) that allow you to control the query and results through properties and methods on the **Query** object.
-   **Internet Server Application Programming Interface (ISAPI) Internet Data Query (.idq file) Query Form:** Use an .idq file when you have a large number of queries against a catalog. With this process, the three query steps are performed by separate files. The .idq files initially take longer to set up, but they execute faster on the server. Use .idq files to set up the query form and HTML Extension (.htx) files to format the results.
-   This section contains detailed information in the following topics:
-   [Creating an Active Server Pages Query Form](creating-an-active-server-pages-query-form.md)
-   [Creating a Static Query Form](creating-a-static-query-form.md)
-   [Support for Multiple Languages](support-for-multiple-languages.md)
-   [Variables in .Idq and .Htx Files](variables-in-idq-and-htx-files.md)
-   [Variables within Query Strings](variables-within-query-strings.md)

 

 




