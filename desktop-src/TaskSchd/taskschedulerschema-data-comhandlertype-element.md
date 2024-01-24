---
title: Data (comHandlerType) Element
description: Specifies additional data associated with the handler.
ms.assetid: 352cb92b-54bb-4bb0-8a43-123c88c80962
keywords:
- Data element Task Scheduler
topic_type:
- apiref
api_name:
- Data
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Data (comHandlerType) Element

Specifies additional data associated with the handler.

``` syntax
<xs:element name="Data"
    type="dataType"
 />
```

The **Data** element is defined by the [**comHandlerType**](taskschedulerschema-comhandlertype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                             | Description                                          |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------|
| [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md) | [**comHandlerType**](taskschedulerschema-comhandlertype-complextype.md) | Specifies an action that fires a handler.<br/> |



## Remarks

Applications define the handler data using the [**Data**](/windows/desktop/api/taskschd/nf-taskschd-icomhandleraction-get_data) property of the [**IComHandlerAction**](/windows/desktop/api/taskschd/nn-taskschd-icomhandleraction) interface.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





