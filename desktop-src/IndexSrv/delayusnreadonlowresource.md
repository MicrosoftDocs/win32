---
title: DelayUsnReadOnLowResource
description: DelayUsnReadOnLowResource
ms.assetid: 746c093c-b3e0-4f26-8e34-c9fb53b56403
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DelayUsnReadOnLowResource

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DelayUsnReadOnLowResource** entry controls whether the USN journal, also known as the change-notification log, is examined under the following system conditions: low memory, high input/output (I/O), recent user activity, and running on battery power.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **DelayUsnReadOnLowResource** entry to one to prevent the reading of the USN journal as long as any of the system conditions exist.

Since indexing does not occur during these conditions, there's no point in examining the USN journal unless the journal has a fixed size ([MaxUsnLogSize](maxusnlogsize.md)) and is about to become full. When this happens, the data being written to the journal wraps around, and a beginning block ([USNLogAllocationDelta](usnlogallocationdelta.md)) is deleted to make room for more data. As a result, change notifications may be lost. If this seems likely, Indexing Service gives checking the USN journal a higher priority even if you have set this entry.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




