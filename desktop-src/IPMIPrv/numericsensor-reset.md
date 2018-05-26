---
title: Reset method of the NumericSensor class
description: Resets the numeric sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0735B679-FF9C-4009-B6D4-00ACFEE19784
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Reset method
- Reset method, NumericSensor interface
- NumericSensor interface, Reset method
topic_type:
- apiref
api_name:
- NumericSensor.Reset
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Reset method of the NumericSensor class

Resets the numeric sensor.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

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

 

 





