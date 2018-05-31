---
title: IsIndexingIMAPSvc
description: IsIndexingIMAPSvc
ms.assetid: bbd99579-2ae0-425c-b02a-999a779c27d0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsIndexingIMAPSvc

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsIndexingIMAPSvc** entry determines whether Indexing Service configures itself to work with Internet Mail Access Protocol (IMAP) mail messages.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 0              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **IsIndexingIMAPSvc** entry to one to configure the catalog to work with IMAP mail. Set it to zero to bypass indexing of IMAP mail.

When the value of this entry is set to one, the virtual server specified by the [IMAPSvcInstance](imapsvcinstance.md) is indexed.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[IMAPSvcInstance](imapsvcinstance.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




