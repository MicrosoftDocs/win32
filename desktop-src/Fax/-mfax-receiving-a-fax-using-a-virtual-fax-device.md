---
Description: When the fax service calls FaxDevVirtualDeviceCreation the service specifies a handle to an I/O completion port in the CompletionPort parameter and a value in the CompletionKey parameter.
ms.assetid: 353d0320-a690-43ec-a141-eaf1cca2fc71
title: Receiving a Fax Using a Virtual Fax Device
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Receiving a Fax Using a Virtual Fax Device

When the fax service calls [**FaxDevVirtualDeviceCreation**](-mfax-faxdevvirtualdevicecreation.md) the service specifies a handle to an I/O completion port in the *CompletionPort* parameter and a value in the *CompletionKey* parameter. The fax service provider (FSP) must use these values when the provider posts an I/O completion port packet to signal the fax service that the provider wants to receive a fax on the provider's virtual port. These values signal the fax service to call the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) function to initialize the fax job and then the [**FaxDevReceive**](-mfax-faxdevreceive.md) function. (This step is necessary because a virtual device does not have an associated telephony service provider (TSP) to generate ring events for the fax service.)

To receive an incoming fax using a virtual fax device, the FSP must perform the following steps.

## To receive a fax using a virtual fax device

1.  Export the [**FaxDevVirtualDeviceCreation**](-mfax-faxdevvirtualdevicecreation.md) function.
2.  Call the [PostQueuedCompletionStatus](http://msdn.microsoft.com/library/en-us/fileio/base/postqueuedcompletionstatus.asp) function to signal the fax service that the FSP wants to receive a fax. Use the *CompletionPort* parameter value and the *CompletionKey* parameter value the fax service specifies when the service calls the [**FaxDevVirtualDeviceCreation**](-mfax-faxdevvirtualdevicecreation.md) function. The completion port packet must be a [LINEMESSAGE](http://msdn.microsoft.com/library/en-us/tapi/tapi2/linemessage_str.asp) structure.
3.  Respond appropriately when the fax service calls the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) function.
4.  Respond appropriately when the fax service calls the [**FaxDevReceive**](-mfax-faxdevreceive.md) function.
5.  Continue to call the [PostQueuedCompletionStatus](http://msdn.microsoft.com/library/en-us/fileio/base/postqueuedcompletionstatus.asp) function, to receive messages and to post status updates, until the fax service calls the [**FaxDevEndJob**](-mfax-faxdevendjob.md) function. Specify the *CompletionPort* parameter value and the *CompletionKey* parameter value the fax service specifies when the service calls the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) function. The completion port packet must be a [**FAX\_DEV\_STATUS**](-mfax-fax-dev-status-str.md) structure.

For more information about setting the members of the [LINEMESSAGE](http://msdn.microsoft.com/library/en-us/tapi/tapi2/linemessage_str.asp) structure and about allocating memory for the structure, see [**FaxDevVirtualDeviceCreation**](-mfax-faxdevvirtualdevicecreation.md).

 

 



