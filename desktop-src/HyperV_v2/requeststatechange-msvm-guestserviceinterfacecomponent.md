---
description: Requests that the state of the guest service interface component be changed to the specified value.
ms.assetid: D9F7CD03-0D86-4005-A600-5CC7082A5047
title: Msvm_GuestServiceInterfaceComponent::RequestStateChange method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_GuestServiceInterfaceComponent.RequestStateChange
api_type: 
- COM
api_location: 
- vmms.exe
---

# Msvm\_GuestServiceInterfaceComponent::RequestStateChange method

Requests that the state of the guest service interface component be changed to the specified value.

## Syntax


```C++
uint32 RequestStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

Type: **uint16**

The new state. The info is placed in the **RequestedState** property of the instance if the return code of the **RequestStateChange** method is 0 or 4096. For more info, see the description of the **EnabledState** and **RequestedState** properties for the element. This must be one of the following values.

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

Type: **[**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85))**

An optional reference to a [**Msvm\_ConcreteJob**](msvm-concretejob.md) object that is returned if the operation is executed asynchronously. If present, the returned reference can be used to monitor progress and obtain the result of the method.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

Type: **datetime**

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the timeout period. A value of 0 or **Null** indicates that the client has no time requirements for the transition. If this property does not contain 0 or **Null** and the implementation does not support this parameter, a return code of 4098 (**Use Of Timeout Parameter Not Supported**) must be returned.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.



| Return code/value                                                                                                                                                                       | Description         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                           | Success.<br/> |
| <dl> <dt>**Not supported**</dt> <dt>1</dt> </dl>                                     |                     |
| <dl> <dt>**Unknown/Unspecified Error**</dt> <dt>2</dt> </dl>                         |                     |
| <dl> <dt>**Can NOT complete within Timeout Period**</dt> <dt>3</dt> </dl>            |                     |
| <dl> <dt>**Failed**</dt> <dt>4</dt> </dl>                                            |                     |
| <dl> <dt>**Invalid Parameter**</dt> <dt>5</dt> </dl>                                 |                     |
| <dl> <dt>**In Use**</dt> <dt>6</dt> </dl>                                            |                     |
| <dl> <dt>**DMTF Reserved**</dt> <dt>..</dt> </dl>                                    |                     |
| <dl> <dt>**Method Parameters Checked - Transition Started**</dt> <dt>4096</dt> </dl> |                     |
| <dl> <dt>**Invalid State Transition**</dt> <dt>4097</dt> </dl>                       |                     |
| <dl> <dt>**Use of Timeout Parameter Not Supported**</dt> <dt>4098</dt> </dl>         |                     |
| <dl> <dt>**Busy**</dt> <dt>4099</dt> </dl>                                           |                     |
| <dl> <dt>**Method Reserved**</dt> <dt>4100..32767</dt> </dl>                         |                     |
| <dl> <dt>**Vendor Specific**</dt> <dt>32768..65535</dt> </dl>                        |                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | \\\\Root\\Virtualization\\V2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_GuestServiceInterfaceComponent**](msvm-guestserviceinterfacecomponent.md)
</dt> </dl>

 

