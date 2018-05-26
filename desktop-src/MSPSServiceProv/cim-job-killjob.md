---
title: KillJob method of the CIM\_Job class
description: KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 29e1564d-d89d-4b5c-a121-478126660368
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- KillJob method
- KillJob method, CIM_Job class
- CIM_Job class, KillJob method
topic_type:
- apiref
api_name:
- CIM_Job.KillJob
api_location:
- MSPSService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# KillJob method of the CIM\_Job class

**KillJob** is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill.

[**CIM\_ConcreteJob**](cim-concretejob.md).[**RequestStateChange**](cim-concretejob-requeststatechange.md)() provides 'Terminate' and 'Kill' options to allow this distinction. A method to kill this job and any underlying processes, and to remove any 'dangling' associations.

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

Indicates whether or not the Job should be automatically deleted upon termination. This parameter takes precedence over the property, **DeleteOnCompletion.**

</dd> </dl>

## Return value

<dl> <dt>

**Success**
</dt> <dd>

0

**Success**

</dd> <dt>

**Not Supported**
</dt> <dd>

1

**Not Supported**

</dd> <dt>

**Unknown**
</dt> <dd>

2

**Unknown**

</dd> <dt>

**Timeout**
</dt> <dd>

3

**Timeout**

</dd> <dt>

**Failed**
</dt> <dd>

4

**Failed**

</dd> <dt>

**Access Denied**
</dt> <dd>

6

**Access Denied**

</dd> <dt>

**Not Found**
</dt> <dd>

7

**Not Found**

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

8 32767

**DMTF Reserved**

</dd> <dt>

**Vendor Specific**
</dt> <dd>

32768 65535

**Vendor Specific**

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 





