---
description: Requests that the state of the job be changed to the specified value. The allowed transitions are job specific and vendor specific.
ms.assetid: b36a5f86-2385-485f-852e-c842ccc6bc00
title: RequestStateChange method of the CIM_ConcreteJob WMI class
ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ConcreteJob.RequestStateChange
api_type: 
- COM
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# RequestStateChange method of the CIM_ConcreteJob WMI class

Requests that the state of the job be changed to the specified value. The allowed transitions are job specific and vendor specific. To invoke this method multiple times could cause earlier requests to be overwritten or to be lost.

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

Specifies the state to which the job should be changed.



| Values                                                                                                                                                                                                                                                                | Meaning                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Start"></span><span id="start"></span><span id="START"></span><dl> <dt>**Start**</dt> <dt>2</dt> </dl>                                                   | Changes the state to Running.<br/>                                                                                                                   |
| <span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span><dl> <dt>**Suspend**</dt> <dt>3</dt> </dl>                                           | Stops the job temporarily. You can restart the job and possibly enter the Service state while the job is suspended. This value is job-specific.<br/> |
| <span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span><dl> <dt>**Terminate**</dt> <dt>4</dt> </dl>                                   | Stops the job cleanly, save data, preserve the state, and shut down all underlying processes in an orderly manner.<br/>                              |
| <span id="Kill"></span><span id="kill"></span><span id="KILL"></span><dl> <dt>**Kill**</dt> <dt>5</dt> </dl>                                                       | Stops the job immediately with no requirement to save data or preserve the state. <br/>                                                              |
| <span id="Service"></span><span id="service"></span><span id="SERVICE"></span><dl> <dt>**Service**</dt> <dt>6</dt> </dl>                                           | Puts the job into a vendor-specific Service state. It might be possible to restart the job from this state.<br/>                                     |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>7 32767</dt> </dl>             | Reserved.<br/>                                                                                                                                       |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl> | Reserved.<br/>                                                                                                                                       |



 

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

Specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the *TimeoutPeriod* parameter. A value of 0 or a null parameter indicates that the client has no time requirements for the transition.

> [!Note]  
> If the implementation does not support this parameter and this property does not contain 0 or null, the **Use Of Timeout Parameter Not Supported** value must be returned.

 

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown/Unspecified Error** (2)
</dt> <dt>

**Can NOT complete within Timeout Period** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Transition Started** (4096)
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



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




