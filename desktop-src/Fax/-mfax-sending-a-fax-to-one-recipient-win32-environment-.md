---
Description: This topic describes how to send a fax to a recipient in the Microsoft Win32 environment.
ms.assetid: 99331570-b396-4ed8-b2f4-3db883be0130
title: Sending a Fax to One Recipient (Win32 Environment)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending a Fax to One Recipient (Win32 Environment)

A fax client application can call the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function to queue a job that will transmit an outgoing fax to one recipient, specifying a file stored on disk.

The application must specify one file to transmit and supply a pointer to a [**FAX\_JOB\_PARAM**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_parama) structure. The fax server queues the fax transmission job according to the details specified by the **FAX\_JOB\_PARAM** structure. The structure includes the recipient's fax number, sender and recipient data, an optional billing code, and job scheduling information.

The application must also supply a pointer to a [**FAX\_COVERPAGE\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_coverpage_infoa) structure if a cover page is required. This structure contains data to display on the cover page of a fax transmission. For more information, see [Sending a Cover Page](-mfax-sending-a-cover-page.md).

Call the [**FaxCompleteJobParams**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxcompletejobparamsa) function before calling the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_coverpage_infoa) and [**FAX\_JOB\_PARAM**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_parama) structures. Call the [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function to free the memory associated with these structures.

To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function multiple times. The [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function is supported for backward compatibility. Note that an application must first call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function to obtain a fax server handle before calling the **FaxSendDocument** function and the **FaxSendDocumentForBroadcast** function.

 

 



