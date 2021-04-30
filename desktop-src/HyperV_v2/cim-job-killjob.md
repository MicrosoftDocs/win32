---
description: A method to kill this job and any underlying processes, and to remove any dangling associations. This method is deprecated; use RequestChangeState instead.
ms.assetid: b116631f-34b8-43ed-9c17-062b5e6058d0
title: KillJob method of the CIM_Job class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Job.KillJob
api_type: 
- COM
api_location: 
- vmms.exe
---

# KillJob method of the CIM\_Job class

A method to kill this job and any underlying processes, and to remove any 'dangling' associations. This method is deprecated; use **RequestChangeState** instead. **KillJob** is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. [**CIM\_ConcreteJob**](cim-concretejob.md).**RequestStateChange**() provides 'Terminate' and 'Kill' options to allow this distinction.

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

Returns a 0 on success; otherwise, returns an error.

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

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 




