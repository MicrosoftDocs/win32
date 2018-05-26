---
title: IMAPSvcInstance
description: IMAPSvcInstance
ms.assetid: 1e334ad1-7bfe-4061-8856-e452f27f2cff
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMAPSvcInstance

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IMAPSvcInstance** entry is the instance number of the Internet Mail Access Protocol (IMAP) virtual server that contains virtual roots to index.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 1                           |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The value of the **IMAPSvcInstance** entry applies only to virtual mail servers of IIS and only if the value of the [IsIndexingIMAPSvc](isindexingimapsvc.md) entry is set to one.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




