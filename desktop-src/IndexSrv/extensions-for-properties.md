---
title: Extensions for Properties
description: Extensions for Properties
ms.assetid: 6f3379ea-bc19-4ed1-8356-e8d692341e5f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Extensions for Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Columns can be either a standard Indexing Service property or a new property defined by a [SET PROPERTYNAME](set-propertyname.md) statement.

Standard properties available for all documents include the following.



| Property Name | Description                               |
|---------------|-------------------------------------------|
| All           | Matches words, phrases, and any property. |
| Contents      | Words and phrases in the document.        |
| Filename      | Name of the document.                     |
| Size          | Document size.                            |
| Write         | Last time the document was modified.      |



 

A query can also use ActiveX property values. Documents created by most ActiveX-aware applications can be queried for the following properties.



| Property Name | Description                  |
|---------------|------------------------------|
| DocTitle      | Title of the document.       |
| DocSubject    | Subject of the document.     |
| DocAuthor     | Author of the document.      |
| DocKeywords   | Keywords for the document.   |
| DocComments   | Comments about the document. |



 

There is also a list of additional standard Indexing Service properties that are available in queries. For the list, see [Default Property Names for a Web Catalog](default-property-names-for-a-web-catalog.md).

 

 




