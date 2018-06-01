---
Description: Record Numbers and Counts
ms.assetid: 98c933a3-dba3-4451-9f88-2c8e1ed3a332
title: Record Numbers and Counts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Record Numbers and Counts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [CiCurrentRecordNumber](https://www.bing.com/search?q=CiCurrentRecordNumber) built-in variable contains the record number of the current record (1-based). The record number starts at \[(*page-number* - 1) \* *records-per-page*\] + 1 for any page. Each time through the &lt;%begindetail%&gt; section, the value of CiCurrentRecordNumber increases by one.

The [CiMatchedRecordCount](https://www.bing.com/search?q=CiMatchedRecordCount) built-in variable contains the value of the total number of records matched in the query (limited to [CiMaxRecordsInResultSet](https://www.bing.com/search?q=CiMaxRecordsInResultSet)). The [CiRecordsNextPage](https://www.bing.com/search?q=CiRecordsNextPage) built-in variable contains the number of records that will appear on the next page. Referring to either CiMatchedRecordCount or CiRecordsNextPage will cause the query to be nonsequential.

 

 



