---
title: Record Numbers and Counts
description: Record Numbers and Counts
ms.assetid: '98c933a3-dba3-4451-9f88-2c8e1ed3a332'
---

# Record Numbers and Counts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [CiCurrentRecordNumber](read-only-variables-available-in-htx-files.md#-idxs-cicurrentrecordnumber-var) built-in variable contains the record number of the current record (1-based). The record number starts at \[(*page-number* - 1) \* *records-per-page*\] + 1 for any page. Each time through the &lt;%begindetail%&gt; section, the value of CiCurrentRecordNumber increases by one.

The [CiMatchedRecordCount](read-only-variables-available-in-htx-files.md#-idxs-cimatchedrecordcount-var) built-in variable contains the value of the total number of records matched in the query (limited to [CiMaxRecordsInResultSet](variables-in-forms-and-in-idq-files.md#-idxs-cimaxrecordsinresultset-var)). The [CiRecordsNextPage](read-only-variables-available-in-htx-files.md#-idxs-cirecordsnextpage-var) built-in variable contains the number of records that will appear on the next page. Referring to either CiMatchedRecordCount or CiRecordsNextPage will cause the query to be nonsequential.

 

 




