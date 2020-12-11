---
title: Arguments (execType) Element
description: Specifies the arguments associated with the command-line operation.
ms.assetid: 37207c4f-941c-4cbf-9a81-5876b224a7c1
keywords:
- Arguments element Task Scheduler
topic_type:
- apiref
api_name:
- Arguments
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Arguments (execType) Element

Specifies the arguments associated with the command-line operation.

``` syntax
<xs:element name="Arguments"
    type="string"
 />
```

The **Arguments** element is defined by the [**execType**](taskschedulerschema-exectype-complextype.md) complex type.

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

 

 





