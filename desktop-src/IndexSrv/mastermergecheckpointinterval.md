---
title: MasterMergeCheckpointInterval
description: MasterMergeCheckpointInterval
ms.assetid: 9bbd4059-124a-4c5e-b7ba-1b6d7af7f0b3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MasterMergeCheckpointInterval

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MasterMergeCheckpointInterval** entry is the amount of information indexed before Indexing Service generates a checkpoint for a master merge.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Kilobytes      |
| Default: | 2048           |
| Range:   | 256 - 4096     |



 

### Remarks

The value of the **MasterMergeCheckpointInterval** entry determines how much work (data written to the new master index) needs to be redone if a master merge is paused and restarted.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




