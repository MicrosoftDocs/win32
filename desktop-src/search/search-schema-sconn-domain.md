---
description: The optional <domain> element specifies the URL of the search service used by this search connector. It is displayed in the details pane. This element has no child elements and no attributes.
ms.assetid: 60a27b13-0bb0-4cf6-9dce-a3abc79ce623
title: domain Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# domain Element (Search Connector Schema)

The optional <domain> element specifies the URL of the search service used by this search connector. It is displayed in the details pane. This element has no child elements and no attributes.

## Syntax


```
<!-- domain -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="domain" type="xs:string" minOccurs="0"/>
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

The URL should be the top-level domain for the search provider. For example, https://www.example.com.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="https://schemas.adventureworks.com/searchConnector">
    ...
    <domain>https://www.adventureworks.com</domain>
    ...
</searchConnectionDescription>
```



 

 



