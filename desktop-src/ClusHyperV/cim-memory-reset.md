---
title: Reset method of the CIM\_Memory class
description: Resets the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a9b63a1-846c-4148-8e35-76a2e21e3d5b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Reset method
- Reset method, CIM_Memory class
- CIM_Memory class, Reset method
topic_type:
- apiref
api_name:
- CIM_Memory.Reset
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Reset method of the CIM\_Memory class

Resets the logical device.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

The possible return values are:

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

2

The operation is not supported when the device is in the current state.

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

[**CIM\_Memory**](cim-memory.md)
</dt> </dl>

 

 





