---
title: BG_JOB_STATE enumeration (Deliveryoptimization.h)
description: The BG_JOB_STATE enumeration defines constant values for the different states of a job.
ms.assetid: DB4806BD-08BC-4F0B-A7F4-BA0719112811
keywords:
- BG_JOB_STATE enumeration
- BG_JOB_STATE enumeration
topic_type:
- apiref
api_name:
- BG_JOB_STATE
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BG_JOB_STATE enumeration

The **BG_JOB_STATE** enumeration defines constant values for the different states of a job.

## Syntax


```C++
typedef enum  { 
  BG_JOB_STATE_QUEUED,
  BG_JOB_STATE_CONNECTING,
  BG_JOB_STATE_TRANSFERRING,
  BG_JOB_STATE_SUSPENDED,
  BG_JOB_STATE_ERROR,
  BG_JOB_STATE_TRANSIENT_ERROR,
  BG_JOB_STATE_TRANSFERRED,
  BG_JOB_STATE_ACKNOWLEDGED,
  BG_JOB_STATE_CANCELLED
} BG_JOB_STATE;
```



## Constants

<dl> <dt>

<span id="BG_JOB_STATE_QUEUED"></span><span id="bg_job_state_queued"></span>**BG_JOB_STATE_QUEUED**
</dt> <dd>

Specifies that the job is in the queue and waiting to run. If a user logs off while their job is transferring, the job transitions to the queued state.

</dd> <dt>

<span id="BG_JOB_STATE_CONNECTING"></span><span id="bg_job_state_connecting"></span>**BG_JOB_STATE_CONNECTING**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_JOB_STATE_TRANSFERRING"></span><span id="bg_job_state_transferring"></span>**BG_JOB_STATE_TRANSFERRING**
</dt> <dd>

Specifies that Delivery Optimization is transferring data for the job.

</dd> <dt>

<span id="BG_JOB_STATE_SUSPENDED"></span><span id="bg_job_state_suspended"></span>**BG_JOB_STATE_SUSPENDED**
</dt> <dd>

Specifies that the job is suspended (paused). To suspend a job, call the [**IBackgroundCopyJob::Suspend**](ibackgroundcopyjob-suspend.md) method. The job remains suspended until you call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md), [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md), or [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method.

</dd> <dt>

<span id="BG_JOB_STATE_ERROR"></span><span id="bg_job_state_error"></span>**BG_JOB_STATE_ERROR**
</dt> <dd>

Specifies that a nonrecoverable error occurred (the service is unable to transfer the file). If the error, such as an access-denied error, can be corrected, call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md) method after the error is fixed. However, if the error cannot be corrected, call the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method to cancel the job, or call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method to accept the portion of a download job that transferred successfully.

</dd> <dt>

<span id="BG_JOB_STATE_TRANSIENT_ERROR"></span><span id="bg_job_state_transient_error"></span>**BG_JOB_STATE_TRANSIENT_ERROR**
</dt> <dd>

Specifies that a recoverable error occurred. Delivery Optimization will retry jobs in the transient error state based on the internal retry configuration. The state of the job changes to **BG_JOB_STATE_ERROR** if the job fails to make progress (see [**IBackgroundCopyJob::SetNoProgressTimeout**](ibackgroundcopyjob-setnoprogresstimeout.md)).

</dd> <dt>

<span id="BG_JOB_STATE_TRANSFERRED"></span><span id="bg_job_state_transferred"></span>**BG_JOB_STATE_TRANSFERRED**
</dt> <dd>

Specifies that your job was successfully processed. You must call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method to acknowledge completion of the job and to make the files available to the client.

</dd> <dt>

<span id="BG_JOB_STATE_ACKNOWLEDGED"></span><span id="bg_job_state_acknowledged"></span>**BG_JOB_STATE_ACKNOWLEDGED**
</dt> <dd>

Specifies that you called the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method to acknowledge that your job completed successfully.

</dd> <dt>

<span id="BG_JOB_STATE_CANCELLED"></span><span id="bg_job_state_cancelled"></span>**BG_JOB_STATE_CANCELLED**
</dt> <dd>

Specifies that you called the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method to cancel the job (remove the job from the transfer queue).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**IBackgroundCopyJob::GetState**](ibackgroundcopyjob-getstate.md)
</dt> </dl>

 

 





