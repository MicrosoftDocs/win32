---
description: Changes the state of the job.
ms.assetid: 3B11CE45-63E4-43D1-AAF6-02F83C9CBB85
title: Msvm_CopyFileToGuestJob::RequestStateChange method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CopyFileToGuestJob.RequestStateChange
api_type: 
- COM
api_location: 
- vmms.exe
---

# Msvm\_CopyFileToGuestJob::RequestStateChange method

Changes the state of the job.

## Syntax


```C++
uint32 RequestStateChange(
  [in] uint16   RequestedState,
  [in] datetime TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The new state. These are the possible values:

<dt>

<span id="Start"></span><span id="start"></span><span id="START"></span>

<span id="Start"></span><span id="start"></span><span id="START"></span>**Start** (2)


</dt> <dd>

Changes the state to 'Running'.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (3)


</dt> <dd>

Stops the job temporarily. The client can then subsequently restart the job with 'Start'. The client can possibly enter the 'Service' state while suspended (this is job-specific).

</dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>**Terminate** (4)


</dt> <dd>

Stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner.

</dd> <dt>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>**Kill** (5)


</dt> <dd>

Terminates the job immediately with no requirement to save data or preserve the state.

</dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>**Service** (6)


</dt> <dd>

Puts the job into a vendor-specific service state. The client can possibly restart the job.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (7..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl> </dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the timeout period. A value of 0 or **Null** indicates that the client has no time requirements for the transition. If this property does not contain 0 or **Null** and the implementation does not support this parameter, a return code of 4098 (**Use Of Timeout Parameter Not Supported**) must be returned.

</dd> </dl>

## Return value

This method returns one of the following values.



| Return code/value                                                                                                                                                               | Description                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                   | Success.<br/>                                                                |
| <dl> <dt>**Use of Timeout Parameter Not Supported**</dt> <dt>4098</dt> </dl> |                                                                                    |
| <dl> <dt>**Failed**</dt> <dt>32768</dt> </dl>                                |                                                                                    |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                         | Access denied.<br/>                                                          |
| <dl> <dt>**Not Supported**</dt> <dt>32770</dt> </dl>                         |                                                                                    |
| <dl> <dt>**Status is unknown**</dt> <dt>32771</dt> </dl>                     |                                                                                    |
| <dl> <dt>**Timeout**</dt> <dt>32772</dt> </dl>                               |                                                                                    |
| <dl> <dt>**Invalid parameter**</dt> <dt>32773</dt> </dl>                     |                                                                                    |
| <dl> <dt>**System is in use**</dt> <dt>32774</dt> </dl>                      |                                                                                    |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>      | The value specified in the *RequestedState* parameter is not supported.<br/> |
| <dl> <dt>**Incorrect data type**</dt> <dt>32776</dt> </dl>                   |                                                                                    |
| <dl> <dt>**System is not available**</dt> <dt>32777</dt> </dl>               |                                                                                    |
| <dl> <dt>**Out of memory**</dt> <dt>32778</dt> </dl>                         |                                                                                    |



 

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

[**Msvm\_CopyFileToGuestJob**](msvm-copyfiletoguestjob.md)
</dt> </dl>

 

 




