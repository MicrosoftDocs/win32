---
title: StartService method of the Msvm\_VirtualSystemMigrationService class
description: Starts the virtual system migration service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d6ab5d20-20e1-43e4-a484-e9f6745e999b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartService method
- StartService method, Msvm_VirtualSystemMigrationService class
- Msvm_VirtualSystemMigrationService class, StartService method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.StartService
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StartService method of the Msvm\_VirtualSystemMigrationService class

Starts the virtual system migration service.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not supported** (1)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





