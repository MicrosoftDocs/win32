---
title: GUIDType simple type (Event Schema)
description: Defines a globally unique identifier type, in Registry format. | GUIDType simple type (Event Schema)
ms.assetid: dbc305ef-6f07-4a70-9013-b89ccec889ea
keywords:
- GUIDType simple type EventLog
topic_type:
- apiref
api_name:
- GUIDType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GUIDType simple type (Event Schema)

Defines a globally unique identifier type, in Registry format.

``` syntax
<xs:simpleType name="GUIDType">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **GUIDType** simple type is a string that is restricted by the following pattern:

-   `\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}`

    The value must be a globally unique identifier type in Registry format. For example, {5b2fc63a-8af4-44cb-960c-aefdced908d6}. Use GUIDGen.exe or UUIDGen.exe to create a GUID.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





