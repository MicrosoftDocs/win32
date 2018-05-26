---
title: OnlineDevice method of the CIM\_Processor class
description: This method is deprecated. Instead, use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9465f7cb-3b49-4f0b-a751-feeaca41b2c1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- OnlineDevice method
- OnlineDevice method, CIM_Processor class
- CIM_Processor class, OnlineDevice method
topic_type:
- apiref
api_name:
- CIM_Processor.OnlineDevice
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineDevice method of the CIM\_Processor class

This method is deprecated. Instead, use the [**RequestStateChange**](cim-processor-requeststatechange.md) method.

**Deprecated description:** Brings the logical device online so it can accept requests, or offline so it can no longer accept requests.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 OnlineDevice(
  [in] boolean Online
);
```



## Parameters

<dl> <dt>

*Online* \[in\]
</dt> <dd>

**true** to bring the device online, **false** to take the device offline.

</dd> </dl>

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

[**CIM\_Processor**](cim-processor.md)
</dt> </dl>

 

 





