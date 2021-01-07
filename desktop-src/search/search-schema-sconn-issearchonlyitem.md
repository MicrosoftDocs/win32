---
description: The Boolean <isSearchOnlyItem> element specifies whether the search provider supports browse mode in addition to search mode. This element is optional and has no child elements and no attributes.
ms.assetid: eec1b735-ae78-48ef-8ebf-05b9fd038963
title: isSearchOnlyItem Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# isSearchOnlyItem Element (Search Connector Schema)

The Boolean <isSearchOnlyItem> element specifies whether the search provider supports browse mode in addition to search mode. This element is optional and has no child elements and no attributes.

## Syntax


```
<!-- isSearchOnlyItem -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            <xs:element name="isSearchOnlyItem" type="xs:boolean" default="false" minOccurs="0"/>
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

The value `true` indicates that the search connector location cannot be browsed by users. The value `false` indicates that users can browse the search connector location.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <isSearchOnlyItem>true</isSearchOnlyItem>
    ...
</searchConnectionDescription>
```



 

 



