---
title: MaxActiveQueryThreads
description: MaxActiveQueryThreads
ms.assetid: '6646e4c4-9a52-42e0-b0df-86cec9e27be1'
---

# MaxActiveQueryThreads

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxActiveQueryThreads** entry is the maximum number of active threads to process queries made using ISAPI.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Threads        |
| Default: | 2              |
| Range:   | 1 - 1000       |



 

### Remarks

The product of the value of the **MaxActiveQueryThreads** entry and the value of the [**IsapiRequestThresholdFactor**](isapirequestthresholdfactor.md) entry establishes the maximum number of concurrently processed asynchronous queries made using ISAPI.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[IsapiRequestThresholdFactor](isapirequestthresholdfactor.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MinIdleQueryThreads](minidlequerythreads.md)
</dt> </dl>

 

 




