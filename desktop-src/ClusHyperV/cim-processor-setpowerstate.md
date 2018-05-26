---
title: SetPowerState method of the CIM\_Processor class
description: This method is deprecated. Instead, use the SetPowerState property of the CIM\_PowerManagementService class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8421b50e-25b7-4886-9f28-d308f176c5e2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, CIM_Processor class
- CIM_Processor class, SetPowerState method
topic_type:
- apiref
api_name:
- CIM_Processor.SetPowerState
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the CIM\_Processor class

This method is deprecated. Instead, use the **SetPowerState** property of the **CIM\_PowerManagementService** class.

**Deprecated description:** Sets the power state of the logical device.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

The power state to set.

The possible values are:

<dt>

1
</dt> <dd>

Full Power

</dd> <dt>

2
</dt> <dd>

Power Save - Low Power Mode

</dd> <dt>

3
</dt> <dd>

Power Save - Standby

</dd> <dt>

4
</dt> <dd>

Power Save - Other

</dd> <dt>

5
</dt> <dd>

Power Cycle

</dd> <dt>

6
</dt> <dd>

Power Off

</dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Indicates when to set the power state, either as a regular **datetime** value or as an interval value (where the interval begins when the method invocation is received).

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

2 = *value*

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

 

 





