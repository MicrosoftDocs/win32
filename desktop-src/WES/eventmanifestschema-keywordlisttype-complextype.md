---
title: KeywordListType Complex Type
description: Defines a list of keywords that categorize events. | KeywordListType Complex Type
ms.assetid: 7aeb5ca1-b23f-40f5-a77b-894deaf9c6bb
keywords:
- KeywordListType complex type EventLog
topic_type:
- apiref
api_name:
- KeywordListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# KeywordListType Complex Type

Defines a list of keywords that categorize events.

``` syntax
<xs:complexType name="KeywordListType">
    <xs:sequence>
        <xs:element name="keyword"
            type="KeywordType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                | Type                                                               | Description                                                                                                  |
|------------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**keyword**](eventmanifestschema-keyword-keywordlisttype-element.md) | [**KeywordType**](eventmanifestschema-keywordtype-complextype.md) | Defines a keyword that identifies a category of events. You can specify a maximum of 48 keywords.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





