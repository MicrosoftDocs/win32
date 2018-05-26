---
title: MaxRunningWebhits
description: MaxRunningWebhits
ms.assetid: d7099da6-1b5b-4157-a113-4e94486a978a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MaxRunningWebhits

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MaxRunningWebhits** entry specifies the maximum number of concurrent instances of WEBHITS.DLL for use by ISAPI with a web server.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Default: | 20             |
| Range:   | 1 - 200        |



 

### Remarks

Increase the value of the **MaxRunningWebhits** entry for computers with more memory or processors.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




