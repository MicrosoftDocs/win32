---
Description: The Fax Service Extended COM API implementation provides complete support for the broadcasting of faxes.
ms.assetid: dd9a7eae-110b-498e-88f9-5a596b25cadd
title: Fax Broadcasts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Broadcasts

The Fax Service Extended Component Object Model (COM) API implementation provides complete support for the broadcasting of faxes. Clients can create a single fax document, specify the recipients, and submit one broadcast request. The fax service receives the broadcast as one submission. The service creates a unique job in the job queue for each of the recipients, assigning each job the same submission ID. This makes it possible to group all the jobs in the broadcast.

The default configuration value is 0, which means there is no limit on the number of recipients in a single fax broadcast. In Windows Server 2003 you can set a limit by specifying a maximum number of recipients as a **REG\_DWORD** value in the registry at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Fax**\\**RecipientsLimit**. No value, or a 0 value, means that there is no limit. If you change this value, you must restart the fax service for the change to take effect.

Once you set a limit, an attempt to send a single fax to more recipients than the number specified will result in the error.

For more information, see [FAX\_E\_RECIPIENT\_LIMIT](-mfax-fax-error-codes.md).

The Fax Service Client API for Windows 2000 does not provide complete support for the broadcasting of faxes. This is because each recipient job in the broadcast receives a unique job ID; there is no ID that is common to all jobs in a broadcast.

## Related topics

<dl> <dt>

[Archived Broadcast Messages](-mfax-archived-broadcast-messages.md)
</dt> </dl>

 

 



