---
Description: IsapiMaxRecordsInResultSet
ms.assetid: 47049cf7-b965-4823-9b16-010d0594d6f6
title: IsapiMaxRecordsInResultSet
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsapiMaxRecordsInResultSet

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

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

 

 



