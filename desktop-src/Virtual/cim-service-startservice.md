---
title: StartService method of the CIM\_Service class
description: Starts the service.
ms.assetid: 226f63a1-f32b-481e-8493-dee1721e4e86
keywords:
- StartService method Hyper-V
- StartService method Hyper-V , CIM_Service class
- CIM_Service class Hyper-V , StartService method
topic_type:
- apiref
api_name:
- CIM_Service.StartService
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

# StartService method of the CIM\_Service class

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
</dt> </dl>

 

 





