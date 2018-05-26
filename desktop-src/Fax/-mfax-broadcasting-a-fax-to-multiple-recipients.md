---
Description: This topic describes how to send a fax document to multiple recipients in the Microsoft Win32 environment.
ms.assetid: 2e7849a9-de99-48e8-b0a3-1b8883976131
title: Broadcasting a Fax to Multiple Recipients
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Broadcasting a Fax to Multiple Recipients

> [!Note]  
> To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function multiple times. The [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function is supported for backward compatibility.

 

> [!Note]  
> This functionality is available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

 

The [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function queues several fax jobs that will transmit the same outgoing fax transmission to multiple recipients, from a file stored on disk. The application must specify one file to transmit.

The [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function calls the [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master) function multiple times, once for each designated fax recipient. **FAX\_RECIPIENT\_CALLBACK** retrieves information to queue the transmission, and cover page information if a cover page is required.

Call the [**FaxCompleteJobParams**](/windows/previous-versions/Winfax/nf-winfax-faxcompletejobparamsa?branch=master) function before calling the [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) and [**FAX\_JOB\_PARAM**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_parama?branch=master) structures. Call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to free the memory associated with these structures.

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function and the [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function.

 

 



