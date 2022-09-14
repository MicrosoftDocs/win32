---
title: HexInt8Type Simple Type
description: Defines a 1-byte hexadecimal type.
ms.assetid: 390acf84-7b5c-45e7-83bd-9f3115099568
keywords:
- HexInt8Type simple type EventLog
topic_type:
- apiref
api_name:
- HexInt8Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HexInt8Type Simple Type

Defines a 1-byte hexadecimal type.

``` syntax
<xs:simpleType name="HexInt8Type">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="0[xX][0-9A-Fa-f]{1,2}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **HexInt8Type** simple type is a [string](/dotnet/api/system.string) that is restricted by the following pattern:

-   `0[xX][0-9A-Fa-f]{1,2}`

    The value can contain from one to two hexadecimal characters (for example, 0xa or 0xac).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

