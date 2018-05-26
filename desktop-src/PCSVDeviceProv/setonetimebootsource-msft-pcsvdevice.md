---
Description: Sets the one time boot source for the next boot on this computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c2b79c89-4a98-4b94-9a9a-4c10c9b63fff
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SetOneTimeBootSource method of the MSFT\_PCSVDevice class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetOneTimeBootSource method of the MSFT\_PCSVDevice class

Sets the one time boot source for the next boot on this computer system. Implemented.

## Syntax


```mof
uint32 SetOneTimeBootSource(
  [in]      string              StructuredBootString,
  [in, out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*StructuredBootString* \[in\]
</dt> <dd>

A string representing the boot source for next boot.

</dd> <dt>

*Job* \[in, out\]
</dt> <dd>

On return contains a reference to the job, but can be null if the task is completed.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Reserved** (3 4095)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097 32767)
</dt> <dt>

**Vendor Reserved** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




