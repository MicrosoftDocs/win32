---
title: XmlType Complex Type
description: Defines an XML fragment.
ms.assetid: ac6ce2a2-4584-4181-9a39-aceab85d5c51
keywords:
- XmlType complex type EventLog
topic_type:
- apiref
api_name:
- XmlType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# XmlType Complex Type

Defines an XML fragment. Any schema instance is allowed; the top-level node in the fragment must contain a namespace attribute.

``` syntax
<xs:complexType name="XmlType">
    <xs:sequence>
        <xs:any
            processContents="skip"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##other"
         />
    </xs:sequence>
</xs:complexType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





