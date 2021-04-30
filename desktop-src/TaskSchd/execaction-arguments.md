---
title: ExecAction.Arguments property
description: For scripting, gets or sets the arguments associated with the command-line operation.
ms.assetid: 911e720f-ea7b-474d-ac75-4cd4f9adee55
keywords:
- Arguments property Task Scheduler
- Arguments property Task Scheduler , ExecAction object
- ExecAction object Task Scheduler , Arguments property
topic_type:
- apiref
api_name:
- ExecAction.Arguments
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExecAction.Arguments property

For scripting, gets or sets the arguments associated with the command-line operation.

## Syntax


```VB
ExecAction.Arguments As String
```



## Property value

The arguments that are needed by the command-line operation.

## Remarks

When reading or writing XML, the command-line operation arguments are specified in the [**Arguments**](taskschedulerschema-arguments-exectype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExecAction**](execaction.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





