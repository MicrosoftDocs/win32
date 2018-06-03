---
title: EnableDevice method of the CIM\_NumericSensor class
description: Note This method is deprecated. Instead we recommend that you use the RequestStateChange method. Enables or disables the sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a8adfc04-7fe0-4446-92f2-f05727f2e7bf
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method
- EnableDevice method, CIM_NumericSensor class
- CIM_NumericSensor class, EnableDevice method
topic_type:
- apiref
api_name:
- CIM_NumericSensor.EnableDevice
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableDevice method of the CIM\_NumericSensor class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the [**RequestStateChange**](sensor-requeststatechange.md) method.

 

Enables or disables the sensor.

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

Indicates whether to enable the sensor. True to enable the sensor; otherwise false.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NumericSensor**](cim-numericsensor.md)
</dt> </dl>

 

 





