---
Description: An extrinsic method for clearing a log on this physical computer system.Requests that the Log be cleared of all entries.The return value shall be 0 if the request was successfully executed, 1 if the request is not supported, and 2 if an error occurred.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5daaaa01-c70c-4632-a3ce-25318aa75fdc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: ClearLog method of the CIM\_PhysicalComputerSystemView class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClearLog method of the CIM\_PhysicalComputerSystemView class

An extrinsic method for clearing a log on this physical computer system.Requests that the Log be cleared of all entries.The return value shall be 0 if the request was successfully executed, 1 if the request is not supported, and 2 if an error occurred. A return code of 4096 shall indicate the request to clear log was successfully initiated, a ConcreteJob has been created, and its reference returned in the output parameter Job.

## Syntax


```mof
uint32 ClearLog(
  [in] string LogInstanceID
);
```



## Parameters

<dl> <dt>

*LogInstanceID* \[in\]
</dt> <dd>

Idenfier for the log that is requested to be cleared.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**DMTF Reserved** (3 32767)
</dt> <dt>

**Vendor Reserved** (32768 65535)
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

[**CIM\_PhysicalComputerSystemView**](cim-physicalcomputersystemview.md)
</dt> </dl>

 

 




