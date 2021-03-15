---
title: HexInt32Type Simple Type (Event Schema)
description: Defines a 4-byte hexadecimal type. | HexInt32Type Simple Type (Event Schema)
ms.assetid: f4b5226d-2a5e-4756-b4c5-30cfbf13568e
keywords:
- HexInt32Type simple type EventLog
topic_type:
- apiref
api_name:
- HexInt32Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HexInt32Type Simple Type (Event Schema)

Defines a 4-byte hexadecimal type.

``` syntax
<xs:simpleType name="HexInt32Type">
    <xs:restriction
        base="string"
    >
        <xs:pattern
            value="0[xX][0-9A-Fa-f]{1,8}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **HexInt32Type** simple type is a **string** that is restricted by the following pattern:

-   `0[xX][0-9A-Fa-f]{1,8}`

    The value can contain from one to eight hexadecimal characters (for example, 0xa or 0xac7bd361).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





