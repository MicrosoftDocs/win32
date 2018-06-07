---
title: TaskSettings.NetworkSettings property
description: For scripting, gets or sets the network settings object that contains a network profile identifier and name.
ms.assetid: 9ee4f2c0-90bf-4a28-9aeb-0c04f3a197aa
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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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



|                                     |                                                                                         |
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

 

 





