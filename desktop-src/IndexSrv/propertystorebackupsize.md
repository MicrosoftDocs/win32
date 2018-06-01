---
Description: PropertyStoreBackupSize
ms.assetid: d0b48421-9fc2-444d-9237-656331c04cdb
title: PropertyStoreBackupSize
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PropertyStoreBackupSize

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **PropertyStoreBackupSize** entry determines the number of system pages held on disk to back up the primary property cache.

### Summary



|                     |                                                                                   |
|---------------------|-----------------------------------------------------------------------------------|
| Type:<br/>    | **REG\_DWORD**<br/>                                                         |
| Units:<br/>   | Pages<br/>                                                                  |
| Default:<br/> | 1024 (x86 processors),<br/> 512 (RISC processors)<br/>                |
| Range:<br/>   | 32 - 500000 (x86 processors),<br/> 16 - 250000 (RISC processors)<br/> |



 

### Remarks

The page size is 4 kilobytes (KB) on *x*86 (486 and higher) computers and 8 KB on RISC (Alpha) computers. The larger the page file, the less often the property cache needs to be written to disk. The fewer times you write the cache to disk, the faster indexing proceeds. The range of values of the **PropertyStoreBackupSize** entry allows the PROPSTOR.BKP file to range in size from about 128 KB to about 2 gigabytes (GB).

The [**SecPropertyStoreBackupSize**](secpropertystorebackupsize.md) entry serves the same function for the secondary property cache.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[SecPropertyStoreBackupSize](secpropertystorebackupsize.md)
</dt> </dl>

 

 




