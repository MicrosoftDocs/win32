---
description: The optional &lt;propertyStore&gt; element specifies the location of an XML-based IPropertyStore to store open metadata for this search connector. This element has no attributes and only one child element.
ms.assetid: 5720c69f-af87-432b-857c-dbd66ba74e80
title: propertyStore Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# propertyStore Element (Search Connector Schema)

The optional &lt;propertyStore&gt; element specifies the location of an XML-based IPropertyStore to store open metadata for this search connector. This element has no attributes and only one child element.

## Syntax


```
<!-- propertyStore -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
        ...
        <xs:element name="propertyStore" type="propertyStoreType" minOccurs="0">
            <xs:element name="property" minOccurs="0" maxOccurrs="unbounded"/>
        </xs:element>
        ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements                                                                                            |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) | [property Element of propertyStore (Search Connector Schema)](search-schema-sconn-propstore-property.md) |



 

## Example

The following example shows a &lt;propertyStore&gt; element with two &lt;property&gt; elements.


```
<propertyStore>
    <property name="OpenSearchHTMLRolloverTemplate">https://www.adventureworks.com/Search/?Query={searchTerms}</property>
    <property name="isExternal" type="boolean">true</property>
</propertyStore>
```



 

 



