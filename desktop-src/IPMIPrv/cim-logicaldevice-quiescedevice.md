---
title: QuiesceDevice method of the CIM\_LogicalDevice class
description: Note This method is deprecated. Instead we recommend that you use the RequestStateChange method. Temporarily suspends activity on the sensor, or re-enables the activity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3c4959be-341c-416d-a55b-f94a7a756c29'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["QuiesceDevice method", "QuiesceDevice method, CIM_LogicalDevice class", "CIM_LogicalDevice class, QuiesceDevice method"]
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.QuiesceDevice
api_location:
- IpmiPrv.dll
api_type:
- COM
---

# QuiesceDevice method of the CIM\_LogicalDevice class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the [**RequestStateChange**](sensor-requeststatechange.md) method.

 

Temporarily suspends activity on the sensor, or re-enables the activity.

## Syntax


```mof
uint32 QuiesceDevice(
  [in] boolean Quiesce
);
```



## Parameters

<dl> <dt>

*Quiesce* \[in\]
</dt> <dd>

Indicates whether the numeric sensor is to temporarily suspend activity or resume activity. True to suspend activity. False to resume activity.

</dd> </dl>

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

2

The operation is not supported when the device is in the current state.

</dd> <dt>


</dt> <dd>

3–...

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

 





