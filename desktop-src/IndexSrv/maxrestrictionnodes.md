---
title: MaxRestrictionNodes
description: MaxRestrictionNodes
ms.assetid: 3277768f-2c07-423c-8def-06737874d06a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxRestrictionNodes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxRestrictionNodes** entry is the maximum number of query restriction nodes that can be created by Indexing Service in a single query.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Units:   | Nodes                       |
| Default: | 5000                        |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

If query normalization creates a query restriction that is greater than the value of the **MaxRestrictionNodes** entry, the query fails with the status of QUERY\_E\_TOOCOMPLEX. This status message means the query was too complex to be completed because it surpassed the limit imposed in this registry key. The value of this entry keeps a user from overloading the capacity of the server with a complex query.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




