---
description: The &lt;url&gt; element specifies a URL to the thumbnail for this search connector. If &lt;imageLink&gt; exists, this element is required. It has no child elements and no attributes.
ms.assetid: addb2614-9f4f-4cab-a678-b6020b8c4648
title: imageLink url Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# imageLink url Element (Search Connector Schema)

The &lt;url&gt; element specifies a URL to the thumbnail for this search connector. If &lt;imageLink&gt; exists, this element is required. It has no child elements and no attributes.

## Syntax


```
<!-- url -->
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



| Parent Element                                                                   | Child Elements |
|----------------------------------------------------------------------------------|----------------|
| [imageLink Element (Search Connector Schema)](search-schema-sconn-imagelink.md) |                |



 

## Remarks

The value can be a local file system path or a URL. The image file can be any of the basic image types supported by Windows 7 (PNG, BMP, JPG, GIF).

## Example of an imageLinkurl Element


```
<imageLink>
    <imageLinkurl>%ProgramFiles%\Example\examplethumbnail.jpg</imageLinkurl>
</imageLink>
```



 

 



