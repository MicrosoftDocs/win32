---
Description: 'This topic describes how to query fax jobs.'
ms.assetid: '12bc1375-6312-4fea-b28e-21224e4952f4'
title: Querying Fax Jobs
---

# Querying Fax Jobs

A fax client application can query the fax number related to a fax job, and fax recipient and sender information. You can also retrieve a job's type, status, and unique identifier; scheduling and billing information; and the transmission's page count.

## In the Win32 Environment

The [**FaxEnumJobs**](-mfax-faxenumjobs.md) function permits a fax client application to retrieve a list of the jobs in the fax job queue on a specified fax server. Call the [**FaxGetJob**](-mfax-faxgetjob.md) function to query an individual fax job. Both functions return detailed information for the jobs in [**FAX\_JOB\_ENTRY**](-mfax-fax-job-entry-str.md) structures, one job per structure.

Because the [**FaxGetJob**](-mfax-faxgetjob.md) function and the [**FaxEnumJobs**](-mfax-faxenumjobs.md) function allocate the memory required for [**FAX\_JOB\_ENTRY**](-mfax-fax-job-entry-str.md) structures, the application must call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate the resources.

Note that an application must call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxEnumJobs**](-mfax-faxenumjobs.md) and [**FaxGetJob**](-mfax-faxgetjob.md) functions.

## In the COM Implementation Environment

If you are writing a C/C++ application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can call [**IFaxJob**](-mfax-ifaxjob.md) interface methods to query the properties of the job. For information about the steps required to create a FaxJob object, and for a list of properties and methods, see **IFaxJob**.

If you are writing a Microsoft Visual Basic application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can retrieve multiple properties of the object. See [**FaxJob object (Visual Basic)**](-mfax-faxjob-object-visual-basic-.md) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



