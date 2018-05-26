---
title: SaveProperties method of the CIM\_IDEController class
description: Saves the configuration and state of the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aca41c05-78c6-4381-89c1-4ee5572edd7c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SaveProperties method
- SaveProperties method, CIM_IDEController class
- CIM_IDEController class, SaveProperties method
topic_type:
- apiref
api_name:
- CIM_IDEController.SaveProperties
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SaveProperties method of the CIM\_IDEController class

Saves the configuration and state of the logical device.

## Syntax


```mof
uint32 SaveProperties();
```



## Parameters

This method has no parameters.

## Return value

A return code that indicates whether the operation completed successfully.

<dl> <dt>


</dt> <dd>

0

The operation completed successfully.

</dd> <dt>


</dt> <dd>

1

The operation was not completed because it is not supported.

</dd> <dt>


</dt> <dd>

3 ...

The operation was not completed because an error occurred.

</dd> </dl>

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

[**CIM\_IDEController**](cim-idecontroller.md)
</dt> </dl>

 

 





