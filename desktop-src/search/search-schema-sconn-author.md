---
description: The optional <author> element specifies the author of this library. This element has no child elements and no attributes.
ms.assetid: c91042d5-9564-463a-9104-97b927027fc9
title: author Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# author Element (Search Connector Schema)

The optional <author> element specifies the author of this library. This element has no child elements and no attributes.

## Syntax


```
<!-- author -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="author" type="xs:string" minOccurs="0"/>
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements |
|------------------------------------------------------------------------------------------------------------------|----------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) |                |



 

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="https://schemas.adventureworks.com/searchConnector">
    ...
    <author>Joe Smith</author>
    ...
</searchConnectionDescription>
```



 

 



