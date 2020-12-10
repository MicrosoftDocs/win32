---
title: IRDVTaskPlugin StartTask method
description: Called to start the update task on the virtual machine.
ms.assetid: c1e9f18b-1e83-4a29-8646-8adde94e8c14
ms.tgt_platform: multiple
keywords:
- StartTask method Remote Desktop Services
- StartTask method Remote Desktop Services , IRDVTaskPlugin interface
- IRDVTaskPlugin interface Remote Desktop Services , StartTask method
topic_type:
- apiref
api_name:
- IRDVTaskPlugin.StartTask
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPlugin::StartTask method

Called to start the update task on the virtual machine.

## Syntax


```C++
HRESULT StartTask(
  [in] BSTR            Label,
  [in] BSTR            Identifier,
  [in] SAFEARRAY(BYTE) *Context
);
```



## Parameters

<dl> <dt>

*Label* \[in\]
</dt> <dd>

The label for the task. This is the label that was passed to the trigger agent in the [**ScheduleTask**](irdvtaskpluginnotifysink-scheduletask.md) method.

</dd> <dt>

*Identifier* \[in\]
</dt> <dd>

The identifier of the task. This is the identifier that was passed to the trigger agent in the [**ScheduleTask**](irdvtaskpluginnotifysink-scheduletask.md) method.

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Optional data for the task. This is the data that was passed to the trigger agent in the [**ScheduleTask**](irdvtaskpluginnotifysink-scheduletask.md) method.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**IRDVTaskPlugin**](irdvtaskplugin.md)
</dt> </dl>

 

 





