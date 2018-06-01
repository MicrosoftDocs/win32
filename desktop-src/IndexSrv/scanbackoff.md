---
Description: ScanBackoff
ms.assetid: ac5b27aa-288b-4ed8-a2ea-a9416ea344bb
title: ScanBackoff
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScanBackoff

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ScanBackoff** entry controls the relative use of system resources by Indexing Service when performing scans.

### Summary



|          |                                          |
|----------|------------------------------------------|
| Type:    | **REG\_DWORD**                           |
| Default: | 3                                        |
| Range:   | 0 - 20 (11 - 20 reserved for future use) |



 

### Remarks

A value of zero for the **ScanBackoff** entry specifies full use of the allowable system resources when Indexing Service is doing a scan. A value of 10 specifies very conservative use of system resources during the scan. Values in the range 11 - 20 are reserved for future use.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



