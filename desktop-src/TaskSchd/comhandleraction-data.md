---
title: ComHandlerAction.Data property
description: For scripting, gets or sets additional data that is associated with the handler.
ms.assetid: bf4d3e77-4b2b-4622-b26b-a8f7e9aa687b
keywords:
- Data property Task Scheduler
- Data property Task Scheduler , ComHandlerAction object
- ComHandlerAction object Task Scheduler , Data property
topic_type:
- apiref
api_name:
- ComHandlerAction.Data
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ComHandlerAction.Data property

For scripting, gets or sets additional data that is associated with the handler.

## Syntax


```VB
ComHandlerAction.Data As String
```



## Property value

The arguments that are needed by the handler.

## Remarks

When reading or writing XML, the data of a COM handler is specified in the [**Data**](taskschedulerschema-data-comhandlertype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**ComHandlerAction**](comhandleraction.md)
</dt> </dl>

 

 





