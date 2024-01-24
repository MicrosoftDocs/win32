---
title: taskType Complex Type (Task Scheduler)
description: Defines the child elements and sequencing information for the Task element.
ms.assetid: 622b2bf4-c7e0-403c-bd6c-99b687c1d439
keywords:
- taskType complex type Task Scheduler
topic_type:
- apiref
api_name:
- taskType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# taskType Complex Type

Defines the child elements and sequencing information for the [**Task**](taskschedulerschema-task-element.md) element.

``` syntax
<xs:complexType name="taskType">
    <xs:all>
        <xs:element name="RegistrationInfo"
            type="registrationInfoType"
            minOccurs="0"
         />
        <xs:element name="Triggers"
            type="triggersType"
            minOccurs="0"
         />
        <xs:element name="Settings"
            type="settingsType"
            minOccurs="0"
         />
        <xs:element name="Data"
            type="dataType"
            minOccurs="0"
         />
        <xs:element name="Principals"
            type="principalsType"
            minOccurs="0"
         />
        <xs:element name="Actions"
            type="actionsType"
         />
    </xs:all>
    <xs:attribute name="version"
        type="versionType"
        use="optional"
        fixed="1.3"
     />
</xs:complexType>
```

## Child elements



| Element                                                                           | Type                                                                                 | Description                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**Actions**](taskschedulerschema-actions-tasktype-element.md)                   | [**actionsType**](taskschedulerschema-actionstype-complextype.md)                   | Specifies the actions performed by the task.<br/>                                                                             |
| [**Data**](taskschedulerschema-data-tasktype-element.md)                         | [**dataType**](taskschedulerschema-datatype-complextype.md)                         | Specifies addition data that is associated with the task, but is otherwise unused by the Task Scheduler service.<br/>         |
| [**Principals**](taskschedulerschema-principals-tasktype-element.md)             | [**principalsType**](taskschedulerschema-principalstype-complextype.md)             | Specifies the security contexts that can be used to run the task.<br/>                                                        |
| [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) | [**registrationInfoType**](taskschedulerschema-registrationinfotype-complextype.md) | Specifies administrative information about the task, such as the author of the task and the date the task is registered.<br/> |
| [**Settings**](taskschedulerschema-settings-tasktype-element.md)                 | [**settingsType**](taskschedulerschema-settingstype-complextype.md)                 | Specifies the settings that the Task Scheduler uses to perform the task.<br/>                                                 |
| [**Triggers**](taskschedulerschema-triggers-tasktype-element.md)                 | [**triggersType**](taskschedulerschema-triggerstype-complextype.md)                 | Specifies the triggers that start the task.<br/>                                                                              |



## Attributes



| Name    | Type                                                              | Description                                   |
|---------|-------------------------------------------------------------------|-----------------------------------------------|
| version | [**versionType**](taskschedulerschema-versiontype-simpletype.md) | Specifies the version of the task.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





