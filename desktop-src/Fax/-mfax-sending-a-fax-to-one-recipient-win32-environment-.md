---
Description: 'This topic describes how to send a fax to a recipient in the Microsoft Win32 environment.'
ms.assetid: '99331570-b396-4ed8-b2f4-3db883be0130'
title: 'Sending a Fax to One Recipient (Win32 Environment)'
---

# Sending a Fax to One Recipient (Win32 Environment)

A fax client application can call the [**FaxSendDocument**](-mfax-faxsenddocument.md) function to queue a job that will transmit an outgoing fax to one recipient, specifying a file stored on disk.

The application must specify one file to transmit and supply a pointer to a [**FAX\_JOB\_PARAM**](-mfax-fax-job-param-str.md) structure. The fax server queues the fax transmission job according to the details specified by the **FAX\_JOB\_PARAM** structure. The structure includes the recipient's fax number, sender and recipient data, an optional billing code, and job scheduling information.

The application must also supply a pointer to a [**FAX\_COVERPAGE\_INFO**](-mfax-fax-coverpage-info-str.md) structure if a cover page is required. This structure contains data to display on the cover page of a fax transmission. For more information, see [Sending a Cover Page](-mfax-sending-a-cover-page.md).

Call the [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md) function before calling the [**FaxSendDocument**](-mfax-faxsenddocument.md) function. **FaxCompleteJobParams** is a utility function that supplies data for members in the [**FAX\_COVERPAGE\_INFO**](-mfax-fax-coverpage-info-str.md) and [**FAX\_JOB\_PARAM**](-mfax-fax-job-param-str.md) structures. Call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to free the memory associated with these structures.

To send a fax document efficiently to multiple recipients, an application should call the [**FaxSendDocument**](-mfax-faxsenddocument.md) function multiple times. The [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function is supported for backward compatibility. Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the **FaxSendDocument** function and the **FaxSendDocumentForBroadcast** function.

 

 



