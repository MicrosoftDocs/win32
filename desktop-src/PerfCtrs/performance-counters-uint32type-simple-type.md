---
description: UInt32Type Simple Type (Performance Counters) - Defines an unsigned integer type.
ms.assetid: 48df484d-d663-42fa-aaec-51c463bb5350
title: UInt32Type Simple Type (Performance Counters)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# UInt32Type Simple Type (Performance Counters)

Defines an unsigned integer type.

``` syntax
<xs:simpleType name="UInt32Type">
    <xs:union
        memberValues="xs:unsignedInt man:HexInt32Type"
     />
</xs:simpleType>
```

## Remarks

You can specify the value as a 4-byte integer or hexadecimal value in the range from 0 through 4,294,967,295.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




