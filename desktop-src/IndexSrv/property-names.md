---
title: Property Names
description: Property Names
ms.assetid: c05099e0-0311-45eb-9b70-8484259fd9d1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Names

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Each document property has a unique name determined by a COM-compatible naming scheme; that is, both a globally unique identifier (GUID) for a property set and a "\_stg\_propspec"&gt;PROPSPEC structure (which specifies a numeric ID or a string name) uniquely define each property. Each property optionally can have one or more friendly names, which act as aliases for the property. For example, the same property could have different friendly names in different languages.

The following table includes several examples of document property names.



| Property Set GUID (Name)                                    | PROPSPEC ID or Name | Friendly Name |
|-------------------------------------------------------------|---------------------|---------------|
| b725f130-47ef-101a-a5f1-02608c9eebac  (PropertyStorage)     | 0x13                | Contents      |
| b725f130-47ef-101a-a5f1-02608c9eebac   (PropertyStorage)    | 0x0c                | Size          |
| f29f85e0-4ff9-1068-ab91-08002b27b3d9   (SummaryInformation) | 0x02                | DocTitle      |
| d1b5d3f0-c0b3-11cf-9a92-00a0c908dbf1   (MetaProperty)       | "description"       | (none)        |
| 70eb7a10-55d9-11cf-b75b-00aa0051fe20   (HtmlInformation)    | 0x03                | HtmlHeading1  |



 

These examples are just a few of the existing properties available in Indexing Service. For a complete list, see [Filtering Well-Known Properties](filtering-well-known-properties.md) and [List of Property Names for a Web Catalog](list-of-property-names-for-a-web-catalog.md). You can define and use additional properties for specific document types by entering the properties with the Microsoft Management Console (MMC) and by implementing a custom filter to extract them.

 

 




