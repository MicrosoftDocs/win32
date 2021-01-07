---
description: The <simpleLocation> element specifies the location for search connectors that are file-system based or protocol-handler based. This element has two child elements and no attributes.
ms.assetid: 04ffc178-0a76-4870-a075-a2ecd31937a1
title: simpleLocation Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# simpleLocation Element (Search Connector Schema)

The <simpleLocation> element specifies the location for search connectors that are file-system based or protocol-handler based. This element has two child elements and no attributes.

## Syntax


```
<!-- simpleLocation -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="simpleLocation" type="shellLinkType" minOccurs="0">
                <xs:all>
                    <xs:element name="url" type="xs:anyURI"/>
                    <xs:element name="serialized" minOccurs="0"/>
                </xs:all>
                
            </xs:element>
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) | [simpleLocation url Element (Search Connector Schema)](search-schema-sconn-url.md)                                                                                                                                                                                                                                |
|                                                                                                                  | serialized: This element contains the base64-encoded ShellLink pointing to the location defined in the <url> element. Windows 7 creates the ShellLink from the value of the <url> element and properly updates this field on the first load of this library, so it should be left empty by the author. |



 

## Remarks

This element can be used instead of <locationProvider> when the location is on the file system or the connector is a known protocol handler (like mapi:). If <simpleLocation> is present, there MUST NOT be a <locationProvider> element. For web service provider search connectors, use the [<locationProvider>](search-schema-sconn-locationprovider.md) element instead.

## Examples


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <simpleLocation>
        <url>mapi://{S-1-5-21-2127521184-1604012920-1887927527-2779359}/</url>
    </simpleLocation>
    ...
</searchConnectionDescription>
```



 

 



