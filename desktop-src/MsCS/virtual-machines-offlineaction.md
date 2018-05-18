---
title: OfflineAction
description: Defines the operation that is performed on the Virtual Machine (VM) for an Offline call on the VM resource instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8b5de834-885c-4730-912c-69e027475a3b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["OfflineAction Failover Cluster ,for virtual machines", "OfflineAction Failover Cluster"]
topic_type:
- apiref
api_name:
- OfflineAction
api_type:
- NA
---

# OfflineAction

Defines the operation that is performed on the Virtual Machine (VM) for an [*Offline*](offline.md) call on the VM resource instance. The following table summarizes the attributes of the **OfflineAction** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 3                                         |
| Default   | 1                                         |



 

## Remarks

The following table summarizes the values for **OfflineAction**.



| Name                         | Value                  | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Turn Off<br/>          | 0<br/>           | The VM is turned off.<br/>                                                                                                                                                                                                                                                                                                                                                                        |
| Save<br/>              | 1 (Default)<br/> | The VM is saved.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| Shutdown<br/>          | 2<br/>           | The guest operating system running in the VM is shut down. This requires that the guest operating system has the shutdown integration component installed. For more information on the shutdown integration component see the [**Msvm\_ShutdownComponent**](https://msdn.microsoft.com/library/cc136893) and [**Msvm\_ShutdownComponentSettingData**](https://msdn.microsoft.com/library/cc136894) classes.<br/> |
| Shutdown (Forced)<br/> | 3<br/>           | The Windows guest operating system running in the VM is shut down forcibly. For more information see the **EWX\_FORCE** option flag on the [**ExitWindowsEx**](https://msdn.microsoft.com/library/windows/desktop/aa376868) function page. This requires that the guest operating system has the shutdown integration component installed.<br/>                                                                                            |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for [**ShareFlags**](distributed-file-system-shareflags.md) can be set with the following example code.


```C++
DWORD          OfflineActionData = 2;
CLUSPROP_DWORD OfflineActionValue;

OfflineActionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
OfflineActionValue.cbLength  = sizeof(DWORD);
OfflineActionValue.dw        = OfflineActionData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> </dl>

 

 





