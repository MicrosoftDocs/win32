---
title: EnableDevice method of the CIM\_PointingDevice class
description: Deprecated description Enables or disables the numeric sensor.This method is deprecated. Instead we recommend that you use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8be89d64-0cfd-4322-8262-664c55cb28e0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["EnableDevice method", "EnableDevice method, CIM_PointingDevice class", "CIM_PointingDevice class, EnableDevice method"]
topic_type:
- apiref
api_name:
- CIM_PointingDevice.EnableDevice
api_location:
- VMMS.exe
api_type:
- COM
---

# EnableDevice method of the CIM\_PointingDevice class

**Deprecated description:** Enables or disables the numeric sensor.

This method is deprecated. Instead we recommend that you use the **RequestStateChange** method.

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_PointingDevice**](cim-pointingdevice.md)
</dt> </dl>

 

 





