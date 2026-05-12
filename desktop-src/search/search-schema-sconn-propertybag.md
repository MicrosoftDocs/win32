---
description: The required &lt;propertyBag&gt; element specifies a set of one or more properties used by this location provider.
ms.assetid: 63f8f2e4-3b52-4d6e-8d3a-2e133aac0e86
title: propertyBag element (search connector schema)
ms.topic: reference
ms.date: 05/31/2018
---

# propertyBag element (search connector schema)

The required &lt;propertyBag&gt; element specifies a set of one or more properties used by this location provider.

## Syntax


```
<!-- propertyBag -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
        ...
            <xs:element name="locationProvider" minOccurs="0">
                <xs:complexType>
                    <xs:all>
                        <xs:element name="propertyBag" type="propertyStoreType" minOccurs="0">
                            <xs:element name="property" minOccurs="0" maxOccurrs="unbounded"/>
                        </xs:element>
                    </xs:all>
                <xs:attribute name="clsid" use="required"/>
                <xs:attribute name="codebase" type="xs:string"/>
            </xs:element>
        ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element information



| Parent Element                                                                                 | Child Elements                                                                                 |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [locationProvider Element (Search Connector Schema)](search-schema-sconn-locationprovider.md) | [property Element (Search Connector Schema)](search-schema-sconn-locationproviderproperty.md) |



 

## Example of a PropertyBag element and property elements


```
<locationProvider clsid="{48E277F6-4E74-4cd6-BA6F-FA4F42898223}">
    <propertyBag>
        <property name="OpenSearchShortName">MSDN</property>
        <property name="OpenSearchQueryTemplate">https://social.msdn.microsoft.com/Search/Feed.aspx?locale=en-US&Query={searchTerms}&format=RSS&StartIndex={startIndex}</property>
        <property name="MaximumResultCount" type="uint32">100</property>
    </propertyBag>
</locationProvider>
```



 

 



