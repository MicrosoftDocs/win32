---
title: TaskNamedValuePair object
description: Scripting object that is used to create a name-value pair in which the name is associated with the value.
ms.assetid: b9d186a3-017d-409e-9d67-e74dc69a486a
keywords:
- TaskNamedValuePair object Task Scheduler
- TaskNamedValuePair object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskNamedValuePair
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TaskNamedValuePair object

Scripting object that is used to create a name-value pair in which the name is associated with the value.

## Members

The **TaskNamedValuePair** object has these types of members:

-   [Properties](#properties)

### Properties

The **TaskNamedValuePair** object has these properties.



| Property                                             | Description                                                                            |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**Name**](tasknamedvaluepair-name.md)<br/>   | Gets or sets the name that is associated with a value in a name-value pair.<br/> |
| [**Value**](tasknamedvaluepair-value.md)<br/> | Gets or sets the value that is associated with a name in a name-value pair.<br/> |



 

## Remarks

When reading or writing your own XML for a task, a name-value pair is specified using the [**ValueQueries**](taskschedulerschema-valuequeries-eventtriggertype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskNamedValueCollection**](tasknamedvaluecollection.md)
</dt> </dl>

 

 





