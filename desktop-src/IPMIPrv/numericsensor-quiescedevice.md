---
title: QuiesceDevice method of the NumericSensor class
description: Temporarily suspends or resumes activity on the numeric sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ADC5F91-78B4-4F26-B1E6-3BABE71380E5
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- QuiesceDevice method
- QuiesceDevice method, NumericSensor interface
- NumericSensor interface, QuiesceDevice method
topic_type:
- apiref
api_name:
- NumericSensor.QuiesceDevice
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# QuiesceDevice method of the NumericSensor class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the [**RequestStateChange**](numericsensor-requeststatechange.md) method.

 

Temporarily suspends or resumes activity on the numeric sensor.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 QuiesceDevice(
  [in] boolean Quiesce
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

3 ...

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> <dt>

[**NumericSensor**](numericsensor.md)
</dt> </dl>

 

 





