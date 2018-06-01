---
Description: Properties of Documents
ms.assetid: 103ddfc0-b431-4a52-bf3a-acaf39e34bc2
title: Properties of Documents
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Properties of Documents

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service views the documents that it processes as objects with an assortment of properties. It separates the information that a document represents into these properties — according to their characteristics — as it filters, indexes, and queries the properties. This section describes the important characteristics of document properties and how Indexing Service processes them. The following table lists the topics in the section and describes the characteristic that each topic discusses.



| Topic                                        | Characteristic                                                                                                                          |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [Property Names](property-names.md)         | Each property has a unique name.                                                                                                        |
| [Property Types](property-types.md)         | Each property represents either unformatted text in the content of the document or a formatted value that describes the whole document. |
| [Property Filtering](property-filtering.md) | Properties are extracted from documents by filters implemented for specific document types.                                             |
| [Property Indexing](property-indexing.md)   | The type of a property determines what kind of indexing occurs for the property.                                                        |
| [Property Querying](property-querying.md)   | The type of a property determines what kind of querying can occur for the property.                                                     |



 

Indexing Service stores and accesses its information using the Microsoft [OLE DB Provider](ole-db-provider-for-indexing-service.md). Consequently, Indexing Service documentation sometimes uses database nomenclature — referring to document properties as attributes, columns, or fields — appropriate for the context.

 

 



