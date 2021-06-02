---
description: Requests that the state of the planned system be changed to the value specified.
ms.assetid: 54ed9514-4f09-458e-8e86-a807ee66df17
title: RequestStateChange method of the Msvm_PlannedComputerSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_PlannedComputerSystem.RequestStateChange
api_type: 
- COM
api_location: 
- vmms.exe
---

# RequestStateChange method of the Msvm\_PlannedComputerSystem class

Requests that the state of the planned system be changed to the value specified.

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

The requested state for the planned system.

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

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

This parameter is not used and should be **Null**.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This method returns one of the following values.



| Return code/value                                                                                                                      | Description                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>0</dt> </dl>     | Success<br/>                                                                 |
| <dl> <dt></dt> <dt>4096</dt> </dl>  |                                                                                    |
| <dl> <dt></dt> <dt>32768</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32769</dt> </dl> | Access denied.<br/>                                                          |
| <dl> <dt></dt> <dt>32770</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32771</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32772</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32773</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32774</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32775</dt> </dl> | The value specified in the *RequestedState* parameter is not supported.<br/> |
| <dl> <dt></dt> <dt>32776</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32777</dt> </dl> |                                                                                    |
| <dl> <dt></dt> <dt>32778</dt> </dl> |                                                                                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_PlannedComputerSystem**](msvm-plannedcomputersystem.md)
</dt> </dl>

 

 




