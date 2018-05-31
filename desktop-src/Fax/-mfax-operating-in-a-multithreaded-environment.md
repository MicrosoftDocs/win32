---
Description: The fax service calls FaxDevStartJob at the beginning of a new fax job and once for each fax operation, because each operation executes in a separate thread. Fax service providers (FSPs) must function in a multithreaded environment.
ms.assetid: af0e3837-5fcb-43da-a951-70b70a9722b1
title: Operating in a Multithreaded Environment
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Operating in a Multithreaded Environment

The fax service calls [**FaxDevStartJob**](-mfax-faxdevstartjob.md) at the beginning of a new fax job and once for each fax operation, because each operation executes in a separate thread. Fax service providers (FSPs) must function in a multithreaded environment.

The FSP must allocate memory for the job-specific instance data for each fax operation thread to ensure that the FSP DLL is thread-safe. The FSP should also deallocate memory for the instance data when the fax operation finishes. For more information, see [Multiple Threads](http://msdn.microsoft.com/library/en-us/dllproc/base/multiple_threads.asp).

 

 



