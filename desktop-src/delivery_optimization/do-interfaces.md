---
title: Delivery Optimization Interfaces
description: Use the following Delivery Optimization interfaces to transfer files and monitor jobs within the transfer queue.
ms.assetid: 20203CCD-86CC-4551-BA4F-0A5999F8C956
ms.topic: article
ms.date: 05/04/2022
---

# Delivery Optimization Interfaces

Use the following Delivery Optimization interfaces to transfer files and monitor jobs within the transfer queue.

| Interface | Description |
|-|-|
| [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) | Clients implement the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface to receive notification that a job is complete, has been modified, or is in error. |
| [**IBackgroundCopyError**](ibackgroundcopyerror.md) | Retrieves details of a job error. |
| [**IBackgroundCopyFile**](ibackgroundcopyfile.md) | Retrieves the local and remote file names of a file transfer request in the job and its progress. |
| [**IBackgroundCopyFile2**](ibackgroundcopyfile2.md) | Specifies a new remote name for the file and retrieves the list of ranges to download. |
| [**IBackgroundCopyFile5**](ibackgroundcopyfile5.md) | Provides generic property get and set methods for BackgroundCopyFile properties. |
| [**IBackgroundCopyJob**](ibackgroundcopyjob-.md) | Adds files to the job, sets the priority level of the job, determines the state of the job, and starts and stops the job. |
| [**IBackgroundCopyJob5**](ibackgroundcopyjob5.md) | Queries or sets several optional behaviors of a job. |
| [**IBackgroundCopyManager**](ibackgroundcopymanager.md) | Creates transfer jobs, retrieves an enumerator object of jobs in the queue, and retrieves individual jobs from the queue. |
| [**IDeliveryOptimizationJob**](ideliveryoptimizationjob.md) | Use to download ranges of a file. |
| [**IDeliveryOptimizationFile**](ideliveryoptimizationfile.md) | Use to identify the status of a specific file. |
| [**IDODownload**](/windows/win32/api/deliveryoptimization/nn-deliveryoptimization-idodownload) | Used to start and manage a download. |
| [**IDODownloadInternal**](./dodownloadinternal/nn-dodownloadinternal-idodownloadinternal.md) | Used to get or set extended download properties. |
| [**IDODownloadStatusCallback**](/windows/win32/api/deliveryoptimization/nn-deliveryoptimization-idodownloadstatuscallback) | Used to receive notifications about a download. |
| [**IDOManager**](/windows/win32/api/deliveryoptimization/nn-deliveryoptimization-idomanager) | Used to create a new download, and to enumerate existing downloads. |
| [**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md) | Enumerates files in the job. |
