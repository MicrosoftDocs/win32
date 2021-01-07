---
description: This optional <templateInfo> element specifies a folder type for displaying the results from a query over this search connector. This element has no attributes and only one mandatory child.
ms.assetid: fe42f589-5c47-4629-94eb-78dbaffa4112
title: templateInfo Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# templateInfo Element (Search Connector Schema)

This optional <templateInfo> element specifies a folder type for displaying the results from a query over this search connector. This element has no attributes and only one mandatory child.

## Syntax


```
<!-- templateInfo -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="templateInfo" minOccurs="0">
                <xs:complexType>
                    <xs:all>
                        <xs:element name="folderType" minOccurs="0"/>
                    </xs:all>
                </xs:complexType>
            </xs:element>
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements                                                                     |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) | [folderType Element (Search Connector Schema)](search-schema-sconn-foldertype.md) |



 

## Remarks

If you don't specify a particular folder type in the <templateInfo> element, Windows uses the general search connector folder type {8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}.

## Example of a templateInfo Element


```
<!-- templateInfo -->
<templateInfo>
    <folderType>{8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}</folderType>
</templateInfo
```



 

 



