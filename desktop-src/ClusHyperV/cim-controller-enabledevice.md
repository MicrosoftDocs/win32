---
title: EnableDevice method of the CIM\_Controller class
description: This method is deprecated. Instead, use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 613077dd-0011-4fc1-9387-2ea30b26aa70
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method
- EnableDevice method, CIM_Controller class
- CIM_Controller class, EnableDevice method
topic_type:
- apiref
api_name:
- CIM_Controller.EnableDevice
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the CIM\_Controller class

This method is deprecated. Instead, use the [**RequestStateChange**](cim-controller-requeststatechange.md) method.

**Deprecated description:** Enables or disables the numeric sensor.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[in\]
</dt> <dd>

Indicates whether to enable the numeric sensor. **true** to enable the sensor; otherwise **false**.

</dd> </dl>

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

 

 





