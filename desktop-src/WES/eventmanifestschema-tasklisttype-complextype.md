---
title: TaskListType Complex Type
description: Defines a list of tasks that are used to identify the components of an application.
ms.assetid: 41a46967-7c5b-4555-9f65-bd9582c0c492
keywords:
- TaskListType complex type EventLog
topic_type:
- apiref
api_name:
- TaskListType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TaskListType Complex Type

Defines a list of tasks that are used to identify the components of an application.

``` syntax
<xs:complexType name="TaskListType">
    <xs:sequence>
        <xs:element name="task"
            type="TaskType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                       | Type                                                         | Description                                                       |
|---------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------|
| [**task**](eventmanifestschema-task-tasklisttype-element.md) | [**TaskType**](eventmanifestschema-tasktype-complextype.md) | Defines a component or subcomponent of an application.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





