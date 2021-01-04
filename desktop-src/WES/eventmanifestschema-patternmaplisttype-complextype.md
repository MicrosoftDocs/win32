---
title: PatternMapListType Complex Type
description: Not used. Defines a list of regular expression pairs that are used to alter the message string.
ms.assetid: f7b92821-a959-4b91-9e7e-47d0136ee61f
keywords:
- PatternMapListType complex type EventLog
topic_type:
- apiref
api_name:
- PatternMapListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PatternMapListType Complex Type

Not used. Defines a list of regular expression pairs that are used to alter the message string.

``` syntax
<xs:complexType name="PatternMapListType">
    <xs:sequence>
        <xs:element name="patternMap"
            type="PatternMapType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                         | Type                                                                     | Description                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**patternMap**](eventmanifestschema-patternmap-patternmaplisttype-element.md) | [**PatternMapType**](eventmanifestschema-patternmaptype-complextype.md) | Defines a mapping between two regular expressions. One expression is used to find a matching string in the message string and the other is used to alter the string before the service places it back in the message string. The first pattern mapping that matches is used and other patterns are not tried.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





