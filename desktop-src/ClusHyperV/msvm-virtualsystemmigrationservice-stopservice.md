---
title: StopService method of the Msvm\_VirtualSystemMigrationService class
description: Stops the virtual system migration service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '59a999a7-22da-4dfc-95af-128fca8e3af2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StopService method", "StopService method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, StopService method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.StopService
api_location:
- VMMS.exe
api_type:
- COM
---

# StopService method of the Msvm\_VirtualSystemMigrationService class

Stops the virtual system migration service.

## Syntax


```mof
uint32 StopService();
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





