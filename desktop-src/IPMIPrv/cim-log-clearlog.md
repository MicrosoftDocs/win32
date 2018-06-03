---
title: ClearLog method of the CIM\_Log class
description: Requests that the Log be cleared of all entries.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 31f2766a-1711-4d95-b3c0-a89779be7316
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ClearLog method
- ClearLog method, CIM_Log class
- CIM_Log class, ClearLog method
topic_type:
- apiref
api_name:
- CIM_Log.ClearLog
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClearLog method of the CIM\_Log class

Requests that the Log be cleared of all entries.

The return value should be 0 if the request was successfully executed, 1 if the request is not supported, and some other value, as indicated by the ValueMap/Values qualifiers, if an error occurred.

## Syntax


```mof
uint32 ClearLog();
```



## Parameters

This method has no parameters.

## Return value

Other codes may be returned if the call fails. On failure, you can obtain available information from the COM function [GetErrorInfo]( http://go.microsoft.com/fwlink/p/?linkid=119575). For scripts, use the command line **net helpmsg** *Return value number*.

<dl> <dt>

**Completed with no error**
</dt> <dd>

0

Success.

</dd> <dt>

**Not Supported**
</dt> <dd>

1

Not supported.

</dd> <dt>

**Unspecified Error**
</dt> <dd>

2

Unspecified error.

</dd> <dt>

**Timeout**
</dt> <dd>

3

Time-out.

</dd> <dt>

**Failed**
</dt> <dd>

4

Failed.

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

Invalid parameter.

</dd> <dt>

**DMTF\_Reserved**
</dt> <dd>

6 4095

Reserved by Distributed Management Task Force (DMTF).

</dd> <dt>

**Method\_Reserved**
</dt> <dd>

4096 32767

Reserved by this method.

</dd> <dt>

**Vendor\_Reserved**
</dt> <dd>

32768 4294967295

Reserved for vendor.

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

[**CIM\_Log**](cim-log.md)
</dt> </dl>

 

 





