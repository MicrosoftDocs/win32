---
title: MaxWordlistIo
description: MaxWordlistIo
ms.assetid: e0c067d4-b210-4686-b61e-90cf157e9883
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxWordlistIo

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxWordlistIo** entry specifies the system I/O threshold above which indexing (word-list creation) is delayed.

### Summary



|          |                                       |
|----------|---------------------------------------|
| Type:    | **REG\_DWORD**                        |
| Units:   | Kilobytes/second                      |
| Default: | 410 (approximately 2 MB in 5 seconds) |
| Range:   | 100 - 4294967295 (0xFFFFFFFF)         |



 

### Remarks

The value of the **MaxWordlistIo** entry provides one method of fine-tuning Indexing Service. Checking the I/O usage by the system is one of the ways Indexing Service limits its resource use so that it can remain an unobtrusive process.

When the disk-performance counters are enabled in the DISKPERF.exe process, the value of the [**MaxWordlistIoDiskPerf**](maxwordlistiodiskperf.md) entry is used instead of the value of this entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MaxWordlistIoDiskPerf](maxwordlistiodiskperf.md)
</dt> </dl>

 

 




