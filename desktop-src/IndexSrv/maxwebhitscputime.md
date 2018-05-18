---
title: MaxWebhitsCpuTime
description: MaxWebhitsCpuTime
ms.assetid: 'bddb1ab2-72b3-478d-8445-7e555491cace'
---

# MaxWebhitsCpuTime

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxWebhitsCpuTime** entry specifies the length of the time-out interval for WEBHITS.dll in CPU seconds.

### Summary



|          |                     |
|----------|---------------------|
| Type:    | **REG\_DWORD**      |
| Units:   | Seconds of CPU time |
| Default: | 30                  |
| Range:   | 5 - 7200            |



 

### Remarks

If WEBHITS.dll does not process a document in the time specified by the value of the **MaxWebhitsCpuTime** entry, it returns an error message indicating that the allowed time has been exceeded.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




