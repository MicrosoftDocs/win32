---
title: ComHandler (actionGroup) Element
description: Specifies an action that fires a handler.
ms.assetid: 18f16873-3879-4a3b-b8f2-17cc84647e25
keywords:
- ComHandler element Task Scheduler
topic_type:
- apiref
api_name:
- ComHandler
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ComHandler (actionGroup) Element

Specifies an action that fires a handler.

``` syntax
<xs:element name="ComHandler"
    type="comHandlerType"
 />
```

The **ComHandler** element is defined by the [**actionGroup**](taskschedulerschema-actiongroup-group.md) .

## Parent element



| Element                                                         | Derived from                                                       | Description                                            |
|-----------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------|
| [**Actions**](taskschedulerschema-actions-tasktype-element.md) | [**actionsType**](taskschedulerschema-actionstype-complextype.md) | Contains the actions performed by the task.<br/> |



## Child elements



| Element                                                               | Type                                                         | Description                                                       |
|-----------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------|
| [**ClassId**](taskschedulerschema-classid-comhandlertype-element.md) | [**guidType**](taskschedulerschema-guidtype-simpletype.md)  | Specifies the identifier of the handler class.<br/>         |
| [**Data**](taskschedulerschema-data-comhandlertype-element.md)       | [**dataType**](taskschedulerschema-datatype-complextype.md) | Specifies additional data associated with the handler.<br/> |



## Remarks

Applications define a COM handler action using the [**IComHandlerAction**](/windows/desktop/api/taskschd/nn-taskschd-icomhandleraction) interface.

### Attributes

The following attribute is defined by the [**actionBaseType**](taskschedulerschema-actionbasetype-complextype.md) complex type.

-   ID: Identifier of the action performed by the task.

## Examples

The following XML defines a COM handler action.


```XML
<Actions>
    <ComHandler>
        <ClassId></ClassId>
        <Data></Data>
    </ComHandler>
</Actions>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





