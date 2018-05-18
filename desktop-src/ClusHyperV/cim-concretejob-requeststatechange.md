---
title: RequestStateChange method of the CIM\_ConcreteJob class
description: Requests the specified state change to a concrete job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7aace66c-2946-4dd7-a95c-bbfa41480e11'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RequestStateChange method", "RequestStateChange method, CIM_ConcreteJob class", "CIM_ConcreteJob class, RequestStateChange method"]
topic_type:
- apiref
api_name:
- CIM_ConcreteJob.RequestStateChange
api_location:
- VMMS.exe
api_type:
- COM
---

# RequestStateChange method of the CIM\_ConcreteJob class

Requests the specified state change to a concrete job.

> [!Note]  
> Invoking this method multiple times could result in earlier requests being overwritten or lost.

 

## Syntax


```mof
uint32 RequestStateChange(
  [in] uint16   RequestedState,
  [in] datetime TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The requested state change.

The possible values are.

<dt>

<span id="Start"></span><span id="start"></span><span id="START"></span>

<span id="Start"></span><span id="start"></span><span id="START"></span>**Start** (2)


</dt> <dd>

Starts the job.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (3)


</dt> <dd>

Pauses the job.

</dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>**Terminate** (4)


</dt> <dd>

Saves data, preserves the stat, and then shuts down the job.

</dd> <dt>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>**Kill** (5)


</dt> <dd>

Shuts the job down immediately.

</dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>**Service** (6)


</dt> <dd>

Puts the job into a vendor-specific service state.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl> </dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

The timeout period required by the client when waiting for the state transition. A 0(zero) or **null** value indicates that the client does not have a timeout requirement for this state transition.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unknown/Unspecified Error**
</dt> <dd>

2

Unknown or Unspecified Error

</dd> <dt>

**Can NOT complete within Timeout Period**
</dt> <dd>

3

Cannot complete within Timeout Period

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**In Use**
</dt> <dd>

6

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

7–4095

</dd> <dt>

**Method Parameters Checked - Transition Started**
</dt> <dd>

4096

Method Parameters Checked - Job Started

</dd> <dt>

**Invalid State Transition**
</dt> <dd>

4097

</dd> <dt>

**Use of Timeout Parameter Not Supported**
</dt> <dd>

4098

</dd> <dt>

**Busy**
</dt> <dd>

4099

</dd> <dt>

**Method Reserved**
</dt> <dd>

4100–32767

</dd> <dt>

**Vendor Specific**
</dt> <dd>

32768–65535

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





