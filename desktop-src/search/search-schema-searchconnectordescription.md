---
description: The &lt;searchConnectorDescriptionType&gt; element is the top level container for the search connector definition.
ms.assetid: a6b45864-210d-4099-804d-7548fd8eb562
title: searchConnectorDescriptionType Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# searchConnectorDescriptionType Element (Search Connector Schema)

The &lt;searchConnectorDescriptionType&gt; element is the top level container for the search connector definition.

-   [Syntax](#syntax)
-   [Element Information](#element-information)
-   [Attributes](#attributes)
-   [Remarks](#remarks)
-   [Example of a Search Connector Description File](#example-of-a-search-connector-description-file)
-   [Related topics](#related-topics)

## Syntax


```
<!-- searchConnectorDescriptionType -->
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



| Parent Element | Child Elements                                                                                                           |
|----------------|--------------------------------------------------------------------------------------------------------------------------|
|                | [isSearchOnlyItem Element (Search Connector Schema)](search-schema-sconn-issearchonlyitem.md)                           |
|                | [isDefaultSaveLocation Element (Search Connector Schema)](search-schema-sconn-isdefaultsavelocation.md)                 |
|                | [isDefaultNonOwnerSaveLocation Element (Search Connector Schema)](search-schema-sconn-isdefaultnonownersavelocation.md) |
|                | [description Element (Search Connector Schema)](search-schema-sconn-description.md)                                     |
|                | [iconReference Element (Search Connector Schema)](search-schema-sconn-iconreference.md)                                 |
|                | [imageLink Element (Search Connector Schema)](search-schema-sconn-imagelink.md)                                         |
|                | [author Element (Search Connector Schema)](search-schema-sconn-author.md)                                               |
|                | [dateCreated Element (Search Connector Schema)](search-schema-sconn-datecreated.md)                                     |
|                | [templateInfo Element (Search Connector Schema)](search-schema-sconn-templateinfo.md)                                   |
|                | [locationProvider Element (Search Connector Schema)](search-schema-sconn-locationprovider.md)                           |
|                | [scope Element (Search Connector Schema)](search-schema-sconn-scope.md)                                                 |
|                | [propertyStore Element (Search Connector Schema)](search-schema-sconn-propertystore.md)                                 |
|                | [includeInStartMenuScope Element (Search Connector Schema)](search-schema-sconn-includeinstartmenuscope.md)             |
|                | [domain Element (Search Connector Schema)](search-schema-sconn-domain.md)                                               |
|                | [supportsAdvancedQuerySyntax Element (Search Connector Schema)](search-schema-sconn-supportsadvancedquerysyntax.md)     |
|                | [isIndexed Element (Search Connector Schema)](search-schema-sconn-isindexed.md)                                         |



 

## Attributes



| Attribute | Description                                                                      |
|-----------|----------------------------------------------------------------------------------|
| publisher | Optional. The display name of the publisher providing the search connector.      |
| product   | Optional. The display name of the product to which the search connector applies. |



 

## Remarks

Search connectors for federated search cannot be used in libraries. The schema for library search connectors is an extension of the schema described here and includes information specific to libraries.

## Example of a Search Connector Description File

The following is an example of a Search Connector Description file for a federated search web service.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
  <description>Search MSDN. Powered by live.com</description>
  <isSearchOnlyItem>true</isSearchOnlyItem>
  <domain>https://social.msdn.microsoft.com</domain>
  <supportsAdvancedQuerySyntax>false</supportsAdvancedQuerySyntax>
  <templateInfo>
    <folderType>{8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}</folderType>
  </templateInfo>
  <propertyStore>
    <property name="OpenSearchHTMLRolloverTemplate">https://social.msdn.microsoft.com/Search/?Query={searchTerms}</property>
  </propertyStore>
  <locationProvider clsid="{48E277F6-4E74-4cd6-BA6F-FA4F42898223}">
    <propertyBag>
      <property name="OpenSearchShortName">MSDN</property>
      <property name="OpenSearchQueryTemplate">https://social.msdn.microsoft.com/Search/Feed.aspx?locale=en-US&Query={searchTerms}&format=RSS&StartIndex={startIndex}</property>
      <property name="MaximumResultCount" type="uint32">100</property>
    </propertyBag>
  </locationProvider>
</searchConnectorDescription>
```



The following is an example of a Search Connector Description file for a MAPI protocol handler.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    <description>Microsoft Outlook</description>
    <isSearchOnlyItem>true</isSearchOnlyItem>
    <includeInStartMenuScope>true</includeInStartMenuScope>
    <templateInfo>
        <folderType>{91475FE5-586B-4EBA-8D75-D17434B8CDF6}</folderType>
    </templateInfo>
    <simpleLocation>
        <url>mapi://{S-1-5-21-2127521184-1604012920-1887927527-2779359}/</url>
    </simpleLocation>
</searchConnectorDescription>
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Overview of the Search Connector Description Schema](search-sconn-desc-schema-entry.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> </dl>

 

 



