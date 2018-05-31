---
title: Property Types
description: Property Types
ms.assetid: 223dc156-c183-4058-afed-e88792eb9d66
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Types

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Each document property represents either unformatted text or a formatted value. Thus, each property is said to be either a text-type or a value-type property. Text-type properties describe the possibly complex content of a document. Value-type properties describe a single property of the entire document.

A text-type property has only unformatted text associated with its name. A value-type property has a data type ID and a value of that data type associated with its name. The data type ID can be textual (for example, VT\_LPWSTR) or non-textual (for example, VT\_I8). If a value-type property is cached, it also has an associated cached size and a storage level, which is either primary or secondary. For details about caching and storage level, see [Property Indexing](property-indexing.md).

The following table gives either the friendly name or the [PROPSPEC](_stg_propspec) string name of several properties and fills in the details appropriate for each property type.



| Name          | Type                | Data Type Identifier | Cached Size | Storage Level |
|---------------|---------------------|----------------------|-------------|---------------|
| Contents      | Text                | –                    | –           | –             |
| Size          | Value (non-textual) | VT\_I8               | 8 bytes     | Secondary     |
| DocTitle      | Value (textual)     | VT\_LPWSTR           | 4 bytes     | Secondary     |
| "description" | Value (textual)     | VT\_LPWSTR           | 4 bytes     | Secondary     |
| HtmlHeading1  | Text                | –                    | –           | –             |



 

The text-type property named Contents is a special case. It corresponds to the main body of unformatted text in a document. A document can have any number of instances of text-type properties with the same name (and typically might have many words associated with the Contents property). However, a processed document can retain the value from only one instance (usually the one encountered last) of a value-type property with a specific name.

The type of a document property determines how Indexing Service indexes the property and the kind of querying Indexing Service can perform with the property. For details about indexing, see [Property Indexing](property-indexing.md), and for details about querying, see [Property Querying](property-querying.md).

 

 




