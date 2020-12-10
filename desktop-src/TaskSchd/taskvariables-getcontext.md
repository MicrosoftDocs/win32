---
title: TaskVariables.GetContext method
description: For scripting, used to share the context between different steps and tasks that are in the same job instance.
ms.assetid: 'c3f1245c-531b-43f4-a3e4-8cb5deedd375'
keywords:
- GetContext method Task Scheduler
- GetContext method Task Scheduler , TaskVariables object
- TaskVariables object Task Scheduler , GetContext method
topic_type:
- apiref
api_name:
- TaskVariables.GetContext
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskVariables.GetContext method

For scripting, used to share the context between different steps and tasks that are in the same job instance. This method is not implemented.

## Syntax


```VB
TaskVariables.GetContext( _
  ByRef context _
)
```



## Parameters

<dl> <dt>

*context* \[out\]
</dt> <dd>

The context that is used to share the context between different steps and tasks that are in the same job instance.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskVariables**](taskvariables.md)
</dt> </dl>

 

 





