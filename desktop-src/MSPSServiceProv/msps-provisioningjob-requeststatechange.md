---
title: RequestStateChange method of the Msps\_ProvisioningJob class
description: Requests that the state of the job be changed to the value specified in the RequestedState parameter. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '55baf3b1-9e1b-482c-a51a-1421f764353e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RequestStateChange method", "RequestStateChange method, Msps_ProvisioningJob class", "Msps_ProvisioningJob class, RequestStateChange method"]
topic_type:
- apiref
api_name:
- Msps_ProvisioningJob.RequestStateChange
api_location:
- MSPSService.dll
api_type:
- COM
---

# RequestStateChange method of the Msps\_ProvisioningJob class

Requests that the state of the job be changed to the value specified in the RequestedState parameter. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost.

If 0 is returned, then the task completed successfully. Any other return code indicates an error condition.

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

The requested state for the job.

<dt>

2
</dt> <dd>

**Start** - changes the state to 'Running'.

</dd> <dt>

3
</dt> <dd>

**Suspend** - stops the job temporarily. The intention is to subsequently restart the job with 'Start'. It might be possible to enter the 'Service' state while suspended. (This is job-specific.)

</dd> <dt>

4
</dt> <dd>

**Terminate** - stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner.

</dd> <dt>

5
</dt> <dd>

**Kill** - terminates the job immediately with no requirement to save data or preserve the state.

</dd> <dt>

6
</dt> <dd>

**Service** - puts the job into a vendor-specific service state. It might be possible to restart the job.

</dd> <dt>

7–32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768–65535
</dt> <dd>

Vendor Reserved

</dd> </dl> </dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the *TimeoutPeriod*. A value of 0 or a null parameter indicates that the client has no time requirements for the transition.

If this property does not contain 0 or null and the implementation does not support this parameter, a return code of 'Use Of Timeout Parameter Not Supported' must be returned.

</dd> </dl>

## Return value

<dl> <dt>


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

1

Not Supported

</dd> <dt>


</dt> <dd>

2

Unknown/Unspecified Error

</dd> <dt>


</dt> <dd>

3

Can NOT complete within Timeout Period

</dd> <dt>


</dt> <dd>

4

Failed

</dd> <dt>


</dt> <dd>

5

Invalid Parameter

</dd> <dt>


</dt> <dd>

6

In Use

</dd> <dt>


</dt> <dd>

7–4095

DMTF Reserved

</dd> <dt>


</dt> <dd>

4096

Method Parameters Checked - Transition Started

</dd> <dt>


</dt> <dd>

4097

Invalid State Transition

</dd> <dt>


</dt> <dd>

4098

Use of Timeout Parameter Not Supported

</dd> <dt>


</dt> <dd>

4099

Busy

</dd> <dt>


</dt> <dd>

4100–32767

Method Reserved

</dd> <dt>


</dt> <dd>

32768–65535

Vendor Specific

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningJob**](msps-provisioningjob.md)
</dt> </dl>

 

 





