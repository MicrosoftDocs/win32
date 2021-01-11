---
description: The optional Boolean <includeInStartMenuScope> element specifies whether this search connector should be included in the Start menu search scope.
ms.assetid: 934a3834-9ddc-4c15-b738-68ea74adc24c
title: includeInStartMenuScope Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# includeInStartMenuScope Element (Search Connector Schema)

The optional Boolean <includeInStartMenuScope> element specifies whether this search connector should be included in the Start menu search scope. The default value is true for search connectors using the file system as a data source, and false for search connectors used by property handlers. This element has no child elements and no attributes.

## Syntax


```
<!-- includeInStartMenuScope -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="includeInStartMenuScope" type="xs:boolean" default="false" minOccurs="0"/>
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

If you include the search connector in the Start menu scope, users can search your location from the search box in the Start menu.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="https://schemas.adventureworks.com/searchConnector">
    ...
    <includeinStartMenuScope>true</includeinStartMenuScope>
    ...
</searchConnectionDescription>
```



 

 



