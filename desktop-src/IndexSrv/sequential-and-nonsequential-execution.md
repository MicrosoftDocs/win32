---
title: Sequential and Nonsequential Execution
description: Sequential and Nonsequential Execution
ms.assetid: '4658699a-79a0-4f10-80bd-920b56abd0de'
---

# Sequential and Nonsequential Execution

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A query can be executed sequentially (results fetched as needed) or it can be executed nonsequentially (results cached on the server). A sequential query requires fewer server resources, but also has some limitations. Backward scrolling ([CiBookmarkSkipCount](parameter-for-use-with-bookmarks.md#-idxs-cibookmarkskipcount-var) &lt; 0) will re-execute the query and scroll forward to the specified position. Sequential queries cannot refer to the following variables: [CiMatchedRecordCount](read-only-variables-available-in-htx-files.md#-idxs-cimatchedrecordcount-var), [CiRecordsNextPage](read-only-variables-available-in-htx-files.md#-idxs-cirecordsnextpage-var), and [CiTotalNumberPages](read-only-variables-available-in-htx-files.md#-idxs-citotalnumberpages-var).

Either of the following actions will force a query to be nonsequential:

-   Referring to the [CiMatchedRecordCount](read-only-variables-available-in-htx-files.md#-idxs-cimatchedrecordcount-var), [CiRecordsNextPage](read-only-variables-available-in-htx-files.md#-idxs-cirecordsnextpage-var) or [CiTotalNumberPages](read-only-variables-available-in-htx-files.md#-idxs-citotalnumberpages-var) variables in the .htx page.
-   Setting the [CiSort](variables-in-forms-and-in-idq-files.md#-idxs-cisort-var) parameter to sort of query results other than the native order of the result. CiSort can safely be set to sort ascending on WorkId (CiSort=WorkId\[a\]) or descending on Rank (CiSort=Rank\[d\]).

 

 




