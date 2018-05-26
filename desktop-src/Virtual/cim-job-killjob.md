---
title: KillJob method of the CIM\_Job class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: 931f4505-b87e-4ab4-bfb2-7befa4482b69
keywords:
- KillJob method Hyper-V
- KillJob method Hyper-V , CIM_Job class
- CIM_Job class Hyper-V , KillJob method
topic_type:
- apiref
api_name:
- CIM_Job.KillJob
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# KillJob method of the CIM\_Job class

This method is deprecated. Instead, use the **RequestStateChange** method.

> [!Note]  
> Deprecated description: Shuts down a job.

 

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

**True** if the job should be automatically deleted upon termination; otherwise, **false**.

> [!Note]  
> This parameter takes precedence over the **DeleteOnCompletion** property of the **CIM\_Job** class.

 

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



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 





