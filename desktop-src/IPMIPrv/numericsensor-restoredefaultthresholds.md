---
title: RestoreDefaultThresholds method of the NumericSensor class
description: Resets the values of numeric sensor thresholds to the hardware default values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a0071d4e-3dd9-44c1-b506-c1c8230c11ad'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["IPMI provider Windows Remote Management", "RestoreDefaultThresholds method", "RestoreDefaultThresholds method, NumericSensor class", "NumericSensor class, RestoreDefaultThresholds method"]
topic_type:
- apiref
api_name:
- NumericSensor.RestoreDefaultThresholds
api_location:
- IpmiPrv.dll
api_type:
- COM
---

# RestoreDefaultThresholds method of the NumericSensor class

Resets the values of numeric sensor thresholds to the hardware default values.

## Syntax


```mof
uint32 RestoreDefaultThresholds();
```



## Parameters

This method has no parameters.

## Return value

Other codes may be returned if the call fails. On failure, you can obtain available information from the COM function [GetErrorInfo]( http://go.microsoft.com/fwlink/p/?linkid=119575). For scripts, use the command line **net helpmsg** *Return value number*.

<dl> <dt>


</dt> <dd>

0

Success.

</dd> <dt>


</dt> <dd>

1

Method unsupported.

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

 

 





