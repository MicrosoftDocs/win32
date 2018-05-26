---
Description: KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. CIM\_ConcreteJob.RequestStateChange() provides Terminate and Kill options to allow this distinction.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1d1b2789-283c-48ae-b071-e697770bef17
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: KillJob method of the CIM\_ConcreteJob class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# KillJob method of the CIM\_ConcreteJob class

**KillJob** is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. [**CIM\_ConcreteJob**](cim-concretejob.md).[**RequestStateChange**](requeststatechange-cim-concretejob.md)() provides 'Terminate' and 'Kill' options to allow this distinction.

A method to kill this job and any underlying processes, and to remove any 'dangling' associations.

## Syntax


```mof
uint32 KillJob(
  [in] boolean DeleteOnKill
);
```



## Parameters

<dl> <dt>

*DeleteOnKill* \[in\]
</dt> <dd>

Indicates whether or not the Job should be automatically deleted upon termination. This parameter takes precedence over the **DeleteOnCompletion** property.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Access Denied** (6)
</dt> <dt>

**Not Found** (7)
</dt> <dt>

**DMTF Reserved** (8 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> <dt>

[**RequestStateChange**](requeststatechange-cim-concretejob.md)
</dt> </dl>

 

 




