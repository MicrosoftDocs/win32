---
Description: To close a fax job gracefully after all fax operations have completed, the fax service calls the FaxDevEndJob function.
ms.assetid: 15b7fdcd-d939-4f70-90bc-5f7684fc0fda
title: Terminating a Fax
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Terminating a Fax

To close a fax job gracefully after all fax operations have completed, the fax service calls the [**FaxDevEndJob**](-mfax-faxdevendjob.md) function. At this time, the fax service provider (FSP) should deallocate any job-specific instance data that was allocated by the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) function during job initialization.

The fax service calls the [**FaxDevAbortOperation**](-mfax-faxdevabortoperation.md) function asynchronously to request that an FSP terminate a send or receive fax operation that is still active. **FaxDevAbortOperation** should post the termination request and return immediately. Even if **FaxDevAbortOperation** terminates an operation, the fax service still calls the [**FaxDevEndJob**](-mfax-faxdevendjob.md) function.

The FSP must export both the [**FaxDevEndJob**](-mfax-faxdevendjob.md) and [**FaxDevAbortOperation**](-mfax-faxdevabortoperation.md) functions.

 

 



