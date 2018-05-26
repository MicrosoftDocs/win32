---
Description: Requests that the state of the job be changed to the value specified in the RequestedState parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 720ee065-983a-470a-bcc8-9a966f6fcc9d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: RequestStateChange method of the CIM\_ConcreteJob class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the CIM\_ConcreteJob class

Requests that the state of the job be changed to the value specified in the RequestedState parameter. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully. Any other return code indicates an error condition.

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

RequestStateChange changes the state of a job. The possible values are as follows: Start (2) changes the state to 'Running'. Suspend (3) stops the job temporarily. The intention is to subsequently restart the job with 'Start'. It might be possible to enter the 'Service' state while suspended. (This is job-specific.) Terminate (4) stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner. Kill (5) terminates the job immediately with no requirement to save data or preserve the state. Service (6) puts the job into a vendor-specific service state. It might be possible to restart the job.

<dt>

<span id="Start"></span><span id="start"></span><span id="START"></span>

**Start** (2)


</dt> <dd></dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

**Suspend** (3)


</dt> <dd></dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

**Terminate** (4)


</dt> <dd></dd> <dt>

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>

**Kill** (5)


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>7 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the TimeoutPeriod. A value of 0 or a null parameter indicates that the client has no time requirements for the transition. If this property does not contain 0 or null and the implementation does not support this parameter, a return code of 'Use Of Timeout Parameter Not Supported' must be returned.

</dd> </dl>

## Return value

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



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




