---
title: OnlineDevice method of the CIM\_LogicalDevice class
description: Brings the sensor online so it can accept requests, or offline so it can no longer accept requests.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76c8d74b-dbaa-41c6-8d4b-c407e56882ee
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- OnlineDevice method
- OnlineDevice method, CIM_LogicalDevice class
- CIM_LogicalDevice class, OnlineDevice method
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.OnlineDevice
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineDevice method of the CIM\_LogicalDevice class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the [**RequestStateChange**](sensor-requeststatechange.md) method.

 

Brings the sensor online so it can accept requests, or offline so it can no longer accept requests.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 OnlineDevice(
  [in] boolean Online
);
```



## Parameters

<dl> <dt>

*Online* \[in\]
</dt> <dd>

Indicates whether the sensor is to accept requests. True to accept requests, otherwise false.

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
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

 





