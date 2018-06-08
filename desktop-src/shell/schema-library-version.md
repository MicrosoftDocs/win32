---
Description: The &lt;version&gt; element specifies the content version of this library. This element has no attributes and no child elements.
ms.assetid: 77FD5EF6-6B6F-48e1-973F-AC069F729613
title: version Element (Library Schema)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# version Element (Library Schema)

The &lt;version&gt; element specifies the content version of this library. This element has no attributes and no child elements.

## Syntax

``` syntax
<!-- version -->
<xs:element name="version" type="xs:int" minOccurs="0"/>
```

## Element Information



| Parent Element                                                               | Child Elements |
|------------------------------------------------------------------------------|----------------|
| [libraryDescription Element (Library Schema)](schema-librarydescription.md) | None           |



 

## Remarks

The content version of the library is different from the library's file format (\*.library-ms) version. The library's file format version is specified in the [namespace](library-schema-entry.md).

## Related topics

<dl> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> <dt>

[Search Connector Description Schema](https://msdn.microsoft.com/windows/desktop/b85a04c6-9398-4cc7-a894-881216600203)
</dt> </dl>

 

 



