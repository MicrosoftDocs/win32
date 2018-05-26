---
title: IsapiMaxRecordsInResultSet
description: IsapiMaxRecordsInResultSet
ms.assetid: 47049cf7-b965-4823-9b16-010d0594d6f6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IsapiMaxRecordsInResultSet

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsapiMaxRecordsInResultSet** entry is the maximum number of rows in the result set generated when processing a query made using ISAPI.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Rows           |
| Default: | 5,000          |
| Range:   | 0 - 1000000    |



 

### Remarks

The value of the **IsapiMaxRecordsInResultSet** entry applies only to queries made using ISAPI and not to queries made using OLE DB.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




