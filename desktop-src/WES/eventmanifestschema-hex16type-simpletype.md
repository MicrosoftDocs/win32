---
title: HexInt16Type Simple Type
description: Defines a 2-byte hexadecimal type.
ms.assetid: d33d24e7-d260-49ea-a8ba-187b9b7a3a9c
keywords:
- HexInt16Type simple type EventLog
topic_type:
- apiref
api_name:
- HexInt16Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HexInt16Type Simple Type

Defines a 2-byte hexadecimal type.

``` syntax
<xs:simpleType name="HexInt16Type">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="0[xX][0-9A-Fa-f]{1,4}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **HexInt16Type** simple type is a **string** that is restricted by the following pattern:

-   `0[xX][0-9A-Fa-f]{1,4}`

    The value can contain from one to four hexadecimal characters (for example, 0xa or 0xac7b).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





