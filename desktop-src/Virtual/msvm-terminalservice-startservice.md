---
title: StartService method of the Msvm\_TerminalService class
description: Starts the service.
ms.assetid: 9187f463-79d8-43e3-8bfa-b70990f3cec0
keywords:
- StartService method Hyper-V
- StartService method Hyper-V , Msvm_TerminalService class
- Msvm_TerminalService class Hyper-V , StartService method
topic_type:
- apiref
api_name:
- Msvm_TerminalService.StartService
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartService method of the Msvm\_TerminalService class

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

[**Msvm\_TerminalService**](msvm-terminalservice.md)
</dt> </dl>

 

 





