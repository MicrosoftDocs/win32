---
title: ClassId (comHandlerType) Element
description: Specifies the identifier of the handler class.
ms.assetid: 38ebcc39-85f2-4f61-8cb6-556c242a63d9
keywords:
- ClassId element Task Scheduler
topic_type:
- apiref
api_name:
- ClassId
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ClassId (comHandlerType) Element

Specifies the identifier of the handler class.

``` syntax
<xs:element name="ClassId"
    type="guidType"
 />
```

The **ClassId** element is defined by the [**comHandlerType**](taskschedulerschema-comhandlertype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                             | Description                                          |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------|
| [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md) | [**comHandlerType**](taskschedulerschema-comhandlertype-complextype.md) | Specifies an action that fires a handler.<br/> |



## Remarks

Applications define the class identifier using the [**ClassId**](/windows/win32/taskschd/nf-taskschd-icomhandleraction-get_classid?branch=master) property of the [**IComHandlerAction**](/windows/win32/taskschd/nn-taskschd-icomhandleraction?branch=master) interface.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

 





