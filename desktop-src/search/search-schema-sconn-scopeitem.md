---
description: The &lt;scopeItem&gt; element represents a single entry in the exclusion/inclusion scope table.
ms.assetid: 18a58b3b-771c-4829-b3d4-253383b4bee8
title: scopeItem Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# scopeItem Element (Search Connector Schema)

The &lt;scopeItem&gt; element represents a single entry in the exclusion/inclusion scope table. &lt;scopeItem&gt; extends the standard shellLinkType type by adding three new elements that control inclusion and exclusion of folders, control the depth of results, and specify the location of the scope. If the &lt;scope&gt; element exists, this element is required. It has three child elements and no attributes.

## Syntax


```
<!-- scopeItem -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
        ...
        <xs:element name="scope" minOccurs="0">
            <xs:complexType>
                <xs:sequence minOccurs="0">
                    <xs:element name="scopeItem" maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:all>
                                <xs:element name="mode" default="Include">
                                    ...
                                </xs:element>
                                <xs:element name="depth" default="Shallow" minOccurs="0">
                                    ...
                                </xs:element>
                                <xs:element name="url" type="xs:anyURI"/>
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



| Parent Element                                                           | Child Elements                                                                        |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [scope Element (Search Connector Schema)](search-schema-sconn-scope.md) | [scope Element (Search Connector Schema)](search-schema-sconn-scope-mode.md).        |
|                                                                          | [scope Element (Search Connector Schema)](search-schema-sconn-scope-depth.md).       |
|                                                                          | [scopeItem url Element (Search Connector Schema)](search-schema-sconn-scope-url.md). |



 

## Remarks

Use the &lt;scope&gt; and &lt;scopeItem&gt; elements to identify which locations should be searched and which locations should be excluded from searching.

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



 

 



