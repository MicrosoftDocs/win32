---
description: KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. RequestStateChange provides Terminate and Kill options to allow this distinction.
ms.assetid: 142fadc7-2afe-4da9-a2cf-33b98afbb134
title: KillJob method of the CIM\_Job class


ms.author: windowssdkdev
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
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# KillJob method of the CIM\_Job class

KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. [**RequestStateChange**](cim-concretejob-requeststatechange.md) provides Terminate and Kill options to allow this distinction.

A method to kill this job and any underlying processes, and to remove any dangling associations.

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

Indicates whether or not the Job should be automatically deleted upon termination. This parameter takes precedence over the property, DeleteOnCompletion.

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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 




