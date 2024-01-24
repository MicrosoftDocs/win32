---
description: The optional Boolean &lt;isDefaultNonOwnerSaveLocation&gt; element specifies whether the location described in the search connector should be used as the default save location when a user from another computer in a Homegroup chooses to save an item.
ms.assetid: 4286b122-2454-4dc3-9c06-9967b7a763dd
title: isDefaultNonOwnerSaveLocation Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# isDefaultNonOwnerSaveLocation Element (Search Connector Schema)

The optional Boolean &lt;isDefaultNonOwnerSaveLocation&gt; element specifies whether the location described in the search connector should be used as the default save location when a user from another computer in a Homegroup chooses to save an item. This element has no child elements and no attributes.

## Syntax


```
<!-- isDefaultNonOwnerSaveLocation -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="isDefaultNonOwnerSaveLocation" type="xs:boolean" minOccurs="0"/>
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

If true, when a user from another computer in a Homegroup chooses to save an item, Windows Explorer saves the item to the location specified in the &lt;simpleLocation&gt; element.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <isDefaultNonOwnerSaveLocation>true</isDefaultNonOwnerSaveLocation>
    ...
</searchConnectionDescription>
```



 

 



