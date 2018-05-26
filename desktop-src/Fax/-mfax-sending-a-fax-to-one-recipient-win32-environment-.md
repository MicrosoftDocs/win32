---
Description: This topic describes how to send a fax to a recipient in the Microsoft Win32 environment.
ms.assetid: 99331570-b396-4ed8-b2f4-3db883be0130
title: Sending a Fax to One Recipient (Win32 Environment)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sending a Fax to One Recipient (Win32 Environment)

A fax client application can call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function to queue a job that will transmit an outgoing fax to one recipient, specifying a file stored on disk.

The application must specify one file to transmit and supply a pointer to a [**FAX\_JOB\_PARAM**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_parama?branch=master) structure. The fax server queues the fax transmission job according to the details specified by the **FAX\_JOB\_PARAM** structure. The structure includes the recipient's fax number, sender and recipient data, an optional billing code, and job scheduling information.

The application must also supply a pointer to a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure if a cover page is required. This structure contains data to display on the cover page of a fax transmission. For more information, see [Sending a Cover Page](-mfax-sending-a-cover-page.md).

Call the [**FaxCompleteJobParams**](/windows/previous-versions/Winfax/nf-winfax-faxcompletejobparamsa?branch=master) function before calling the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) and [**FAX\_JOB\_PARAM**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_parama?branch=master) structures. Call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to free the memory associated with these structures.

To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function multiple times. The [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function is supported for backward compatibility. Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the **FaxSendDocument** function and the **FaxSendDocumentForBroadcast** function.

 

 



