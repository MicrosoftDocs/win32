---
description: The optional Boolean &lt;isIndexed&gt; element specifies whether the location described by the search connector is indexed (either locally or remotely using Windows Search 4 or higher).
ms.assetid: e72b5614-454c-481f-bc31-897d2dea8042
title: isIndexed Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# isIndexed Element (Search Connector Schema)

The optional Boolean &lt;isIndexed&gt; element specifies whether the location described by the search connector is indexed (either locally or remotely using Windows Search 4 or higher). The default value is true for local folders. This element has no child elements and no attributes.

## Syntax


```
<!-- isIndexed -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="isIndexed" type="xsIboolean" minOccurs="0"/>
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
    <isIndexed>false</isIndexed>
    ...
</searchConnectionDescription>
```



 

 



