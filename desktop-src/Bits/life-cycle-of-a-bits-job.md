---
title: Life Cycle of a BITS Job
description: The life cycle of a BITS job begins when you create a job.
ms.assetid: b765a8ef-74bd-475e-9cd9-e9e2cf4f0305
ms.topic: article
ms.date: 11/13/2018
---


# BITS Job states
There are four classes of BITS [**states**](/windows/desktop/api/Bits/ne-bits-bg_job_state): starting, action, transferred, and final. As a job runs, it transitions between states in the different state classes. Once a job is in a final state, it won't move out of the final state and won't show up in a [job enumeration](/windows/desktop/api/bits/nf-bits-ibackgroundcopymanager-enumjobs).

## State-changing methods
There are four state-changing methods on a job: [**Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel), [**Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete), [**Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume), and [**Suspend**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-suspend). As long as a job is not in a final state, you can call any of the state-changing methods. 

The [**Suspend**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-suspend) method is used to switch a job to the SUSPENDED state. When a job is suspended, all of its transfers will be stopped and won't resume until you call Resume.
A job that's already suspended will simply stay suspended.

The [**Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume) method is used to start a job that's suspended. Jobs in an error or transient error state will be set up to be retried. Jobs that are currently in an action state will stay in that state.

The [**Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel) method is used to cancel a job. The state will switch to cancelled. Any files currently being transferred will not be completed. All completely transferred and partially transferred files will be deleted.

The [**Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method will finish a transfer. Any fully downloaded files will be kept; files that are not fully transferred will be deleted.

You must call either Cancel or Complete to move your job to a final state and be cleaned up. Jobs that aren't transitioned to a final state will waste system resources. BITS will eventually automatically cancel old jobs. The default [JobInactivityTimeout](/windows/desktop/Bits/group-policies) is to cancel jobs after 90 days.


## Starting state 
The starting state is **SUSPENDED**. From here, you can add files to the job and set job and file properties. To start a job transferring, call Resume on the job. If you resume a job with no files, it will return a BG_E_EMPTY error code and the job will stay suspended.

## Action states
The **QUEUED**, **CONNECTING** and **TRANSFERRING** states show the current internal activity of your job. A job that's QUEUED is ready to be scheduled, possibly waiting for the BITS scheduler or waiting for the user to log in. A job that's CONNECTING is attempting to connect to the server to start transferring files. A job that's TRANSFERRING is actively uploading or downloading your files.

The **TRANSIENT ERROR** state means that the job tried and failed to transfer the file. This might be for network policy reasons; the job might be blocked because the current network is too expensive. It might also be blocked for system reasons like the system being in battery saver or game mode, or because there's no internet connectivity. 

Jobs in the transient error state will be retried automatically by BITS when appropriate. BITS includes a [MinimumRetryDelay](/windows/desktop/api/bits/nf-bits-ibackgroundcopyjob-setminimumretrydelay) and [NoProgressTimeout](/windows/desktop/api/bits/nf-bits-ibackgroundcopyjob-setnoprogresstimeout) value to control when a job is retried and when BITS will finally stop retrying.


## Transferred states
The transferred states happen when there's no more transferring to be done. You must either cancel or complete a job in this state. You may also add more files to transfer and call Resume(), but this isn't a common practice.

The **ERROR** state happens when a transfer is done (it won't be retried), but didn't fully succeed. All the files must be transferred to be successful; if any have permanently failed the job will be in error. You will typically either call Cancel or Complete to move the job to a final state. The practical difference is that when you call Cancel, any successfully transferred file will be deleted, but if you call Complete, any successfully transferred file will not be deleted.

Reasons for being in an ERROR state include 
* Staying too long in a TRANSIENT ERROR state (beyond the [NoProgressTimeout](/windows/desktop/api/bits/nf-bits-ibackgroundcopyjob-setnoprogresstimeout) setting).
* Getting a BG_E_TOKEN_REQUIRED error and needing assistance with [helper tokens](/windows/desktop/Bits/helper-tokens-for-bits-transfer-jobs)

It's a common practice to reconfigure an ERROR'd job and then call Resume to retry the job. For example, your app might need to update a file's remote name via [SetRemoteName](/windows/desktop/api/bits2_0/nf-bits2_0-ibackgroundcopyfile2-setremotename).

The **TRANSFERRED** state happens when a transfer is done and it succeeded. You must call Complete to finalize the job; for download jobs the downloaded files won't be available until after you call Complete. The exception to this rule is jobs which are the high performance jobs (and you should still call Complete).

## Final states
Once a job is in a final state, you can't call any of the state-changing methods. The job will be **ACKNOWLEDGED** after you call Complete() and all completed downloaded files will be available. The job will be **CANCELLED** after you call Cancel() and all downloaded files will be deleted. 


## Life Cycle of a BITS job

The life cycle of a BITS job begins when you create a job. A job is a container that contains one or more files to transfer. A job also has properties that specify how BITS transfers the files and interacts with your application. For example, you can specify the priority of the job, whether the job is an upload or download job, and for which events you want to receive notification.

After you create the job, add one or more files (upload jobs can contain only one file) to the job and change any of the property values as appropriate for your application. When you add a file to the job, specify both the local (client) and remote (server) name of the file. The remote file name must use the HTTP, HTTPS, or SMB protocol. Files within a job are processed sequentially (first in, first out).

BITS automatically suspends jobs when they are created. You must resume the job to activate it in the transfer queue. You can suspend or resume a job at any time. Resuming the job moves the job from the suspended state to the queued state. The job stays in the queued state until the scheduler determines it is the job's turn to transfer files. All foreground jobs run concurrently with one background job. BITS processes the files within foreground jobs serially.

When it is a job's turn to transfer files, the job moves to the connecting state while BITS connects to the remote server (specified in the remote file name). If BITS is able to connect to the remote server, the job moves to the transferring state where it stays until its time slice ends, the transfer is complete, an error occurs, or the application suspends the job.

The job moves between the queued, connecting, and transferring states until BITS transfers all files in the job. At that point, the job moves to the transferred state. BITS uses round-robin scheduling to schedule jobs that are at the same priority level. Each job is given a slice of time to process its files. If the job does not complete during its time slice, the job goes back to the queued state and the next job in the queue is activated. This prevents large jobs from blocking smaller jobs. Jobs are processed largely on a first in, first out (FIFO) basis; however, BITS cannot guarantee FIFO processing because of round-robin scheduling, job errors, and service restarts.

The transferred files are not available to the client until the application calls the [**IBackgroundCopyJob::Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method to transfer ownership of the files from BITS to the user. Upload jobs are also set to the transferred state when the file is successfully received by the server. Upload-reply jobs are set to the transferred state after the file is successfully sent to the server and the reply from the server application is successfully transferred to the client.

If an error occurs, the job moves to either the fatal or transient error state. Fatal errors are errors that BITS cannot recover from or which require intervention to fix. If the application is able to fix the error, the application resumes the job and BITS moves the job to the queued state. Transient errors are errors that may resolve themselves. BITS retries jobs in the transient error state until the transfer is successful or the job times out. The job times out when no progress is made within an application-specified period. If the job times out, BITS moves the job to fatal error state.

For more information on job states, see [**BG\_JOB\_STATE**](/windows/desktop/api/Bits/ne-bits-bg_job_state).
