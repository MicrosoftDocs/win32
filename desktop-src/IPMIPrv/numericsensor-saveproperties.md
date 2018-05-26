---
title: SaveProperties method of the NumericSensor class
description: Saves the configuration and state of the numeric sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74DFDC36-DE1A-4BF0-94A0-217899D26268
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SaveProperties method
- SaveProperties method, NumericSensor interface
- NumericSensor interface, SaveProperties method
topic_type:
- apiref
api_name:
- NumericSensor.SaveProperties
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SaveProperties method of the NumericSensor class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the **ConfigurationInformation** property of the **CIM\_ConfigurationData** class.

 

Saves the configuration and state of the numeric sensor.

This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

## Syntax


```mof
uint32 SaveProperties();
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

 

 





