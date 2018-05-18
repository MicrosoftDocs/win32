---
title: Query Result Pages
description: Query Result Pages
ms.assetid: 'fe340a76-2716-4780-abc3-481d9169039d'
---

# Query Result Pages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses the .htx file mainly to format the results of a query. Query results are split into pages based upon the parameter [CiMaxRecordsPerPage](variables-in-forms-and-in-idq-files.md#-idxs-cimaxrecordsperpage-var). The total number of query result records is governed by the parameter [CiMaxRecordsInResultSet](variables-in-forms-and-in-idq-files.md#-idxs-cimaxrecordsinresultset-var). The current page number in the result set is given in the variable [CiCurrentPageNumber](read-only-variables-available-in-htx-files.md#-idxs-cicurrentpagenumber-var). For a nonsequential query, the [CiTotalNumberPages](read-only-variables-available-in-htx-files.md#-idxs-citotalnumberpages-var) variable gives the total number of pages in the result and [CiRecordsNextPage](read-only-variables-available-in-htx-files.md#-idxs-cirecordsnextpage-var) gives the number of records on the next page. The variables [CiContainsFirstRecord](read-only-variables-available-in-htx-files.md#-idxs-cicontainsfirstrecord-var) and [CiContainsLastRecord](read-only-variables-available-in-htx-files.md#-idxs-cicontainslastrecord-var) indicate if the current page is the first or last in the result set. For an example of how to navigate between pages See [Navigating Between Pages in Query Results](navigating-between-pages-in-query-results.md).

 

 




