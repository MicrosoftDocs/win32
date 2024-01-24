---
title: runLevelType Simple Type
description: Defines the possible values for the RunLevel (principalType) element.
ms.assetid: d6b73dc5-97ac-4f94-99c1-c241a25cc252
keywords:
- runLevelType simple type Task Scheduler
topic_type:
- apiref
api_name:
- runLevelType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# runLevelType Simple Type

Defines the possible values for the [**RunLevel (principalType)**](taskschedulerschema-runlevel-principaltype-element.md) element.

``` syntax
<xs:simpleType name="runLevelType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="LeastPrivilege"
         />
        <xs:enumeration
            value="HighestAvailable"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **runLevelType** simple type defines the following values.



| Value            | Description                                               |
|------------------|-----------------------------------------------------------|
| LeastPrivilege   | Tasks are run with the least privileges (LUA).<br/> |
| HighestAvailable | Tasks are run with the highest privileges.<br/>     |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





