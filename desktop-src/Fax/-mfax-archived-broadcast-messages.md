---
Description: When a user sends the same fax to multiple recipients (broadcasts a fax), the fax service creates a unique job in the job queue for each of the recipients.
ms.assetid: c0075ad5-187c-4b46-9461-1c4546497a0f
title: Archived Broadcast Messages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Archived Broadcast Messages

When a user sends the same fax to multiple recipients (broadcasts a fax), the fax service creates a unique job in the job queue for each of the recipients. However, the fax service assigns the same broadcast ID (called the [**submission ID**](/windows/previous-versions/FaxComex/?branch=master) in the extended Component Object Model (COM) API) to each of the jobs in the broadcast, with which the service can group the jobs. The fax service uses the broadcast ID to determine when to archive fax messages.

The fax service creates a copy of the individual recipient job in the archive for each job that reaches a successful final state. All jobs with the same broadcast ID remain in the job queue until all the jobs with that broadcast ID reach a final state, whether successful or not. When all of the jobs reach a final state, successful jobs are deleted from the queue and remain in the archive. Unsuccessful jobs remain in the queue for the number of days specified in the [**AgeLimit**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxoutgoingqueue-get_agelimit?branch=master) property of the [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object (in Windows Vista, [**IFaxConfiguration:OutgoingQueueAgeLimit**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_outgoingqueueagelimit?branch=master)), and are then deleted. You can restart the failed jobs using the [**IFaxOutgoingJob::Restart**](/windows/previous-versions/FaxComex/?branch=master) method, as long as the jobs are still in the queue.

For example, consider a partially completed broadcast with 50 recipients. So far, only 35 of the 50 jobs have completed successfully. Three other jobs have reached a final error state because the jobs received a continuous busy signal. The fax service is still attempting to send the remaining 12 jobs. All 50 jobs are still in the job queue, and copies of the successful jobs are in the archive. Only when all 50 jobs reach a final state will the fax service remove the successful jobs from the queue. When the value of the [**AgeLimit**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxoutgoingqueue-get_agelimit?branch=master) property is exceeded, the fax service will remove the failed jobs from the queue.

## Related topics

<dl> <dt>

[Fax Broadcasts](-mfax-fax-broadcasts.md)
</dt> </dl>

 

 



