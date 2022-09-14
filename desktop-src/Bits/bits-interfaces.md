---
title: BITS interfaces
description: Use the following Background Intelligent Transfer Service (BITS) interfaces to transfer files and monitor jobs within the transfer queue.
ms.assetid: 72668c9b-e6f3-4f3f-9d4b-50d930d1889d
ms.topic: article
ms.date: 01/08/2019
---

# BITS interfaces

Use the following Background Intelligent Transfer Service (BITS) interfaces to [transfer files and monitor jobs](using-bits.md) within the transfer queue.

| Interface | Description |
|-|-|
| [**IBackgroundCopyCallback**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopycallback) | Clients implement the [**IBackgroundCopyCallback**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopycallback) interface to receive notification that a job is complete, has been modified, or is in error. |
| [**IBackgroundCopyCallback2**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibackgroundcopycallback2) | Clients implement the [**IBackgroundCopyCallback2**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibackgroundcopycallback2) interface to receive notification that a file has completed downloading. |
| [**IBackgroundCopyCallback3**](/windows/desktop/api/Bits10_1/nn-bits10_1-ibackgroundcopycallback3) | Clients implement the [**IBackgroundCopyCallback3**](/windows/desktop/api/Bits10_1/nn-bits10_1-ibackgroundcopycallback3) interface to receive notification that ranges of a file have completed downloading. |
| [**IBackgroundCopyError**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyerror) | Retrieves details of a job error. |
| [**IBackgroundCopyFile**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyfile) | Retrieves the local and remote file names of a file transfer request in the job and its progress. |
| [**IBackgroundCopyFile2**](/windows/desktop/api/Bits2_0/nn-bits2_0-ibackgroundcopyfile2) | Specifies a new remote name for the file and retrieves the list of ranges to download. |
| [**IBackgroundCopyFile3**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibackgroundcopyfile3) | Validates the file so that peers can request its content and retrieves the name of the temporary file. |
| [**IBackgroundCopyFile4**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibackgroundcopyfile4) | Retrieves download statistics for peers and origin servers. |
| [**IBackgroundCopyFile5**](/windows/desktop/api/Bits5_0/nn-bits5_0-ibackgroundcopyfile5) | Provides generic property get and set methods for BackgroundCopyFile properties. |
| [**IBackgroundCopyFile6**](/windows/desktop/api/bits10_1/nn-bits10_1-ibackgroundcopyfile6) | Gets or sets generic properties of BITS file transfers. |
| [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) | Adds files to the job, sets the priority level of the job, determines the state of the job, and starts and stops the job. |
| [**IBackgroundCopyJob2**](/windows/desktop/api/Bits1_5/nn-bits1_5-ibackgroundcopyjob2) | Retrieves reply data from an upload job, determines the progress of the reply data transfer to the client, requests command line execution, and provides credentials for a proxy and remote server. |
| [**IBackgroundCopyJob3**](/windows/desktop/api/Bits2_0/nn-bits2_0-ibackgroundcopyjob3) | Downloads ranges of a file, changes the prefix of a remote file name, and maintains the owner and ACL information with the file. |
| [**IBackgroundCopyJob4**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibackgroundcopyjob4) | Enables peer caching, restrict download time, and inspect user token characteristics. |
| [**IBackgroundCopyJob5**](/windows/desktop/api/Bits5_0/nn-bits5_0-ibackgroundcopyjob5) | Queries or sets several optional behaviors of a job. |
| [**IBackgroundCopyJobHttpOptions**](/windows/desktop/api/Bits2_5/nn-bits2_5-ibackgroundcopyjobhttpoptions) | Specifies client certificates for certificate-based client authentication and custom headers for HTTP requests. |
| [**IBackgroundCopyJobHttpOptions2**](/windows/desktop/api/Bits10_2/nn-bits10_2-ibackgroundcopyjobhttpoptions2) | Use this interface to retrieve and/or to override the HTTP method used for a BITS transfer. |
| [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) | Creates transfer jobs, retrieves an enumerator object of jobs in the queue, and retrieves individual jobs from the queue. |
| [**IBitsPeer**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeer) | Gets information about a peer in the neighborhood. |
| [**IBitsPeerCacheAdministration**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeercacheadministration) | Manage the pool of peers from which you can download content. |
| [**IBitsPeerCacheRecord**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeercacherecord) | Gets information about a file in the cache. |
| [**IBitsTokenOptions**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibitstokenoptions) | Associates and manages a pair of security tokens for a Background Intelligent Transfer Service (BITS) transfer job. |
| [**IEnumBackgroundCopyFiles**](/windows/desktop/api/Bits/nn-bits-ienumbackgroundcopyfiles) | Enumerates files in the job. |
| [**IEnumBackgroundCopyJobs**](/windows/desktop/api/Bits/nn-bits-ienumbackgroundcopyjobs) | Enumerates jobs in the transfer queue. |
| [**IEnumBitsPeerCacheRecords**](/windows/desktop/api/Bits3_0/nn-bits3_0-ienumbitspeercacherecords) | Enumerates the records of the cache. |
| [**IEnumBitsPeers**](/windows/desktop/api/Bits3_0/nn-bits3_0-ienumbitspeers) | Enumerates the list of peers that BITS has discovered. |



 

 

 




