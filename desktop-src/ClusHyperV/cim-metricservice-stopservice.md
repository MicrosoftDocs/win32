---
title: StopService method of the CIM\_MetricService class
description: Stops the service.CIM\_Service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b79da5e2-fbb6-432d-910f-7b59ae0e7853
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StopService method
- StopService method, CIM_MetricService class
- CIM_MetricService class, StopService method
topic_type:
- apiref
api_name:
- CIM_MetricService.StopService
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StopService method of the CIM\_MetricService class

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>                    |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_MetricService**](cim-metricservice.md)
</dt> </dl>

 

 





