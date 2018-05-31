---
Description: This topic describes how to query fax jobs.
ms.assetid: 12bc1375-6312-4fea-b28e-21224e4952f4
title: Querying Fax Jobs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Fax Jobs

A fax client application can query the fax number related to a fax job, and fax recipient and sender information. You can also retrieve a job's type, status, and unique identifier; scheduling and billing information; and the transmission's page count.

## In the Win32 Environment

The [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa) function permits a fax client application to retrieve a list of the jobs in the fax job queue on a specified fax server. Call the [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba) function to query an individual fax job. Both functions return detailed information for the jobs in [**FAX\_JOB\_ENTRY**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_entrya) structures, one job per structure.

Because the [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba) function and the [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa) function allocate the memory required for [**FAX\_JOB\_ENTRY**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_entrya) structures, the application must call the [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function to deallocate the resources.

Note that an application must call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function to obtain a fax server handle before calling the [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa) and [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba) functions.

## In the COM Implementation Environment

If you are writing a C/C++ application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can call [**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob) interface methods to query the properties of the job. For information about the steps required to create a FaxJob object, and for a list of properties and methods, see **IFaxJob**.

If you are writing a Microsoft Visual Basic application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can retrieve multiple properties of the object. See [**FaxJob object (Visual Basic)**](-mfax-faxjob-object-visual-basic-.md) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



