---
title: namedValues Complex Type
description: Defines a name-value pair in which the name is associated with the value.
ms.assetid: 07c512fd-3eab-4238-8d75-83827a958a1e
keywords:
- namedValues complex type Task Scheduler
topic_type:
- apiref
api_name:
- namedValues
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# namedValues Complex Type

Defines a name-value pair in which the name is associated with the value.

``` syntax
<xs:complexType name="namedValues">
    <xs:sequence>
        <xs:element name="Value"
            type="namedValue"
            minOccurs="1"
            maxOccurs="32"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                        | Type                                                | Description                                                                         |
|----------------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------|
| [**Value**](taskschedulerschema-value-namedvalues-element.md) | [**namedValue**](schema-namedvalue-complextype.md) | Specifies the value that is associated with a name in a name-value pair.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





