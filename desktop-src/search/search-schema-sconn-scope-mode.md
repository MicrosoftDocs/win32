---
description: The &lt;mode&gt; element specifies whether the URL should be included or excluded from the scope of the search connector. The allowed values are Include and Exclude. This element has no child elements and no attributes.
ms.assetid: 7654c04a-31c4-4260-a51c-0600804e62a9
title: mode Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# mode Element (Search Connector Schema)

The &lt;mode&gt; element specifies whether the URL should be included or excluded from the scope of the search connector. The allowed values are `Include` and `Exclude`. This element has no child elements and no attributes.

## Syntax


```
<!-- mode -->
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
                                <xs:element name="mode" default="Include">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="Include"/>
                                            <xs:enumeration value="Exclude"/>
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

An excluded scope cannot be searched or browsed. You can nest scopeItem URLs. For example, you can include a parent scope and all its children except one by adding the parent URL as included, with depth value of Deep, and excluding the child URL.

## Example

The following example shows a search scope that includes C:\\ExampleFolder and all its child folders except C:\\ExampleFolder\\ExcludeMe.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <scope>
        <scopeItem>
            <mode>Include</mode>
            <depth>Deep</depth>
            <url>C:\ExampleFolder</url>
        </scopeItem>
        <scopeItem>
            <mode>Include</mode>
            <depth>Shallow</depth>
            <url>C:\ExampleFolder\ExcludeMe</url>
        </scopeItem>
    </scope>
    ...
</searchConnectionDescription>
```



 

 



