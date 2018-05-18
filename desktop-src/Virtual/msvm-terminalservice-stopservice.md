---
title: StopService method of the Msvm\_TerminalService class
description: Stops the service.CIM\_Service.
ms.assetid: '12eb71b6-4ed6-4992-a0e0-80626409f6df'
keywords: ["StopService method Hyper-V", "StopService method Hyper-V , Msvm_TerminalService class", "Msvm_TerminalService class Hyper-V , StopService method"]
topic_type:
- apiref
api_name:
- Msvm_TerminalService.StopService
api_location:
- Root\virtualization
api_type:
- COM
---

# StopService method of the Msvm\_TerminalService class

Stops the service.

The [**StopService**](https://msdn.microsoft.com/library/aa393668) method stops the service represented by the object derived from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

## Syntax


```mof
uint32 StopService();
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

 

 





