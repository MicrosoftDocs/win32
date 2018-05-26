---
title: BITS Interfaces
description: Use the following Background Intelligent Transfer Service (BITS) interfaces to transfer files and monitor jobs within the transfer queue.
ms.assetid: 72668c9b-e6f3-4f3f-9d4b-50d930d1889d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BITS Interfaces

Use the following Background Intelligent Transfer Service (BITS) interfaces to [transfer files and monitor jobs](using-bits.md) within the transfer queue.



| Interface                                                              | Description                                                                                                                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IBackgroundCopyCallback**](/windows/win32/Bits/nn-bits-ibackgroundcopycallback?branch=master)             | Clients implement the [**IBackgroundCopyCallback**](/windows/win32/Bits/nn-bits-ibackgroundcopycallback?branch=master) interface to receive notification that a job is complete, has been modified, or is in error.                       |
| [**IBackgroundCopyCallback2**](/windows/win32/Bits3_0/nn-bits3_0-ibackgroundcopycallback2?branch=master)           | Clients implement the [**IBackgroundCopyCallback2**](/windows/win32/Bits3_0/nn-bits3_0-ibackgroundcopycallback2?branch=master) interface to receive notification that a file has completed downloading.                                         |
| [**IBackgroundCopyCallback3**](/windows/win32/Bits10_1/nn-bits10_1-ibackgroundcopycallback3?branch=master)           | Clients implement the [**IBackgroundCopyCallback3**](/windows/win32/Bits10_1/nn-bits10_1-ibackgroundcopycallback3?branch=master) interface to receive notification that ranges of a file have completed downloading.                              |
| [**IBackgroundCopyError**](/windows/win32/Bits/nn-bits-ibackgroundcopyerror?branch=master)                   | Retrieves details of a job error.                                                                                                                                                                   |
| [**IBackgroundCopyFile**](/windows/win32/Bits/nn-bits-ibackgroundcopyfile?branch=master)                     | Retrieves the local and remote file names of a file transfer request in the job and its progress.                                                                                                   |
| [**IBackgroundCopyFile2**](/windows/win32/Bits2_0/nn-bits2_0-ibackgroundcopyfile2?branch=master)                   | Specifies a new remote name for the file and retrieves the list of ranges to download.                                                                                                              |
| [**IBackgroundCopyFile3**](/windows/win32/Bits3_0/nn-bits3_0-ibackgroundcopyfile3?branch=master)                   | Validates the file so that peers can request its content and retrieves the name of the temporary file.                                                                                              |
| [**IBackgroundCopyFile4**](/windows/win32/Bits4_0/nn-bits4_0-ibackgroundcopyfile4?branch=master)                   | Retrieves download statistics for peers and origin servers.                                                                                                                                         |
| [**IBackgroundCopyFile5**](/windows/win32/Bits5_0/nn-bits5_0-ibackgroundcopyfile5?branch=master)                   | Provides generic property get and set methods for BackgroundCopyFile properties.                                                                                                                    |
| [**IBackgroundCopyFile6**](/windows/win32/bits10_1/nn-bits10_1-ibackgroundcopyfile6?branch=master)                   | Gets or sets generic properties of BITS file transfers.                                                                                                                                             |
| [**IBackgroundCopyJob**](/windows/win32/Bits/nn-bits-ibackgroundcopyjob?branch=master)                       | Adds files to the job, sets the priority level of the job, determines the state of the job, and starts and stops the job.                                                                           |
| [**IBackgroundCopyJob2**](/windows/win32/Bits1_5/nn-bits1_5-ibackgroundcopyjob2?branch=master)                     | Retrieves reply data from an upload job, determines the progress of the reply data transfer to the client, requests command line execution, and provides credentials for a proxy and remote server. |
| [**IBackgroundCopyJob3**](/windows/win32/Bits2_0/nn-bits2_0-ibackgroundcopyjob3?branch=master)                     | Downloads ranges of a file, changes the prefix of a remote file name, and maintains the owner and ACL information with the file.                                                                    |
| [**IBackgroundCopyJob4**](/windows/win32/Bits3_0/nn-bits3_0-ibackgroundcopyjob4?branch=master)                     | Enables peer caching, restrict download time, and inspect user token characteristics.                                                                                                               |
| [**IBackgroundCopyJob5**](/windows/win32/Bits5_0/nn-bits5_0-ibackgroundcopyjob5?branch=master)                         | Queries or sets several optional behaviors of a job.                                                                                                                                                |
| [**IBackgroundCopyJobHttpOptions**](/windows/win32/Bits2_5/nn-bits2_5-ibackgroundcopyjobhttpoptions?branch=master) | Specifies client certificates for certificate-based client authentication and custom headers for HTTP requests.                                                                                     |
| [**IBackgroundCopyManager**](/windows/win32/Bits/nn-bits-ibackgroundcopymanager?branch=master)               | Creates transfer jobs, retrieves an enumerator object of jobs in the queue, and retrieves individual jobs from the queue.                                                                           |
| [**IBitsPeer**](/windows/win32/Bits3_0/nn-bits3_0-ibitspeer?branch=master)                                         | Gets information about a peer in the neighborhood.                                                                                                                                                  |
| [**IBitsPeerCacheAdministration**](/windows/win32/Bits3_0/nn-bits3_0-ibitspeercacheadministration?branch=master)   | Manage the pool of peers from which you can download content.                                                                                                                                       |
| [**IBitsPeerCacheRecord**](/windows/win32/Bits3_0/nn-bits3_0-ibitspeercacherecord?branch=master)                   | Gets information about a file in the cache.                                                                                                                                                         |
| [**IBitsTokenOptions**](/windows/win32/Bits4_0/nn-bits4_0-ibitstokenoptions?branch=master)                         | Associates and manages a pair of security tokens for a Background Intelligent Transfer Service (BITS) transfer job.                                                                                 |
| [**IEnumBackgroundCopyFiles**](/windows/win32/Bits/nn-bits-ienumbackgroundcopyfiles?branch=master)           | Enumerates files in the job.                                                                                                                                                                        |
| [**IEnumBackgroundCopyJobs**](/windows/win32/Bits/nn-bits-ienumbackgroundcopyjobs?branch=master)             | Enumerates jobs in the transfer queue.                                                                                                                                                              |
| [**IEnumBitsPeerCacheRecords**](/windows/win32/Bits3_0/nn-bits3_0-ienumbitspeercacherecords?branch=master)         | Enumerates the records of the cache.                                                                                                                                                                |
| [**IEnumBitsPeers**](/windows/win32/Bits3_0/nn-bits3_0-ienumbitspeers?branch=master)                               | Enumerates the list of peers that BITS has discovered.                                                                                                                                              |



 

 

 




