---
title: BITS Interfaces
description: Use the following Background Intelligent Transfer Service (BITS) interfaces to transfer files and monitor jobs within the transfer queue.
ms.assetid: '72668c9b-e6f3-4f3f-9d4b-50d930d1889d'
---

# BITS Interfaces

Use the following Background Intelligent Transfer Service (BITS) interfaces to [transfer files and monitor jobs](using-bits.md) within the transfer queue.



| Interface                                                              | Description                                                                                                                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IBackgroundCopyCallback**](ibackgroundcopycallback.md)             | Clients implement the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface to receive notification that a job is complete, has been modified, or is in error.                       |
| [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md)           | Clients implement the [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md) interface to receive notification that a file has completed downloading.                                         |
| [**IBackgroundCopyCallback3**](ibackgroundcopycallback3.md)           | Clients implement the [**IBackgroundCopyCallback3**](ibackgroundcopycallback3.md) interface to receive notification that ranges of a file have completed downloading.                              |
| [**IBackgroundCopyError**](ibackgroundcopyerror.md)                   | Retrieves details of a job error.                                                                                                                                                                   |
| [**IBackgroundCopyFile**](ibackgroundcopyfile.md)                     | Retrieves the local and remote file names of a file transfer request in the job and its progress.                                                                                                   |
| [**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)                   | Specifies a new remote name for the file and retrieves the list of ranges to download.                                                                                                              |
| [**IBackgroundCopyFile3**](ibackgroundcopyfile3.md)                   | Validates the file so that peers can request its content and retrieves the name of the temporary file.                                                                                              |
| [**IBackgroundCopyFile4**](ibackgroundcopyfile4.md)                   | Retrieves download statistics for peers and origin servers.                                                                                                                                         |
| [**IBackgroundCopyFile5**](ibackgroundcopyfile5.md)                   | Provides generic property get and set methods for BackgroundCopyFile properties.                                                                                                                    |
| [**IBackgroundCopyFile6**](ibackgroundcopyfile6.md)                   | Gets or sets generic properties of BITS file transfers.                                                                                                                                             |
| [**IBackgroundCopyJob**](ibackgroundcopyjob.md)                       | Adds files to the job, sets the priority level of the job, determines the state of the job, and starts and stops the job.                                                                           |
| [**IBackgroundCopyJob2**](ibackgroundcopyjob2.md)                     | Retrieves reply data from an upload job, determines the progress of the reply data transfer to the client, requests command line execution, and provides credentials for a proxy and remote server. |
| [**IBackgroundCopyJob3**](ibackgroundcopyjob3.md)                     | Downloads ranges of a file, changes the prefix of a remote file name, and maintains the owner and ACL information with the file.                                                                    |
| [**IBackgroundCopyJob4**](ibackgroundcopyjob4.md)                     | Enables peer caching, restrict download time, and inspect user token characteristics.                                                                                                               |
| [**IBackgroundCopyJob5**](bits5-functions.md)                         | Queries or sets several optional behaviors of a job.                                                                                                                                                |
| [**IBackgroundCopyJobHttpOptions**](ibackgroundcopyjobhttpoptions.md) | Specifies client certificates for certificate-based client authentication and custom headers for HTTP requests.                                                                                     |
| [**IBackgroundCopyManager**](ibackgroundcopymanager.md)               | Creates transfer jobs, retrieves an enumerator object of jobs in the queue, and retrieves individual jobs from the queue.                                                                           |
| [**IBitsPeer**](ibitspeer.md)                                         | Gets information about a peer in the neighborhood.                                                                                                                                                  |
| [**IBitsPeerCacheAdministration**](ibitspeercacheadministration.md)   | Manage the pool of peers from which you can download content.                                                                                                                                       |
| [**IBitsPeerCacheRecord**](ibitspeercacherecord.md)                   | Gets information about a file in the cache.                                                                                                                                                         |
| [**IBitsTokenOptions**](ibitstokenoptions.md)                         | Associates and manages a pair of security tokens for a Background Intelligent Transfer Service (BITS) transfer job.                                                                                 |
| [**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles.md)           | Enumerates files in the job.                                                                                                                                                                        |
| [**IEnumBackgroundCopyJobs**](ienumbackgroundcopyjobs.md)             | Enumerates jobs in the transfer queue.                                                                                                                                                              |
| [**IEnumBitsPeerCacheRecords**](ienumbitspeercacherecords.md)         | Enumerates the records of the cache.                                                                                                                                                                |
| [**IEnumBitsPeers**](ienumbitspeers.md)                               | Enumerates the list of peers that BITS has discovered.                                                                                                                                              |



 

 

 




