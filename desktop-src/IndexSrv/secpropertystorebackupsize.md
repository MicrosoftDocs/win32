---
title: SecPropertyStoreBackupSize
description: SecPropertyStoreBackupSize
ms.assetid: 'a5438f45-e141-4f42-8d49-098396511279'
---

# SecPropertyStoreBackupSize

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SecPropertyStoreBackupSize** entry determines the number of system pages held in memory to back up the secondary property cache.

### Summary



|                     |                                                                                   |
|---------------------|-----------------------------------------------------------------------------------|
| Type:<br/>    | **REG\_DWORD**<br/>                                                         |
| Units:<br/>   | Pages<br/>                                                                  |
| Default:<br/> | 1024 (x86 processors),<br/> 512 (RISC processors)<br/>                |
| Range:<br/>   | 32 - 500000 (x86 processors),<br/> 16 - 250000 (RISC processors)<br/> |



 

### Remarks

For more details, see the [**PropertyStoreBackupSize**](propertystorebackupsize.md) entry, which serves the same function for the primary property cache.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[**PropertyStoreBackupSize**](propertystorebackupsize.md)
</dt> </dl>

 

 





