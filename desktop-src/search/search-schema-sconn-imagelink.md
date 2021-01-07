---
description: The optional <imageLink> element specifies a thumbnail for this search connector. This element has one mandatory child element and no attributes.
ms.assetid: 71078d83-72f4-41f9-b80c-7ba0139206fb
title: imageLink Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# imageLink Element (Search Connector Schema)

The optional <imageLink> element specifies a thumbnail for this search connector. This element has one mandatory child element and no attributes.

## Syntax


```
<!-- imageLink -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="imageLink" minOccurs="0">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="url" type="xs:anyURI"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>            
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements                                                                           |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) | [imageLink url Element (Search Connector Schema)](search-schema-sconn-imagelink-url.md) |



 

## Remarks

The imageLink value can be a local file system path or a URL. The image file can be any of the basic image types supported by Windows 7 (PNG, BMP, JPG, GIF).

## Example of an imageLink Element


```
<imageLink>
    <imageLinkurl>%ProgramFiles%\Example\examplethumbnail.jpg</imageLinkurl>
</imageLink>
```



 

 



