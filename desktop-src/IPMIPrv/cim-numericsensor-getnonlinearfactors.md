---
title: GetNonLinearFactors method of the CIM\_NumericSensor class
description: The use of this method is being deprecated, since Current senor reading can be retrieved through the GetInstance operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8adf3820-fb40-431e-ad3a-69e5496688e0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetNonLinearFactors method", "GetNonLinearFactors method, CIM_NumericSensor class", "CIM_NumericSensor class, GetNonLinearFactors method"]
topic_type:
- apiref
api_name:
- CIM_NumericSensor.GetNonLinearFactors
api_location:
- IpmiPrv.dll
api_type:
- COM
---

# GetNonLinearFactors method of the CIM\_NumericSensor class

The use of this method is being deprecated, since Current senor reading can be retrieved through the GetInstance operation.

For a non-linear Sensor, the resolution, accuracy, tolerance and hysteresis vary as the current reading moves. This method can be used to get these factors for a given reading. It returns 0 if successful, 1 if unsupported, and any other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 GetNonLinearFactors(
  [in]  sint32 SensorReading,
  [out] sint32 Accuracy,
  [out] uint32 Resolution,
  [out] sint32 Tolerance,
  [out] uint32 Hysteresis
);
```



## Parameters

<dl> <dt>

*SensorReading* \[in\]
</dt> <dd>

The sensor reading to get information for.

</dd> <dt>

*Accuracy* \[out\]
</dt> <dd>

The accuracy of the reading.

</dd> <dt>

*Resolution* \[out\]
</dt> <dd>

The resolution of the reading.

</dd> <dt>

*Tolerance* \[out\]
</dt> <dd>

The tolerance of the reading.

</dd> <dt>

*Hysteresis* \[out\]
</dt> <dd>

The Hysteresis of the reading.

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

[**CIM\_NumericSensor**](cim-numericsensor.md)
</dt> </dl>

 

 





