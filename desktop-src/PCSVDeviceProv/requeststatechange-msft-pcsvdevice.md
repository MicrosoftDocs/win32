---
Description: Requests that the state of the physical computer system be changed to the specified value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f1608208-b3e5-46a6-b5fb-eb40252de31f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: RequestStateChange method of the MSFT\_PCSVDevice class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestStateChange method of the MSFT\_PCSVDevice class

Requests that the state of the physical computer system be changed to the specified value. Implemented. Invoking this method multiple times could result in earlier requests being overwritten or lost.

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

Specifies the state requested for the physical computer system.

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

On return contains a reference to the job, but can be null if the task is completed.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

Specifies the maximum amount of time that the client expects the transition to the new state to take. The timeout must be specified using the **datetime** interval format.

A value of zero or **NULL** indicates that the client has no time requirements for the transition. If this property does not contain zero or **NULL** and the implementation does not support this parameter, a return code of **Use Of Timeout Parameter Not Supported** must be returned.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Reserved** (3 4095)
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
| MOF<br/>                      | <dl> <dt>PCSVDevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVDevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> </dl>

 

 




