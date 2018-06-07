---
Description: This &lt;searchConnectorDescriptionList&gt; element contains a list of search connectors that map to locations included in this library. Each search connector is defined by a &lt;searchConnectorDescription&gt; element. This element is optional and has no attributes.
ms.assetid: 58A7BC21-0EB8-4bcf-98EE-31A56A4BC58C
title: searchConnectorDescriptionList Element (Library Schema)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# searchConnectorDescriptionList Element (Library Schema)

This &lt;searchConnectorDescriptionList&gt; element contains a list of search connectors that map to locations included in this library. Each search connector is defined by a &lt;searchConnectorDescription&gt; element. This element is optional and has no attributes.

## Syntax

``` syntax
<!-- searchConnectorDescriptionList -->
    <xs:element name="searchConnectorDescriptionList" minOccurs="0">
          <xs:complexType>
            <xs:sequence minOccurs="0">
              <xs:element name="searchConnectorDescription" type="searchConnectorDescriptionType" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
```

## Element Information



| Parent Element                                                               | Child Elements                                                                                       |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [libraryDescription Element (Library Schema)](schema-librarydescription.md) | [searchConnectorDescription Element (Library Schema)](schema-library-searchconnectordescription.md) |



 

## Remarks

Search connectors for Windows Federated Search and protocol handler scopes cannot be included in a library.

## Related topics

<dl> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> <dt>

[Search Connector Description Schema](b85a04c6-9398-4cc7-a894-881216600203)
</dt> </dl>

 

 



