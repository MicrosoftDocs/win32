---
description: The &lt;searchConnectorDescription&gt; element is the top level container element of a search connector definition.
ms.assetid: 383CAA20-56CA-4bdc-AC79-E57A1D59785C
title: searchConnectorDescription Element (Library Schema)
ms.topic: article
ms.date: 05/31/2018
---

# searchConnectorDescription Element (Library Schema)

The &lt;searchConnectorDescription&gt; element is the top level container element of a search connector definition. The &lt;searchConnectorDescription&gt; element is an extension of the &lt;searchConnectorDescriptionType&gt; element type associated with Windows Federated Search connectors; however, you cannot include search connectors for Windows Federated Search or protocol handlers in a library.

## Syntax

``` syntax
<!-- searchConnectorDescription -->
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
   <xs:complexType name="searchConnectorDescriptionType">
      <xs:all>
         <xs:element name="isSearchOnlyItem" type="xs:boolean" default="false" minOccurs="0"/>
         <xs:element name="isDefaultSaveLocation" type="xs:boolean" minOccurs="0"/>
         <xs:element name="isDefaultNonOwnerSaveLocation" type="xs:boolean" minOccurs="0"/
         <xs:element name="description" type="xs:string" minOccurs="0"/>
         <xs:element name="iconReference" type="xs:string" minOccurs="0"/>
         <xs:element name="imageLink" minOccurs="0">
            <xs:complexType>
               <xs:sequence>
                  <xs:element name="url" type="xs:anyURI"/>
               </xs:sequence>
            </xs:complexType>
         </xs:element>
         <xs:element name="author" type="xs:string" minOccurs="0"/>
         <xs:element name="dateCreated" type="xs:dateTime" minOccurs="0"/>
         <xs:element name="templateInfo" minOccurs="0">
            <xs:complexType>
               <xs:all>
                  <xs:element name="folderType" minOccurs="0"/>
               </xs:all>
            </xs:complexType>
         </xs:element>
         <xs:element name="simpleLocation" type="shellLinkType" minOccurs="0"/>
         <xs:element name="locationProvider" minOccurs="0">
            <xs:complexType>
               <xs:all>
                  <xs:element name="propertyBag" type="propertyStoreType" minOccurs="0"/>
               </xs:all>
               <xs:attribute name="clsid" use="required"/>
               <xs:attribute name="codebase" type="xs:string"/>
            </xs:complexType>
         </xs:element>
         <xs:element name="scope" minOccurs="0">
            <xs:complexType>
               <xs:sequence minOccurs="0">
                  <xs:element name="scopeItem" maxOccurs="unbounded">
                     <xs:complexType>
                        <xs:all>
                           <xs:element name="mode" default="Include">
                              <xs:simpleType>
                                 <xs:restriction base="xs:string">
                                    <xs:enumeration value="Include"/>
                                    <xs:enumeration value="Exclude"/>
                                 </xs:restriction>
                              </xs:simpleType>
                           </xs:element>
                           <xs:element name="depth" default="Shallow" minOccurs="0">
                              <xs:simpleType>
                                 <xs:restriction base="xs:string">
                                    <xs:enumeration value="Shallow"/>
                                    <xs:enumeration value="Deep"/>
                                 </xs:restriction>
                              </xs:simpleType>
                           </xs:element>
                           <xs:element name="url" type="xs:anyURI"/>
                        </xs:all>
                     </xs:complexType>
                  </xs:element>
               </xs:sequence>
            </xs:complexType>
         </xs:element>
         <xs:element name="propertyStore" type="propertyStoreType" minOccurs="0"/>
         <xs:element name="includeInStartMenuScope" type="xs:boolean" default="false" minOccurs="0"/>
         <xs:element name="domain" type="xs:string" minOccurs="0"/>
         <xs:element name="supportsAdvancedQuerySyntax" type="xs:boolean" default="false" minOccurs="0"/>
         <xs:element name="isIndexed" type="xs:boolean" minOccurs="0"/>
      </xs:all>
      <xs:attribute name="publisher" type="xs:string"/>
      <xs:attribute name="product" type="xs:string"/>
   </xs:complexType>
</xs:schema>
```

## Element Information

Refer to the schema documentation in [Windows Search](/previous-versions/bb268030(v=msdn.10))



| Parent Element                                                                                               | Child Elements                        |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------|
| [searchConnectorDescriptionList Element (Library Schema)](schema-library-searchconnectordescriptionlist.md) | <isSearchOnlyI.tem>             |
|                                                                                                              | &lt;description&gt;                   |
|                                                                                                              | &lt;iconReference&gt;                 |
|                                                                                                              | &lt;imageLink&gt;                     |
|                                                                                                              | &lt;author&gt;                        |
|                                                                                                              | &lt;dateCreated&gt;                   |
|                                                                                                              | &lt;templateInfo&gt;                  |
|                                                                                                              | &lt;locationProvider&gt;              |
|                                                                                                              | &lt;scope&gt;                         |
|                                                                                                              | &lt;propertyStore&gt;                 |
|                                                                                                              | &lt;domain&gt;                        |
|                                                                                                              | &lt;supportsAdvancedQuerySyntax&gt;   |
|                                                                                                              | &lt;isDefaultSaveLocation&gt;         |
|                                                                                                              | &lt;isDefaultNonOwnerSaveLocation&gt; |
|                                                                                                              | &lt;isIndexed&gt;                     |
|                                                                                                              | &lt;simpleLocation&gt;                |
|                                                                                                              | &lt;includeInStartMenu&gt;            |



 

## Attributes



| Attribute | Description                                                                      |
|-----------|----------------------------------------------------------------------------------|
| publisher | Optional. The display name of the publisher providing the search connector.      |
| product   | Optional. The display name of the product to which the search connector applies. |



 

## Remarks

The &lt;searchConnectorDescription&gt; element of a library uses the same schema definition as the &lt;searchConnectorDescription&gt; for Windows Federated Search. Although they use the same schemas, search connectors for Windows Federated search cannot be included in a library.

## Related topics

<dl> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> <dt>

[Search Connector Description Schema](../search/search-sconn-desc-schema-entry.md)
</dt> </dl>

 

 
