---
Description: This topic describes how to send a fax document to multiple recipients in the Microsoft Win32 environment.
ms.assetid: 2e7849a9-de99-48e8-b0a3-1b8883976131
title: Broadcasting a Fax to Multiple Recipients
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Broadcasting a Fax to Multiple Recipients

> [!Note]  
> To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function multiple times. The [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function is supported for backward compatibility.

 

> [!Note]  
> This functionality is available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

 

The [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function queues several fax jobs that will transmit the same outgoing fax transmission to multiple recipients, from a file stored on disk. The application must specify one file to transmit.

The [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function calls the [**FAX\_RECIPIENT\_CALLBACK**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_recipient_callbacka) function multiple times, once for each designated fax recipient. **FAX\_RECIPIENT\_CALLBACK** retrieves information to queue the transmission, and cover page information if a cover page is required.

Call the [**FaxCompleteJobParams**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxcompletejobparamsa) function before calling the [**FAX\_RECIPIENT\_CALLBACK**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_recipient_callbacka) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_coverpage_infoa) and [**FAX\_JOB\_PARAM**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_parama) structures. Call the [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function to free the memory associated with these structures.

Note that an application must first call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function to obtain a fax server handle before calling the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function and the [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function.

 

 



