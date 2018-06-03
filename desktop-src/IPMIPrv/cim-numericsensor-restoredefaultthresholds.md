---
title: RestoreDefaultThresholds method of the CIM\_NumericSensor class
description: This method resets the values of the thresholds to hardware defaults.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4ab8969-c38d-4887-9490-58e908e0e115
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RestoreDefaultThresholds method
- RestoreDefaultThresholds method, CIM_NumericSensor class
- CIM_NumericSensor class, RestoreDefaultThresholds method
topic_type:
- apiref
api_name:
- CIM_NumericSensor.RestoreDefaultThresholds
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RestoreDefaultThresholds method of the CIM\_NumericSensor class

This method resets the values of the thresholds to hardware defaults. This method returns 0 if successful, 1 if unsupported and any other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 RestoreDefaultThresholds();
```



## Parameters

This method has no parameters.

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

 

 





