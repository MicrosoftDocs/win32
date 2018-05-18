---
Description: 'This method is used to set the one time boot source for the next boot on this computer system.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'df4ff4d9-1188-4b27-a921-7f7ec4a9b7e7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetOneTimeBootSource method of the CIM\_PhysicalComputerSystemView class'
---

# SetOneTimeBootSource method of the CIM\_PhysicalComputerSystemView class

This method is used to set the one time boot source for the next boot on this computer system.

## Syntax


```mof
uint32 SetOneTimeBootSource(
  [in]      string              StructuredBootString,
  [in, out] CIM_ConcreteJob REF Job
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

Reference to the job spawned if the operation continues after the method returns. (May be null if the task is completed).

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097–32767)
</dt> <dt>

**Vendor Reserved** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalComputerSystemView**](cim-physicalcomputersystemview.md)
</dt> </dl>

 

 




