---
description: The &lt;folderType&gt; element specifies GUID for the folder type. This element is required if the &lt;templateInfo&gt; element exists. It has no attributes and no child elements.
ms.assetid: 2361bbf5-adeb-4189-a8ff-5fdd1c9b0ec6
title: folderType Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# folderType Element (Search Connector Schema)

The &lt;folderType&gt; element specifies GUID for the folder type. This element is required if the &lt;templateInfo&gt; element exists. It has no attributes and no child elements.

## Syntax


```
<!-- folderType -->
    <xs:element name="templateInfo" minOccurs="0">
      <xs:complexType>
        <xs:all>
          <xs:element name="folderType" minOccurs="0"/>
        </xs:all>
      </xs:complexType>
    </xs:element>
```



## Element Information



| Parent Element                                                                         | Child Elements |
|----------------------------------------------------------------------------------------|----------------|
| [templateInfo Element (Search Connector Schema)](search-schema-sconn-templateinfo.md) |                |



 

## Remarks

The default GUID is {8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}, a general folder type for federated search (OpenSearch) connectors.

## Example of a folderType Element


```
<!-- templateInfo and folderType -->
<templateInfo>
    <folderType>{8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}</folderType>
</templateInfo
```



 

 



