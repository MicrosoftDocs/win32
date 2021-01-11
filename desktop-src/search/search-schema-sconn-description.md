---
description: The optional <description> element specifies a description for this search connector. This element has no child elements and no attributes.
ms.assetid: 0e9d806c-7dfd-4e7f-8843-15a4e22f317f
title: description Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# description Element (Search Connector Schema)

The optional <description> element specifies a description for this search connector. This element has no child elements and no attributes.

## Syntax


```
<!-- description -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="description" type="xs:string" minOccurs="0"/>
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



 

## Remarks

The description should be user-friendly as it may be used in tooltips.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="https://schemas.adventureworks.com/searchConnector">
    ...
    <description>Search AdventureWorks.com</description>
    ...
</searchConnectionDescription>
```



 

 



