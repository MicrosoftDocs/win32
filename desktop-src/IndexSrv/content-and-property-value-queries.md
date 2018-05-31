---
title: Content and Property-Value Queries
description: Content and Property-Value Queries
ms.assetid: c0b0bf19-4ae6-4df4-b457-6e6ea70f6999
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Content and Property-Value Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service considers a document to be an assemblage of properties, which are either text-type or value-type. (See [Property Types](property-types.md) for a description of the types of properties.) Most queries of text-type properties involve the Contents property, so these queries are often called "content queries." Queries of value-type properties are similarly often called "property-value queries."

Queries involving text-type properties or textual value-type properties are limited in comparison to queries of nontextual value-type properties. For example, queries can contain Boolean operators when they involve either type of property, but queries can contain relational operators only when they involve value-type properties. (See [Property Querying](property-querying.md) for a description of properties and queries.)

 

 




