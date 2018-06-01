---
Description: IsapiRequestThresholdFactor
ms.assetid: 5317e5d5-9cb3-4746-878c-730acfd1f2a6
title: IsapiRequestThresholdFactor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsapiRequestThresholdFactor

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsapiRequestThresholdFactor** entry is a multiplier for determining the maximum number of threads per server that simultaneously process query requests.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Default: | 3              |
| Range:   | 1 - 100000     |



 

### Remarks

The maximum number of threads for processing query requests is the product of the value of the **IsapiRequestThresholdFactor** entry and the number of processors on the server. If the number of threads required exceeds that product, subsequent query requests are queued. To allow simultaneous processing of more queries, increase the value of **IsapiRequestThresholdFactor**.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[IsapiRequestQueueSize](isapirequestqueuesize.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



