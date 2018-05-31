---
title: MajorVersion
description: MajorVersion
ms.assetid: 2e89209f-5cb9-49cd-a833-f583a03c905b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MajorVersion

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MajorVersion** entry indicates the major version number of the installed Indexing Service.

### Summary



|          |                             |
|----------|-----------------------------|
| Type:    | **REG\_DWORD**              |
| Default: | 3                           |
| Range:   | 1 - 4294967295 (0xFFFFFFFF) |



 

### Remarks

The complete version of Indexing Service is the value of **MajorVersion** combined with the value of the [MinorVersion](minorversion.md) entry. For example, if there were a Version 3.1, the value of this entry would be 3.

This entry should not be changed except by installation of an upgraded version of Indexing Service.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




