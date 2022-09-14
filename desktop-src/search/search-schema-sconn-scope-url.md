---
description: The &lt;url&gt; element specifies a URL that represents the scope of the search connector. This element has no child elements and no attributes.
ms.assetid: 5afd84aa-98e3-4118-845a-d4efad19a488
title: scopeItem url Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# scopeItem url Element (Search Connector Schema)

The &lt;url&gt; element specifies a URL that represents the scope of the search connector. This element has no child elements and no attributes.

## Syntax


```
<!-- url -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
        ...
        <xs:element name="scope" minOccurs="0">
            <xs:complexType>
                <xs:sequence minOccurs="0"><xs:all>
                    <xs:element name="scopeItem" maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:all>
                                ...
                                <xs:element name="url" type="xs:anyURI"/>
                            </xs:all>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence></xs:all>
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

The value can be a local file system path or a URL.

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
            <mode>Exclude</mode>
            <depth>Deep</depth>
            <url>C:\ExampleFolder\ExcludeMe</url>
        </scopeItem>
    </scope>
    ...
</searchConnectionDescription>
```



 

 



