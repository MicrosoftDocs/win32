---
title: ClearLog method of the RecordLog class
description: Deletes all records in the BMC system event log (SEL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b85b536e-e7d3-4b4f-a3ce-84ff6f141227
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- IPMI provider Windows Remote Management
- ClearLog method
- ClearLog method, RecordLog class
- RecordLog class, ClearLog method
topic_type:
- apiref
api_name:
- RecordLog.ClearLog
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClearLog method of the RecordLog class

Deletes all records in the BMC system event log (SEL).

## Syntax


```mof
uint32 ClearLog();
```



## Parameters

This method has no parameters.

## Return value

Other codes may be returned if the call fails. On failure, you can obtain available information from the COM function [GetErrorInfo]( http://go.microsoft.com/fwlink/p/?linkid=119575). For scripts, use the command line **net helpmsg** *Return value number*.

<dl> <dt>


</dt> <dd>

0 (0x0)

Success.

</dd> <dt>


</dt> <dd>

1 (0x1)

Not supported.

</dd> <dt>


</dt> <dd>

2 (0x2)

Unspecified error.

</dd> <dt>


</dt> <dd>

3 (0x3)

Time-out.

</dd> <dt>


</dt> <dd>

4 (0x4)

Failed.

</dd> <dt>


</dt> <dd>

5 (0x5)

Invalid parameter.

</dd> <dt>


</dt> <dd>

6 4095

DMTF Reserved

</dd> <dt>


</dt> <dd>

4096 32767

Reserved by this method

</dd> <dt>


</dt> <dd>

32768 (0x8000)

Reserved for vendor.

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

[**RecordLog**](recordlog.md)
</dt> </dl>

 

 





