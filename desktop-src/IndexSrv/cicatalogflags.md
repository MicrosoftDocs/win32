---
title: CiCatalogFlags
description: CiCatalogFlags
ms.assetid: a3e1be38-5b7f-42ed-bc25-fd2600e725ad
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CiCatalogFlags

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **CiCatalogFlags** entry controls whether Indexing Service receives file-modification notifications from local or remote hosts.

### Summary



|          |                                       |
|----------|---------------------------------------|
| Type:    | **REG\_DWORD**                        |
| Default: | 0x00000000 (Enable all notifications) |
| Range:   | 0x00000000 - 0x00000003               |



 

### Remarks

The CiCatalogFlags entry enables all notifications when set to 0x00000000. When nonzero, it can be either of the following mask values or the logical **OR** operation of the two.



| Mask Value | Effect on Notifications                                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000001 | Disable notification processing for all remote universal naming convention (UNC) paths. Set this flag if Indexing Service is configured to index documents on a wide area network (WAN) over slow links. |
| 0x00000002 | Disable notification processing for all local paths.                                                                                                                                                     |



 

When either or both of remote and local notification processing is disabled, Indexing Service triggers periodic scans for the disabled paths. The registry entry [**ForcedNetPathScanInterval**](forcednetpathscaninterval.md) controls the frequency of scanning disabled paths.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




