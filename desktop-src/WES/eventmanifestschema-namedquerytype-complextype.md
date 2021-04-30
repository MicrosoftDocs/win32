---
title: NamedQueryType Complex Type
description: Not used. Defines a list of named queries that query the event message string for a value and perform a specified action if found. | NamedQueryType Complex Type
ms.assetid: 2606094d-ae1b-4a3f-a78f-30659fa141ab
keywords:
- NamedQueryType complex type EventLog
topic_type:
- apiref
api_name:
- NamedQueryType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# NamedQueryType Complex Type

Not used. Defines a list of named queries that query the event message string for a value and perform a specified action if found.

``` syntax
<xs:complexType name="NamedQueryType">
    <xs:sequence
        minOccurs="0"
    >
        <xs:element name="patternMaps"
            type="PatternMapListType"
         />
        <xs:any
            processContents="lax"
            maxOccurs="unbounded"
            minOccurs="0"
            namespace="##other"
         />
    </xs:sequence>
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                       | Type                                                                             | Description                                                                                      |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**patternMaps**](eventmanifestschema-patternmaps-namedquerytype-element.md) | [**PatternMapListType**](eventmanifestschema-patternmaplisttype-complextype.md) | Defines a list of regular expression pairs that are used to alter the message string.<br/> |



## Examples

The following example shows how to use the [**namedQueries**](eventmanifestschema-namedqueries-metadatatype-element.md) element. This example takes the contents of the message string and inserts it into the string https://www.*messagestring*.com. It then replaces the message string with the result. For example, if the message string contained Microsoft, the query would replace the Microsoft message string with https://www.Microsoft.com.


```XML
<namedqueries>
   <patternmap name="SearchStrings" format="winrxv1">
       <map name="/${1}/" value="/http:\/\/www\.*\.com\/"/>
   </patternmap>
</namedqueries>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





