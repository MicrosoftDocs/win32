---
Description: When the job is executing or has terminated without error, then this method returns no CIM\_Error instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b2fa6c08-e2d5-4286-8209-a849afe2b785
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetError method of the CIM\_ConcreteJob class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetError method of the CIM\_ConcreteJob class

When the job is executing or has terminated without error, then this method returns no CIM\_Error instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a CIM\_Error instance is returned.

## Syntax


```mof
uint32 GetError(
  [out] CIM_Error Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

If the OperationalStatus on the Job is not "OK", then this method will return a CIM Error instance. Otherwise, when the Job is "OK", null is returned.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Access Denied** (6)
</dt> <dt>

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




