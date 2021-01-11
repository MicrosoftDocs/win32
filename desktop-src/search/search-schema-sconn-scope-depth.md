---
description: The <depth> element specifies whether the search connector's scope should include child URLs. The allowed values are Deep and Shallow. This element has no child elements and no attributes.
ms.assetid: 859decab-cbe3-4cec-b37c-6d0e7c353876
title: depth Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# depth Element (Search Connector Schema)

The <depth> element specifies whether the search connector's scope should include child URLs. The allowed values are `Deep` and `Shallow`. This element has no child elements and no attributes.

## Syntax


```
<!-- depth -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
        ...
        <xs:element name="scope" minOccurs="0">
            <xs:complexType>
                <xs:sequence minOccurs="0">
                    <xs:element name="scopeItem" maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:all>
                                ...
                                <xs:element name="depth" default="Shallow" minOccurs="0">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="Shallow"/>
                                            <xs:enumeration value="Deep"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:element>
                                ...
                            </xs:all>
                        </xs:complexType>
                    </xs:element>
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
| [scopeItem Element (Search Connector Schema)](search-schema-sconn-scopeitem.md) |                |



 

## Remarks

If the depth is deep, users can browse or search items in the scopeItem's URL level or within any child URLs.

## Example

The following example shows a search scope that includes C:\\FolderA and all its child folders and C:\\FolderB but none of its child folders.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <scope>
        <scopeItem>
            <mode>Include</mode>
            <depth>Deep</depth>
            <url>C:\FolderA</url>
        </scopeItem>
        <scopeItem>
            <mode>Include</mode>
            <depth>Shallow</depth>
            <url>C:\FolderB</url>
        </scopeItem>
    </scope>
    ...
</searchConnectionDescription>
```



 

 



