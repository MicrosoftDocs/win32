---
description: Defines a globally unique identifier type, in Registry format.
ms.assetid: 2be73c57-b6b6-46ab-93e1-d70f8655c30e
title: GUIDType Simple Type (Performance Counters)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# GUIDType Simple Type (Performance Counters)

Defines a globally unique identifier type, in Registry format.

``` syntax
<xs:simpleType name="GUIDType">
    <xs:restriction
        base="xs:string"
    >
        <xs:pattern
            value="\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **GUIDType** simple type is a **xs:string** that is restricted by the following pattern:

-   `\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}`

    The value must be a globally unique identifier type in Registry format. For example, {5b2fc63a-8af4-44cb-960c-aefdced908d6}. Use GUIDGen.exe or UUIDGen.exe to create a GUID.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




