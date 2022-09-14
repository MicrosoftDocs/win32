---
description: The &lt;libraryDescription&gt; element is the top-level container for the library definition. This element is required.
ms.assetid: 62098944-E1B2-46e8-AC87-314C55F96B62
title: libraryDescription Element (Library Schema)
ms.topic: article
ms.date: 05/31/2018
---

# libraryDescription Element (Library Schema)

The &lt;libraryDescription&gt; element is the top-level container for the library definition. This element is required.

## Syntax


```
<!-- libraryDescription -->
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
    <xs:include schemaLocation="commonTypes-ms.xsd"/>
    <xs:element name="libraryDescription">
        <xs:complexType>
            <xs:all>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="ownerSID" minOccurs="0"/>
                <xs:element name="version" type="xs:int" minOccurs="0"/>
                <xs:element name="isLibraryPinned" type="xs:boolean" default="false" minOccurs="0"/>
                <xs:element name="iconReference" type="xs:string" minOccurs="0"/>
                <xs:element name="propertyStore" minOccurs="0">
                    <xs:complexType>
                        <xs:complexContent>
                            <xs:extension base="propertyStoreType"/>
                        </xs:complexContent>
                    </xs:complexType>
                </xs:element>
                <xs:element name="templateInfo" minOccurs="0">
                    <xs:complexType>
                        <xs:all>
                            <xs:element name="folderType" minOccurs="0"/>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
                <xs:element name="searchConnectorDescriptionList" minOccurs="0">
                    <xs:complexType>
                        <xs:sequence minOccurs="0">
                            <xs:element name="searchConnectorDescription" 
                             type="searchConnectorDescriptionType" minOccurs="0" 
                             maxOccurs="unbounded"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>
</xs:schema>
```



## Element Information



| Parent element | Child elements                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------------|
|                | [name Element (Library Schema)](schema-library-name.md). Required.                                                     |
|                | [ownerSID Element (Library Schema)](schema-library-ownersid.md). Optional.                                             |
|                | [version Element (Library Schema)](schema-library-version.md). Optional.                                               |
|                | [isLibraryPinned Element (Library Schema)](schema-library-islibrarypinned.md). Optional.                               |
|                | [iconReference Element (Library Schema)](schema-library-iconreference.md). Optional.                                   |
|                | [propertyStore Element (Library Schema)](schema-library-propertystore.md). Optional.                                   |
|                | [templateInfo Element (Library Schema)](schema-library-templateinfo.md). Optional.                                     |
|                | [searchConnectorDescriptionList Element (Library Schema)](schema-library-searchconnectordescriptionlist.md). Required. |



 

## Remarks

Each library can contain one or more locations that can be browsed or searched by a user using Windows Explorer. The locations are defined by search connectors using [&lt;searchConnectorDescription&gt;](schema-library-searchconnectordescription.md) elements in a [&lt;searchConnectorDescriptionList&gt;](schema-library-searchconnectordescriptionlist.md) container element.

A library can have a unique set of properties, and locations in the library can also have unique sets of properties. These properties are defined in [&lt;property&gt;](schema-library-property.md) elements within a [&lt;propertyStore&gt;](schema-library-propertystore.md) container element.

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
    <name>@shell32.dll,-34575</name>
    <ownerSID>S-1-5-21-379071477-2495173225-776587366-1000</ownerSID>
    <version>1</version>
    <isLibraryPinned>true</isLibraryPinned>
    <iconReference>imageres.dll,-1002</iconReference>
    <templateInfo>
        <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
    </templateInfo>
    <searchConnectorDescriptionList>
        <searchConnectorDescription publisher="Microsoft" product="Windows">
            <description>@shell32.dll,-34577</description>
            <isDefaultSaveLocation>true</isDefaultSaveLocation>
            <simpleLocation>
                <url>knownfolder:{FDD39AD0-238F-46AF-ADB4-6C85480369C7}</url>
                <serialized>MBAAAEAFCAAA...MFNVAAAAAA</serialized>
            </simpleLocation>
        </searchConnectorDescription>
        <searchConnectorDescription publisher="Microsoft" product="Windows">
            <description>@shell32.dll,-34579</description>
            <isDefaultNonOwnerSaveLocation>true</isDefaultNonOwnerSaveLocation>
            <simpleLocation>
                <url>knownfolder:{ED4824AF-DCE4-45A8-81E2-FC7965083634}</url>
                <serialized>MBAAAEAFCAAA...HJIfK9AAAAAA</serialized>
            </simpleLocation>
        </searchConnectorDescription>
    </searchConnectorDescriptionList>
</libraryDescription>
```



## Related topics

<dl> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> <dt>

[Search Connector Description Schema](../search/search-sconn-desc-schema-entry.md)
</dt> </dl>

 

 
