---
title: Querying with Visual Basic
description: Querying with Visual Basic
ms.assetid: dd77c221-8ebc-40c1-8104-936cf6b2f7ec
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying with Visual Basic

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [VBQuery Sample](vbquery-sample.md) illustrates several querying tasks for Indexing Service using the [Query Helper](https://www.bing.com/search?q=Query Helper), [ActiveX Data Objects (ADO)](https://www.bing.com/search?q=ActiveX Data Objects (ADO)), and [OLE DB Helper](https://www.bing.com/search?q=OLE DB Helper) APIs. The VBQuery Sample has one primary form, **Main**, which contains the following controls.

-   A text box for the query text.
-   A text box for the selected scope of the query.
-   A command button for browsing to select the scope of the query.
-   A combo box for selecting the sort criteria. The default selection is "Rank\[d\]"
-   A combo box for selecting the query language. The possible selections are "Dialect 2", "SQL", and "Dialect 1". When either "Dialect" is selected, the query uses the Query Helper API. When "SQL" is selected, the query uses the ADO API.
-   A command button to begin execution of the query.
-   A command button to clear the current query settings.
-   A list view for displaying the results of the query.

The following topics discuss selected code segments from the **Main** form that perform actions specific to Indexing Service.

-   [Locating the Catalog for the Selected Scope](locating-the-catalog-for-the-selected-scope.md)
-   [Creating a Query Object with the Query Helper API](creating-a-query-object-with-the-query-helper-api.md)
-   [Creating a Recordset Object with the Query Helper API](creating-a-recordset-object-with-the-query-helper-api.md)
-   [Creating a Recordset Object with the ADO API](creating-a-recordset-object-with-the-ado-api.md)
-   [Using the Results from the Recordset Object](using-the-results-from-the-recordset-object.md)

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




