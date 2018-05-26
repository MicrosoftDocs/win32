---
title: Reset method of the CIM\_Controller class
description: Resets the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61a41b0e-d139-450c-83eb-87e52f228d3b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Reset method
- Reset method, CIM_Controller class
- CIM_Controller class, Reset method
topic_type:
- apiref
api_name:
- CIM_Controller.Reset
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Reset method of the CIM\_Controller class

Resets the logical device.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

The possible return values are.

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

3 = *value*

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

[**CIM\_Controller**](cim-controller.md)
</dt> </dl>

 

 





