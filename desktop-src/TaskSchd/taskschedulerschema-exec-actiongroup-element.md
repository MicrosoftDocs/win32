---
title: Exec (actionGroup) Element
description: Specifies an action that executes a command-line operation.
ms.assetid: 84bdd1ec-4279-4282-b44a-4b5ad30503eb
keywords:
- Exec element Task Scheduler
topic_type:
- apiref
api_name:
- Exec
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Exec (actionGroup) Element

Specifies an action that executes a command-line operation.

``` syntax
<xs:element name="Exec"
    type="execType"
 />
```

The **Exec** element is defined by the [**actionGroup**](taskschedulerschema-actiongroup-group.md) .

## Parent element



| Element                                                         | Derived from                                                       | Description                                            |
|-----------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------|
| [**Actions**](taskschedulerschema-actions-tasktype-element.md) | [**actionsType**](taskschedulerschema-actionstype-complextype.md) | Contains the actions performed by the task.<br/> |



## Child elements



| Element                                                                           | Type       | Description                                                                                                  |
|-----------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------|
| [**Arguments**](taskschedulerschema-arguments-exectype-element.md)               | **string** | Specifies the arguments associated with the command-line operation.<br/>                               |
| [**Command**](taskschedulerschema-command-exectype-element.md)                   | **string** | Specifies the executable file or document to be run.<br/>                                              |
| [**WorkingDirectory**](taskschedulerschema-workingdirectory-exectype-element.md) | string     | Specifies the directory where either the executable or those files used by the executable exists.<br/> |



## Attributes



| Name | Type       | Description                                                    |
|------|------------|----------------------------------------------------------------|
| id   | **string** | The identifier of the action performed by the task.<br/> |



## Remarks

The child elements listed above are defined by the [**execType**](taskschedulerschema-exectype-complextype.md) complex type.

For script development, an execution action is defined by the [**ExecAction**](execaction.md) object.

For C++ development, an execution action is defined by the [**IExecAction**](/windows/desktop/api/taskschd/nn-taskschd-iexecaction) interface.

If environment variables are used in the [**Command**](taskschedulerschema-command-exectype-element.md), [**Arguments**](taskschedulerschema-arguments-exectype-element.md), or [**WorkingDirectory**](taskschedulerschema-workingdirectory-exectype-element.md) elements, then the values of the environment variables are cached and used when the Taskeng.exe (the task engine) is launched. Changes to the environment variables that occur after the task engine is launched will not be used by the task engine.

## Examples

For a complete example of the XML for a task that uses an event trigger, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





