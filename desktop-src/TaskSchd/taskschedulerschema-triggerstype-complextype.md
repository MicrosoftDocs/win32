---
title: triggersType Complex Type
description: Defines the group (triggerGroup) for all trigger elements.
ms.assetid: ceabc332-e028-491e-8fd8-c02ac23a2635
keywords:
- triggersType complex type Task Scheduler
topic_type:
- apiref
api_name:
- triggersType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# triggersType Complex Type

Defines the group ([**triggerGroup**](taskschedulerschema-triggergroup-group.md)) for all trigger elements. The [**triggerGroup**](taskschedulerschema-triggergroup-group.md) group contains the list of triggers that can be used in a task.

``` syntax
<xs:complexType name="triggersType">
    <xs:group
        minOccurs="0"
        maxOccurs="48"
        ref="triggerGroup"
     />
</xs:complexType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





