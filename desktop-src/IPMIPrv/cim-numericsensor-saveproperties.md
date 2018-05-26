---
title: SaveProperties method of the CIM\_NumericSensor class
description: Requests that the Device capture its current configuration, setup and/or state information in a backing store. This is handled more generally by the ConfigurationData subclass of SettingData. Therefore, this method is deprecated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe703972-3e41-4b91-9a2b-8bafce5cd9c3
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SaveProperties method
- SaveProperties method, CIM_NumericSensor class
- CIM_NumericSensor class, SaveProperties method
topic_type:
- apiref
api_name:
- CIM_NumericSensor.SaveProperties
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SaveProperties method of the CIM\_NumericSensor class

Requests that the Device capture its current configuration, setup and/or state information in a backing store. This is handled more generally by the ConfigurationData subclass of SettingData. Therefore, this method is deprecated.

The information returned by this method could be used at a later time (via the RestoreProperties method), to return a Device to its present "condition". This method may not be supported by all Devices. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

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
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NumericSensor**](cim-numericsensor.md)
</dt> </dl>

 

 





