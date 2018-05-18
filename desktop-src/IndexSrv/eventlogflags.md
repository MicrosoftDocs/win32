---
title: EventLogFlags
description: EventLogFlags
ms.assetid: 'aa1be4ef-ef40-4149-817a-6cfc61dd0ff0'
---

# EventLogFlags

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **EventLogFlags** entry controls the types of events that are logged to the system event message log.

### Summary



|          |                         |
|----------|-------------------------|
| Type:    | **REG\_DWORD**          |
| Default: | 0x00000002              |
| Range:   | 0x00000000 - 0x00000003 |



 

### Remarks

The **EventLogFlags** entry disables all the relevant event message types when set to 0x00000000. When nonzero, it can be either of the following mask values or the logical **OR** operation of the two.



| Mask Value | Controlled Event                                                  |
|------------|-------------------------------------------------------------------|
| 0x00000001 | Reserved.                                                         |
| 0x00000002 | One or more embedded objects in a document could not be filtered. |



 

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




