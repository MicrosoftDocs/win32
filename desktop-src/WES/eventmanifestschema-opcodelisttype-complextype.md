---
title: OpcodeListType Complex Type
description: Defines a list of opcodes that are used to identify the operations of a component of the application.
ms.assetid: 0cbca036-b32e-4fc4-96ee-1dd5bee019bf
keywords:
- OpcodeListType complex type EventLog
topic_type:
- apiref
api_name:
- OpcodeListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# OpcodeListType Complex Type

Defines a list of opcodes that are used to identify the operations of a component of the application.

``` syntax
<xs:complexType name="OpcodeListType">
    <xs:sequence>
        <xs:element name="opcode"
            type="OpcodeType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                             | Type                                                             | Description                                                            |
|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| [**opcode**](eventmanifestschema-opcode-opcodelisttype-element.md) | [**OpcodeType**](eventmanifestschema-opcodetype-complextype.md) | Defines an operation within a component of the application.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





