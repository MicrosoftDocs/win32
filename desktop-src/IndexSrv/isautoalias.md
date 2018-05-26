---
title: IsAutoAlias
description: IsAutoAlias
ms.assetid: c5ff0c61-6f35-48e4-9bef-88ae7383de9e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IsAutoAlias

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsAutoAlias** entry controls whether Indexing Service automatically creates aliases for file shares.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

Set the value of the **IsAutoAlias** entry to one to enable aliasing. Aliasing is a convenience for users accessing remote shares because it allows such users to get a friendly UNC path.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




