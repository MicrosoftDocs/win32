---
Description: To close a fax job gracefully after all fax operations have completed, the fax service calls the FaxDevEndJob function.
ms.assetid: 15b7fdcd-d939-4f70-90bc-5f7684fc0fda
title: Terminating a Fax
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Terminating a Fax

To close a fax job gracefully after all fax operations have completed, the fax service calls the [**FaxDevEndJob**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevendjob?branch=master) function. At this time, the fax service provider (FSP) should deallocate any job-specific instance data that was allocated by the [**FaxDevStartJob**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevstartjob?branch=master) function during job initialization.

The fax service calls the [**FaxDevAbortOperation**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevabortoperation?branch=master) function asynchronously to request that an FSP terminate a send or receive fax operation that is still active. **FaxDevAbortOperation** should post the termination request and return immediately. Even if **FaxDevAbortOperation** terminates an operation, the fax service still calls the [**FaxDevEndJob**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevendjob?branch=master) function.

The FSP must export both the [**FaxDevEndJob**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevendjob?branch=master) and [**FaxDevAbortOperation**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevabortoperation?branch=master) functions.

 

 



