---
description: The Boolean &lt;supportsAdvancedQuerySyntax&gt; element specifies whether the search provider supports the Advanced Query Syntax. The default is false. This element is optional and has no child elements and no attributes.
ms.assetid: d4aef1f1-63c8-4e9a-9e22-5efbb8c523b2
title: supportsAdvancedQuerySyntax Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# supportsAdvancedQuerySyntax Element (Search Connector Schema)

The Boolean &lt;supportsAdvancedQuerySyntax&gt; element specifies whether the search provider supports the [Advanced Query Syntax](-search-3x-advancedquerysyntax.md). The default is false. This element is optional and has no child elements and no attributes.

## Syntax


```
<!-- supportsAdvancedQuerySyntax -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="supportsAdvancedQuerySyntax" type="xs:boolean" default="false" minOccurs="0"/>
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

The value `true` indicates that the search provider supports Advanced Query Syntax sent in search queries.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <supportsAdvancedQuerySyntax>true</supportsAdvancedQuerySyntax>
    ...
</searchConnectionDescription>
```



 

 



