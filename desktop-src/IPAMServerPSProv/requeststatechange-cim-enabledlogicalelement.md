---
Description: Requests that the state of the element be changed to the value specified in the RequestedState parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e2352227-622f-4d0b-9630-7e32c027279c
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RequestStateChange method of the CIM\_EnabledLogicalElement class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the CIM\_EnabledLogicalElement class

Requests that the state of the element be changed to the value specified in the *RequestedState* parameter. When the requested state change takes place, the **EnabledState** and **RequestedState** of the element will be the same. Invoking the this method multiple times could result in earlier requests being overwritten or lost.

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

The state requested for the element. This information will be placed into the **RequestedState** property of the instance if the return code of the [**RequestStateChange**](msft-ipam-address-requeststatechange.md) method is 0 **Completed with No Error**, or 4096 (0x1000) **Job Started**.

The possible values are.

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

May contain a reference to the ConcreteJob created to track the state transition initiated by the method invocation.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

May contain a reference to the [**CIM\_ConcreteJob**](cim-concretejob.md) created to track the state transition initiated by the method invocation.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown or Unspecified Error** (2)
</dt> <dt>

**Cannot complete within Timeout Period** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid State Transition** (4097)
</dt> <dt>

**Use of Timeout Parameter Not Supported** (4098)
</dt> <dt>

**Busy** (4099)
</dt> <dt>

**Method Reserved** (4100 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md)
</dt> </dl>

 

 




