---
description: Defines the wireless network types.
ms.assetid: 03236db9-4f58-4fe3-82ff-d4b3a387490a
title: networkTypeType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- networkTypeType
api_type: 
- Schema
api_location: 
---

# networkTypeType Simple Type

The networkTypeType simple type defines the wireless network types. There are two types of networks: infrastructure networks (ESS) and ad-hoc networks (IBSS).

``` syntax
<xs:simpleType name="networkTypeType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="IBSS"
         />
        <xs:enumeration
            value="ESS"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **networkTypeType** simple type defines the following values.



| Value | Description |
|-------|-------------|
| IBSS  |             |
| ESS   |             |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




