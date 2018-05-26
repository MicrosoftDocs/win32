---
title: StartService method of the Msvm\_ImageManagementService class
description: Starts the service.
ms.assetid: 6521738d-3b06-4fda-8d81-5fa0408722ea
keywords:
- StartService method Hyper-V
- StartService method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , StartService method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.StartService
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StartService method of the Msvm\_ImageManagementService class

Starts the service.

The [**StartService**](https://msdn.microsoft.com/library/aa393655) method puts the service in a started state.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





