---
title: KillJob method of the CIM\_ConcreteJob class
description: Shuts down a job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3f087663-b86e-4011-894c-d02c3bed8c0c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- KillJob method
- KillJob method, CIM_ConcreteJob class
- CIM_ConcreteJob class, KillJob method
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.KillJob
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KillJob method of the CIM\_ConcreteJob class

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
> This parameter takes precedence of the **DeleteOnCompletion** property of the **CIM\_Job** class.

 

</dd> </dl>

## Return value

<dl> <dt>


</dt> <dd>

0

Success

</dd> <dt>


</dt> <dd>

1

Not Supported

</dd> <dt>


</dt> <dd>

2

Unknown

</dd> <dt>


</dt> <dd>

3

Timeout

</dd> <dt>


</dt> <dd>

4

Failed

</dd> <dt>


</dt> <dd>

6

Access Denied

</dd> <dt>


</dt> <dd>

7

Not Found

</dd> <dt>


</dt> <dd>

8 32767

DMTF Reserved

</dd> <dt>


</dt> <dd>

32768 65535

Vendor Specific

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





