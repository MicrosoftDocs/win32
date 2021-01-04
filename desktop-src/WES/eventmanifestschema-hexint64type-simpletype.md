---
title: UInt64Type Simple Type (EventManifest Schema)
description: Defines an unsigned long type.
ms.assetid: 6f69dbde-8292-4f8e-bf49-3ef41ea7315e
keywords:
- UInt64Type simple type EventLog
topic_type:
- apiref
api_name:
- UInt64Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# UInt64Type Simple Type

Defines an unsigned long type. The value can be specified as an 8-byte integer or hexadecimal value in the range from 0 through 18,446,744,073,709,551,615.

``` syntax
<xs:simpleType name="UInt64Type">
    <xs:union
        memberValues="unsignedLong HexInt64Type"
     />
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





