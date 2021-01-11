---
description: The optional <locationProvider> element specifies the search provider to be used by the web service provider search connector. This element contains one mandatory attribute and an optional child element.
ms.assetid: 5481b1ae-e166-4f09-bf0d-d6b7f7c8a331
title: locationProvider Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# locationProvider Element (Search Connector Schema)

The optional <locationProvider> element specifies the search provider to be used by the web service provider search connector. This element contains one mandatory attribute and an optional child element.

## Syntax


```
<!-- locationProvider -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="locationProvider" minOccurs="0">
                <xs:complexType>
                    <xs:all>
                        <xs:element name="propertyBag" type="propertyStoreType" minOccurs="0"/>
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



## Element Information



| Parent Element                                                                                                   | Child Elements                                                                       |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) | [propertyBag Element (Search Connector Schema)](search-schema-sconn-propertybag.md) |



 

## Attributes



| Attribute | Description                                                    |
|-----------|----------------------------------------------------------------|
| @clsid    | Required. The class identifier (CLSID) of the search provider. |
| codebase  | Optional.                                                      |



 

## Remarks

The @clsid attribute value for the OpenSearch provider is {48E277F6-4E74-4cd6-BA6F-FA4F42898223}.

File system and protocol handler based search connectors can use the [<simpleLocation>](search-schema-sconn-simplelocation.md) element instead. If <locationProvider> is present, there MUST NOT be a <simpleLocation> element in the Search Connector description.

## Example of a locationProvider Element


```
<locationProvider clsid="{48E277F6-4E74-4cd6-BA6F-FA4F42898223}">
    <propertyBag>
        <property name="OpenSearchShortName">MSDN</property>
        <property name="OpenSearchQueryTemplate">https://social.msdn.microsoft.com/Search/Feed.aspx?locale=en-US&Query={searchTerms}&format=RSS&StartIndex={startIndex}</property>
        <property name="MaximumResultCount" type="uint32">100</property>
    </propertyBag>
</locationProvider>
```



 

 



