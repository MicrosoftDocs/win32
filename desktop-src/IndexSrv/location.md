---
title: Location
description: Location
ms.assetid: 809192fc-2a65-47b5-9404-05663528613b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Location

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **Location** entry indicates the full path to the catalog.

### Summary



|          |                                            |
|----------|--------------------------------------------|
| Type:    | **REG\_SZ**                                |
| Default: | "%SystemDrive%\\System Volume Information" |



 

### Remarks

The catalog that is named System defaults to the value of the **Location** entry if there is enough space on that drive. If that location does not exist, the catalog is put in the root directory of the disk. If %SystemDrive% does not have sufficient space available, Indexing Service looks for a suitable volume with sufficient space.

Reading the value of this entry allows you to check where the catalog is located.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> </dl>

 

 




