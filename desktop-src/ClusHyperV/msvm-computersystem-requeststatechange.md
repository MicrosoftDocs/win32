---
title: RequestStateChange method of the Msvm\_ComputerSystem class
description: Requests a state change on the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da7a5c77-ce78-49b5-9f2e-28e394a84bf6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RequestStateChange method
- RequestStateChange method, Msvm_ComputerSystem class
- Msvm_ComputerSystem class, RequestStateChange method
topic_type:
- apiref
api_name:
- Msvm_ComputerSystem.RequestStateChange
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the Msvm\_ComputerSystem class

Requests a state change on the computer system.

## Syntax


```mof
uint32 RequestStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob REF Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The requested state change.

The possible values are:

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>

**Defer** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>12 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. A value of "0" or **NULL** indicates that the client has no time requirements for the transition. If this property does not contain "0" or **NULL** and the implementation does not support this parameter, the return code "Use Of Timeout Parameter Not Supported" is returned.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

4096

Method Parameters Checked - Job Started

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

System is in use

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

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> </dl>

 

 





