---
Description: An extrinsic method for changing the state of this physical computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5365999f-3d7b-465a-aa3d-f82d47a9e20c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: RequestStateChange method of the CIM\_PhysicalComputerSystemView class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the CIM\_PhysicalComputerSystemView class

An extrinsic method for changing the state of this physical computer system. Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost.A return code of 0 shall indicate the state change was successfully initiated.A return code of 1 shall indicate that the method is not supported. A return code of 2 shall indicate that the method failed.A return code of 4096 shall indicate the state change was successfully initiated, a ConcreteJob has been created, and its reference returned in the output parameter Job.

## Syntax


```mof
uint32 RequestStateChange(
  [in]      uint16              RequestedState,
  [in, out] CIM_ConcreteJob REF Job,
  [in]      datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

See CIM\_ComputerSystem.RequestedStateChange.RequestedState for details.

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

*Job* \[in, out\]
</dt> <dd>

May contain a reference to the ConcreteJob created to track the state transition initiated by the method invocation.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

See CIM\_ComputerSystem.TimeoutPeriod for details.

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

**DMTF Reserved** (4097 32767)
</dt> <dt>

**Vendor Reserved** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalComputerSystemView**](cim-physicalcomputersystemview.md)
</dt> </dl>

 

 




