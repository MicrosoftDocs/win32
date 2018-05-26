---
Description: This topic describes how to terminate a fax transmission that is in progress.
ms.assetid: b957ed68-3e48-4c97-8c7c-3329a52f41bb
title: Terminating a Fax Job
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Terminating a Fax Job

A fax client application can terminate a fax transmission that is in progress. For more information about changing the status of a fax job, see [Modifying a Fax Job](-mfax-modifying-a-fax-job.md).

## In the Win32 Environment

A fax client application can call the [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master) function or the [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master) function to cancel a fax transmission that is in progress.

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master) function or the [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master) function.

## In the COM Implementation Environment

If you are writing a C/C++ application, after you create a [FaxJob](-mfax-faxjob.md) object you can call the [**IFaxJob::SetStatus**](/windows/previous-versions/Faxcom/?branch=master) method to terminate the fax job. You must specify JC\_DELETE in the *Command* parameter.

If you are writing a Microsoft Visual Basic application, after you create a [FaxJob](-mfax-faxjob.md) object you can call the [**SetStatus**](/windows/previous-versions/Faxcom/?branch=master) method of the object to cancel the fax job by specifying the constant JC\_DELETE. Note that you must define this constant.

 

 



