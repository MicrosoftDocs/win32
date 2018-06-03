---
title: RequestStateChange method of the Msvm\_ConcreteJob class
description: Requests a state change to the job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: adcf8ad1-5f9f-44f4-9b72-895fdd011854
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RequestStateChange method
- RequestStateChange method, Msvm_ConcreteJob class
- Msvm_ConcreteJob class, RequestStateChange method
topic_type:
- apiref
api_name:
- Msvm_ConcreteJob.RequestStateChange
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestStateChange method of the Msvm\_ConcreteJob class

Requests a state change to the job.

## Syntax


```mof
uint32 RequestStateChange(
  [in] uint16   RequestedState,
  [in] datetime TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

Requests a state change to the job.

The possible values are:

<dt>

<span id="Start"></span><span id="start"></span><span id="START"></span>

**Start** (2)


</dt> <dd></dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

**Suspend** (3)


</dt> <dd></dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

**Terminate** (4)


</dt> <dd></dd> <dt>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>

**Kill** (5)


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>7 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. A "0" or **NULL** value indicates that the client has no time requirements for the transition. If this property does not contain "0" or **NULL** and the implementation does not support this parameter, the return code "Use Of Timeout Parameter Not Supported" must be returned.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

32768

Failed

</dd> <dt>


</dt> <dd>

32769

Access Denied

</dd> <dt>


</dt> <dd>

32770

Not Supported

</dd> <dt>


</dt> <dd>

32771

Status is unknown

</dd> <dt>


</dt> <dd>

32772

Timeout

</dd> <dt>


</dt> <dd>

32773

Invalid parameter

</dd> <dt>


</dt> <dd>

32774

System is in used

</dd> <dt>


</dt> <dd>

32775

Invalid state for this operation

</dd> <dt>


</dt> <dd>

32776

Incorrect data type

</dd> <dt>


</dt> <dd>

32777

System is not available

</dd> <dt>


</dt> <dd>

32778

Out of memory

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

[**Msvm\_ConcreteJob**](msvm-concretejob.md)
</dt> </dl>

 

 





