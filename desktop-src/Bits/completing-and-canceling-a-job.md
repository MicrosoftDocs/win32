---
title: Completing and Canceling a Job
description: To complete a transfer job, call the IBackgroundCopyJob Complete method.
ms.assetid: 8f96ed59-b038-4047-bea4-c63b9e84c209
keywords:
- transfer job BITS , canceling
- canceling a job BITS
- transfer job BITS , completing
- completing a job BITS
ms.topic: article
ms.date: 05/31/2018
---

# Completing and Canceling a Job

To complete a transfer job, call the [**IBackgroundCopyJob::Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method. For download jobs, you can call the **Complete** method before all files in the job have been transferred (before the job's state is BG\_JOB\_STATE\_TRANSFERRED). Only those files that BITS successfully transferred to the client before you called the **Complete** method are available to the user.

For upload jobs, call the [**Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method only if the job's state is BG\_JOB\_STATE\_TRANSFERRED. To determine when the job's state is BG\_JOB\_STATE\_TRANSFERRED, [poll](polling-for-the-status-of-the-job.md) the job's state property or register to receive BG\_NOTIFY\_JOB\_TRANSFERRED [event notification](registering-a-com-callback.md).

To cancel a transfer job, call the [**IBackgroundCopyJob::Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel) method. The **Cancel** method removes the job from the transfer queue and removes the temporary files from the client. Typically, you call this method if you are unable to resolve an error associated with the job.

The [**Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel) method cancels an upload if the upload is not complete. If the upload is complete, and the job is of type BG\_JOB\_TYPE\_UPLOAD\_REPLY, the method cancels the reply.

If you do not call the [**Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method or the [**IBackgroundCopyJob::Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel) method within 90 days (default [JobInactivityTimeout](group-policies.md) Group Policy), the service cancels the job. If the service cancels the job, the downloaded files and the reply file are not available to the client; job cancellation does not affect files that have been successfully uploaded. You should always call the **Complete** or the **Cancel** method and not rely on the JobInactivityTimeout policy to cleanup your jobs. Jobs left in the queue may prevent users from creating other jobs if the MaxJobsPerUser or MaxJobsPerMachine policy limit is reached.

 

 




