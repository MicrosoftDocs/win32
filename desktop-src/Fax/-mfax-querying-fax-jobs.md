---
Description: This topic describes how to query fax jobs.
ms.assetid: 12bc1375-6312-4fea-b28e-21224e4952f4
title: Querying Fax Jobs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying Fax Jobs

A fax client application can query the fax number related to a fax job, and fax recipient and sender information. You can also retrieve a job's type, status, and unique identifier; scheduling and billing information; and the transmission's page count.

## In the Win32 Environment

The [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master) function permits a fax client application to retrieve a list of the jobs in the fax job queue on a specified fax server. Call the [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master) function to query an individual fax job. Both functions return detailed information for the jobs in [**FAX\_JOB\_ENTRY**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_entrya?branch=master) structures, one job per structure.

Because the [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master) function and the [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master) function allocate the memory required for [**FAX\_JOB\_ENTRY**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_entrya?branch=master) structures, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate the resources.

Note that an application must call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master) and [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master) functions.

## In the COM Implementation Environment

If you are writing a C/C++ application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can call [**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master) interface methods to query the properties of the job. For information about the steps required to create a FaxJob object, and for a list of properties and methods, see **IFaxJob**.

If you are writing a Microsoft Visual Basic application, after you create a [FaxJob](-mfax-faxjob.md) object for a specified fax job, you can retrieve multiple properties of the object. See [**FaxJob object (Visual Basic)**](-mfax-faxjob-object-visual-basic-.md) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



