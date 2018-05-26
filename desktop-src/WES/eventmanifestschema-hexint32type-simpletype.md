---
title: UInt32Type Simple Type
description: Defines an unsigned integer type.
ms.assetid: 11e99c26-3be7-4fac-b3e1-97cb0428a886
keywords:
- UInt32Type simple type EventLog
topic_type:
- apiref
api_name:
- UInt32Type
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UInt32Type Simple Type

Defines an unsigned integer type. The value can be specified as a 4-byte integer or hexadecimal value in the range from 0 through 4,294,967,295.

``` syntax
<xs:simpleType name="UInt32Type">
    <xs:union
        memberValues="unsignedInt HexInt32Type"
     />
</xs:simpleType>
```

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





