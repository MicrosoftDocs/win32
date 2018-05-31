---
title: MaxWordListIoDiskPerf
description: MaxWordListIoDiskPerf
ms.assetid: 0561f689-768c-4078-9530-94a956a9c707
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaxWordListIoDiskPerf

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxWordListIoDiskPerf** entry specifies the system I/O threshold above which indexing (word-list creation) is delayed when disk-performance counters are enabled.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Percent        |
| Default: | 10             |
| Range:   | 1 - 100        |



 

### Remarks

The value of the **MaxWordListIoDiskPerf** entry is enabled only if counters in the DISKPERF.exe process are enabled. When the disk-performance counters are enabled, the value of this entry is used instead of the value of the [**MaxWordlistIo**](maxwordlistio.md) entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> <dt>

[MaxWordlistIo](maxwordlistio.md)
</dt> </dl>

 

 




