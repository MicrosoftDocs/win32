---
title: GetNonLinearFactors method of the NumericSensor class
description: Retrieves data collected by the numeric sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 140A2156-CCD6-4C8C-8690-880943C16B23
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNonLinearFactors method
- GetNonLinearFactors method, NumericSensor interface
- NumericSensor interface, GetNonLinearFactors method
topic_type:
- apiref
api_name:
- NumericSensor.GetNonLinearFactors
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetNonLinearFactors method of the NumericSensor class

> [!Note]  
> This method is deprecated and should not be used.

 

Retrieves data collected by the numeric sensor.

This method is inherited from **CIM\_NumericSensor**.

## Syntax


```mof
uint32 GetNonLinearFactors(
  [in]  sint32 SensorReading,
  [out] sint32 Accuracy,
  [out] uint32 Resolution,
  [out] sint32 Tolerance,
  [out] uint32 Hysteresis
);
```



## Parameters

<dl> <dt>

*SensorReading* \[in\]
</dt> <dd>

The ID of the sensor reading to retrieve.

</dd> <dt>

*Accuracy* \[out\]
</dt> <dd>

The accuracy of the sensor reading.

</dd> <dt>

*Resolution* \[out\]
</dt> <dd>

The resolution of the sensor reading.

</dd> <dt>

*Tolerance* \[out\]
</dt> <dd>

The tolerance of the sensor reading.

</dd> <dt>

*Hysteresis* \[out\]
</dt> <dd>

The hysteresis of the sensor reading.

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
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> <dt>

[**NumericSensor**](numericsensor.md)
</dt> </dl>

 

 





