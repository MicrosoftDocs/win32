---
Description: IsapiRequestQueueSize
ms.assetid: 64b575a1-eb6a-4836-94c7-4699d7b325fa
title: IsapiRequestQueueSize
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsapiRequestQueueSize

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsapiRequestQueueSize** entry is the maximum number of server query requests to queue while Indexing Service is busy with other queries.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Requests       |
| Default: | 16             |
| Range:   | 0 - 100000     |



 

### Remarks

If the number of query requests exceeds the value of the **IsapiRequestQueueSize** entry, subsequent query requests fail. To allow simultaneous queuing of more queries, increase this value.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[IsapiRequestThresholdFactor](isapirequestthresholdfactor.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



