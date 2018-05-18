---
title: SetPowerState method of the NumericSensor class
description: Sets the power state of the numeric sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D5A991AE-7BDC-4D49-8EDA-C05D4BB1EC3B'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetPowerState method", "SetPowerState method, NumericSensor interface", "NumericSensor interface, SetPowerState method"]
topic_type:
- apiref
api_name:
- NumericSensor.SetPowerState
api_location:
- IpmiPrv.dll
api_type:
- COM
---

# SetPowerState method of the NumericSensor class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the **SetPowerState** property of the **CIM\_PowerManagementService** class.

 

Sets the power state of the numeric sensor.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

The power state to set.

This parameter can contain one of the following values:

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

Indicates when to set the power state, either as a regular **datetime**value or as an interval value (where the interval begins when the method invocation is received).

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

2–...

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> <dt>

[**NumericSensor**](numericsensor.md)
</dt> </dl>

 

 





