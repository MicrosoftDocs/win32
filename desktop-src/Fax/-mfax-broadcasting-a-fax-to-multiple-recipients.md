---
Description: 'This topic describes how to send a fax document to multiple recipients in the Microsoft Win32 environment.'
ms.assetid: '2e7849a9-de99-48e8-b0a3-1b8883976131'
title: Broadcasting a Fax to Multiple Recipients
---

# Broadcasting a Fax to Multiple Recipients

> [!Note]  
> To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](-mfax-faxsenddocument.md) function multiple times. The [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function is supported for backward compatibility.

 

> [!Note]  
> This functionality is available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

 

The [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function queues several fax jobs that will transmit the same outgoing fax transmission to multiple recipients, from a file stored on disk. The application must specify one file to transmit.

The [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function calls the [**FAX\_RECIPIENT\_CALLBACK**](-mfax-fax-recipient-callback.md) function multiple times, once for each designated fax recipient. **FAX\_RECIPIENT\_CALLBACK** retrieves information to queue the transmission, and cover page information if a cover page is required.

Call the [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md) function before calling the [**FAX\_RECIPIENT\_CALLBACK**](-mfax-fax-recipient-callback.md) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](-mfax-fax-coverpage-info-str.md) and [**FAX\_JOB\_PARAM**](-mfax-fax-job-param-str.md) structures. Call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to free the memory associated with these structures.

Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxSendDocument**](-mfax-faxsenddocument.md) function and the [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function.

 

 



