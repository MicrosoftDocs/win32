---
title: InputTypeListType Complex Type
description: Defines a list of input types.
ms.assetid: e6bba894-7c17-411e-92e5-9276728a5e4b
keywords:
- InputTypeListType complex type EventLog
topic_type:
- apiref
api_name:
- InputTypeListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InputTypeListType Complex Type

Defines a list of input types.

``` syntax
<xs:complexType name="InputTypeListType">
    <xs:sequence>
        <xs:element name="inType"
            type="InputType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                | Type                                                           | Description                       |
|------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------|
| [**inType**](eventmanifestschema-intype-inputtypelisttype-element.md) | [**InputType**](eventmanifestschema-inputtype-complextype.md) | Defines an input type.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





