---
description: The optional Boolean &lt;isDefaultSaveLocation&gt; element specifies whether the location described in the search connector should be used as the default save location. This element has no child elements and no attributes.
ms.assetid: 4a33f411-d71e-41d3-b5fd-018a92dceeac
title: isDefaultSaveLocation Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# isDefaultSaveLocation Element (Search Connector Schema)

The optional Boolean &lt;isDefaultSaveLocation&gt; element specifies whether the location described in the search connector should be used as the default save location. This element has no child elements and no attributes.

## Syntax


```
<!-- isDefaultSaveLocation -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="isDefaultSaveLocation" type="xs:boolean" minOccurs="0"/>
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

When a user chooses to save an item, Windows Explorer saves the item to the location specified in the &lt;simpleLocation&gt; element. Users can change this setting using the Properties dialog for the search connector.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <isDefaultSaveLocation>true</isDefaultSaveLocation>
    ...
</searchConnectionDescription>
```



 

 



