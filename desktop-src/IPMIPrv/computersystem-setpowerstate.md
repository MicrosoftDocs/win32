---
title: SetPowerState method of the ComputerSystem class
description: Note This method is deprecated. Instead we recommend that you use the SetPowerState property of the CIM\_PowerManagementService class. Sets the power state of the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FB062FB9-BA45-4576-A8A6-B85DAF8042CB
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, ComputerSystem interface
- ComputerSystem interface, SetPowerState method
topic_type:
- apiref
api_name:
- ComputerSystem.SetPowerState
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the ComputerSystem class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the **SetPowerState** property of the **CIM\_PowerManagementService** class.

 

Sets the power state of the computer system.

This method is inherited from [**CIM\_ComputerSystem**](cim_computersystem).

## Syntax


```mof
uint32 SetPowerState(
  [in] uint32   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

The requested power state for the computer system.

This property can contain one of the following values:

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

</dd> <dt>

7
</dt> <dd>

Hibernate

</dd> <dt>

8
</dt> <dd>

Soft Off

</dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Indicates when to set the power state, either as a regular **datetimevalue** or as an interval value (where the interval begins when the method invocation is received).

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

2 ...

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

[**ComputerSystem**](computersystem.md)
</dt> </dl>

 

 





