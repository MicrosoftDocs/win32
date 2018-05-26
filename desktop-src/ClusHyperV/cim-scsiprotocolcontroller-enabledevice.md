---
title: EnableDevice method of the CIM\_SCSIProtocolController class
description: Deprecated description Enables or disables the numeric sensor.This method is deprecated. Instead we recommend that you use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 988e7fec-82aa-4cb0-80a3-81bf20bfc354
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method
- EnableDevice method, CIM_SCSIProtocolController class
- CIM_SCSIProtocolController class, EnableDevice method
topic_type:
- apiref
api_name:
- CIM_SCSIProtocolController.EnableDevice
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the CIM\_SCSIProtocolController class

**Deprecated description:** Enables or disables the numeric sensor.

This method is deprecated. Instead we recommend that you use the **RequestStateChange** method.

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

[**CIM\_SCSIProtocolController**](cim-scsiprotocolcontroller.md)
</dt> </dl>

 

 





