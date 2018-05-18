---
title: Effect of Parameters on Query Performance
description: Effect of Parameters on Query Performance
ms.assetid: '03cf02c6-b21a-42a7-944d-06fce8a052cf'
---

# Effect of Parameters on Query Performance

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The fastest query is a *sequential* query that uses the *content index*. Certain parameter settings will force the query engine to use a less-efficient method to resolve the query. To guarantee fast queries, set [CiSort](variables-in-forms-and-in-idq-files.md#-idxs-cisort-var) to nothing (or descending by rank) set [CiForceUseCi](variables-in-forms-and-in-idq-files.md#-idxs-ciforceuseci-var) to TRUE, and do not reference [CiMatchedRecordCount](read-only-variables-available-in-htx-files.md#-idxs-cimatchedrecordcount-var), [CiRecordsNextPage](read-only-variables-available-in-htx-files.md#-idxs-cirecordsnextpage-var), or [CiTotalNumberPages](read-only-variables-available-in-htx-files.md#-idxs-citotalnumberpages-var) in the .htx template.

 

 




