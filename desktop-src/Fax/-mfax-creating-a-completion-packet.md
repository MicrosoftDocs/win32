---
Description: The sample code in this topic illustrates the procedure for creating an I/O completion packet and posting the packet to the fax service.
ms.assetid: d9a99db4-d8f1-4951-8f12-da743c03487f
title: Creating a Completion Packet
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Completion Packet

The sample code in this topic illustrates the procedure for creating an I/O completion packet and posting the packet to the fax service. Fax service providers (FSPs) must post I/O completion packets, in the form of a [**FAX\_DEV\_STATUS**](/previous-versions/windows/desktop/api/FaxDev/ns-faxdev-_fax_dev_status) structure, to the fax service when the provider changes its status.

First, the sample computes the size required for the [**FAX\_DEV\_STATUS**](/previous-versions/windows/desktop/api/FaxDev/ns-faxdev-_fax_dev_status) structure. It calls the [HeapAlloc](http://msdn.microsoft.com/library/en-us/memory/base/heapalloc.asp) function to allocate the memory for the structure from the heap specified by the *HeapHandle* parameter of the [**FaxDevInitialize**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevinitialize) function. Then the sample assigns values to the members in the structure. Finally, the example calls the [PostQueuedCompletionStatus](http://msdn.microsoft.com/library/en-us/fileio/base/postqueuedcompletionstatus.asp) function, using the *CompletionPortHandle* and *CompletionKey* parameters specified in the [**FaxDevStartJob**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevstartjob) function, to post the completion packet.


```
BOOL rVal;
DWORD StatusSize;
PFAX_DEV_STATUS FaxStatus;
 
 
//
// Compute the size of the status structure. 
//
 
StatusSize = sizeof(FAX_DEV_STATUS);
 
//
// Allocate memory for the status structure. 
//
 
FaxStatus = (PFAX_DEV_STATUS) HeapAlloc( HeapHandle, 
                                         HEAP_ZERO_MEMORY, 
                                         StatusSize );
if (!FaxStatus) {
    //
    // Process some errors. 
    //
}
 
//
// Assign values to the status structure. 
//
 
FaxStatus->SizeOfStruct     = sizeof(FAX_DEV_STATUS);
FaxStatus->StatusId         = 0;
FaxStatus->StringId         = 0;
FaxStatus->PageCount        = 0;
FaxStatus->CSI              = NULL;
FaxStatus->CallerId         = NULL;
FaxStatus->RoutingInfo      = NULL;
FaxStatus->ErrorCode        = 0;
 
//
// Post the packet to the fax service. 
//
 
rVal = PostQueuedCompletionStatus(
    CompletionPortHandle,             // from FaxDevStartJob
    sizeof(FAX_DEV_STATUS),
    CompletionKey,                    // from FaxDevStartJob
    (LPOVERLAPPED) FaxStatus
    );
if (!rVal) {
    //
    // Process some errors. 
    //
}
```



 

 



