---
description: Defines a 4-byte hexadecimal type.
ms.assetid: d0e538c1-f22e-4905-ba73-b670fa7eb174
title: HexInt32Type Simple Type (Performance Counters)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# HexInt32Type Simple Type (Performance Counters)

Defines a 4-byte hexadecimal type.

``` syntax
<xs:simpleType name="HexInt32Type">
    <xs:restriction
        base="xs:string"
    >
        <xs:pattern
            value="0[xX][0-9A-Fa-f]{1,8}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **HexInt32Type** simple type is a **xs:string** that is restricted by the following pattern:

-   `0[xX][0-9A-Fa-f]{1,8}`

    The value can contain from one to eight hexadecimal characters (for example, 0xa or 0xac7bd361).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




