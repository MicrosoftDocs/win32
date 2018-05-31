---
Description: This topic describes how to modify a fax job.
ms.assetid: 8bcfa999-85d8-43f1-a7f1-59d5a824376a
title: Modifying a Fax Job
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying a Fax Job

A fax client application cannot modify the attributes or properties of a fax transmission after the job has been queued. For more information about terminating and pausing a job, see [Terminating a Fax Job](-mfax-terminating-a-fax-job.md).

## In the Win32 Environment

A fax client application cannot change the attributes of a fax job after the job has been queued. This is because many of the attributes contained in the [**FAX\_JOB\_ENTRY**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_entrya) structure associated with the job cannot change after document transmission begins.

To pause, resume, cancel, or restart a queued fax job, an application can call the [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba) function.

Note that an application must first call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function to obtain a fax server handle before calling the [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba) function.

## In the COM Implementation Environment

If you are writing a C/C++ application, after you create a [FaxJob](-mfax-faxjob.md) object you can call the [**IFaxJob::SetStatus**](/previous-versions/windows/desktop/api/Faxcom/) method to pause, resume, cancel, or restart the job.

If you are writing a Microsoft Visual Basic application, after you create a [FaxJob](-mfax-faxjob.md) object you can call the [**SetStatus**](/previous-versions/windows/desktop/api/Faxcom/) method of the object to pause, resume, cancel, or restart the job.

 

 



