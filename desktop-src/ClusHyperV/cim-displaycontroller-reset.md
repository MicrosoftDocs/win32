---
title: Reset method of the CIM\_DisplayController class
description: Resets the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '13cfc50c-7a04-41e6-8c1f-f4313b0bb257'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method", "Reset method, CIM_DisplayController class", "CIM_DisplayController class, Reset method"]
topic_type:
- apiref
api_name:
- CIM_DisplayController.Reset
api_location:
- VMMS.exe
api_type:
- COM
---

# Reset method of the CIM\_DisplayController class

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

3–...

The operation was not completed because an error occurred.

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

[**CIM\_DisplayController**](cim-displaycontroller.md)
</dt> </dl>

 

 





