---
Description: IsEnumAllowed
ms.assetid: 7627008a-a40d-46cd-b55a-9f1a94d92d5b
title: IsEnumAllowed
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsEnumAllowed

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsEnumAllowed** entry determines whether directory enumeration can be used to execute a query.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Units:   | Boolean        |
| Default: | 1              |
| Range:   | 0, 1           |



 

### Remarks

The value of the **IsEnumAllowed** entry overrides any value set in a specific query.

Setting the value of this entry to zero reduces the vulnerability of a server to misdirected enumeration queries, since enumeration queries can be slow and can seriously affect the performance of the server.

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 



