---
title: Command (execType) Element
description: Specifies the executable file or document to be run.
ms.assetid: dedf8627-926c-43c6-8add-21ff298d697a
keywords:
- Command element Task Scheduler
topic_type:
- apiref
api_name:
- Command
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Command (execType) Element

Specifies the executable file or document to be run.

``` syntax
<xs:element name="Command"
    type="pathType"
 />
```

The **Command** element is defined by the [**execType**](taskschedulerschema-exectype-complextype.md) complex type.

## Parent element



| Element                                                      | Derived from                                                 | Description                                                            |
|--------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------|
| [**Exec**](taskschedulerschema-exec-actiongroup-element.md) | [**execType**](taskschedulerschema-exectype-complextype.md) | Specifies an action that executes a command-line operation.<br/> |



## Remarks

For C++ development, see the [**Arguments property of IExecAction**](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_arguments).

For script development, see [**ExecAction.Arguments**](execaction-arguments.md).

## Examples

For a complete example of the XML for a task that uses an executable action, see [Time Trigger Example (XML)](time-trigger-example--xml-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





