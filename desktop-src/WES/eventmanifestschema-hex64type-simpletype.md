---
title: HexInt64Type Simple Type
description: Defines an 8-byte hexadecimal type. | HexInt64Type Simple Type
ms.assetid: 2e81ec2b-cf67-42df-92a0-bf45b6dca051
keywords:
- HexInt64Type simple type EventLog
topic_type:
- apiref
api_name:
- HexInt64Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HexInt64Type Simple Type

Defines an 8-byte hexadecimal type.

``` syntax
<xs:simpleType name="HexInt64Type">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="0[xX][0-9A-Fa-f]{1,16}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **HexInt64Type** simple type is a [string](/dotnet/api/system.string) that is restricted by the following pattern:

-   `0[xX][0-9A-Fa-f]{1,16}`

    The value can contain from one to sixteen hexadecimal characters (for example, 0xa or 0xac7bd361004fe190).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

