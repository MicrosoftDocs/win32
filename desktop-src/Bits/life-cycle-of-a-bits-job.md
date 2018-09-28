---
title: Life Cycle of a BITS Job
description: The life cycle of a BITS job begins when you create a job.
ms.assetid: b765a8ef-74bd-475e-9cd9-e9e2cf4f0305
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Life Cycle of a BITS Job

The life cycle of a BITS job begins when you create a job. A job is a container that contains one or more files to transfer. A job also has properties that specify how BITS transfers the files and interacts with your application. For example, you can specify the priority of the job, whether the job is an upload or download job, and for which events you want to receive notification.

After you create the job, add one or more files (upload jobs can contain only one file) to the job and change any of the property values as appropriate for your application. When you add a file to the job, specify both the local (client) and remote (server) name of the file. The remote file name must use the HTTP, HTTPS, or SMB protocol. Files within a job are processed sequentially (first in, first out).

BITS automatically suspends jobs when they are created. You must resume the job to activate it in the transfer queue. You can suspend or resume a job at any time. Resuming the job moves the job from the suspended state to the queued state. The job stays in the queued state until the scheduler determines it is the job's turn to transfer files. All foreground jobs run concurrently with one background job. BITS processes the files within foreground jobs serially.

When it is a job's turn to transfer files, the job moves to the connecting state while BITS connects to the remote server (specified in the remote file name). If BITS is able to connect to the remote server, the job moves to the transferring state where it stays until its time slice ends, the transfer is complete, an error occurs, or the application suspends the job.

The job moves between the queued, connecting, and transferring states until BITS transfers all files in the job. At that point, the job moves to the transferred state. BITS uses round-robin scheduling to schedule jobs that are at the same priority level. Each job is given a slice of time to process its files. If the job does not complete during its time slice, the job goes back to the queued state and the next job in the queue is activated. This prevents large jobs from blocking smaller jobs. Jobs are processed largely on a first in, first out (FIFO) basis; however, BITS cannot guarantee FIFO processing because of round-robin scheduling, job errors, and service restarts.

The transferred files are not available to the client until the application calls the [**IBackgroundCopyJob::Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method to transfer ownership of the files from BITS to the user. Upload jobs are also set to the transferred state when the file is successfully received by the server. Upload-reply jobs are set to the transferred state after the file is successfully sent to the server and the reply from the server application is successfully transferred to the client.

If an error occurs, the job moves to either the fatal or transient error state. Fatal errors are errors that BITS cannot recover from or which require intervention to fix. If the application is able to fix the error, the application resumes the job and BITS moves the job to the queued state. Transient errors are errors that may resolve themselves. BITS retries jobs in the transient error state until the transfer is successful or the job times out. The job times out when no progress is made within an application-specified period. If the job times out, BITS moves the job to fatal error state.

For more information on job states, see [**BG\_JOB\_STATE**](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0002).

 

 




