---
title: TaskSettings.NetworkSettings property
description: For scripting, gets or sets the network settings object that contains a network profile identifier and name.
ms.assetid: '3d368f6c-4534-4e71-8fbd-84361730a3e2'
keywords:
- NetworkSettings property Task Scheduler
- NetworkSettings property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , NetworkSettings property
topic_type:
- apiref
api_name:
- TaskSettings.NetworkSettings
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.NetworkSettings property

For scripting, gets or sets the network settings object that contains a network profile identifier and name. If the [**RunOnlyIfNetworkAvailable**](tasksettings-runonlyifnetworkavailable.md) property of [**TaskSettings**](tasksettings.md) is **True** and a network propfile is specified in the **NetworkSettings** property, then the task will run only if the specified network profile is available.

## Syntax


```VB
TaskSettings.NetworkSettings As NetworkSettings
```



## Property value

A [**NetworkSettings**](networksettings.md) object that contains a network profile identifier and name.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskSettings**](tasksettings.md)
</dt> <dt>

[**NetworkSettings**](networksettings.md)
</dt> </dl>

 

 





