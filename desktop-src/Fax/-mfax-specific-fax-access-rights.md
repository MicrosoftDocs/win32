---
Description: This topic describes the specific access rights defined by the Fax Service Client API.
ms.assetid: 7d6ff208-33e4-42b2-ae21-76ec8ff58809
title: Specific Fax Access Rights
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Specific Fax Access Rights

If you are using the Microsoft Component Object Model (COM) implementation, your fax client application cannot access this functionality at this time.

The Fax Service Client API defines the following specific access rights, which provide security when users query and manage fax jobs, fax devices, and fax documents.



| Value              | Meaning                                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_CONFIG\_QUERY | Grants permission to query configuration and routing method data at the fax server level.                                                                                  |
| FAX\_CONFIG\_SET   | Grants permission to modify configuration and routing method data at the fax server level.                                                                                 |
| FAX\_JOB\_MANAGE   | Grants permission to terminate a fax job in progress, or change the status of a queued fax job.                                                                            |
| FAX\_JOB\_QUERY    | Grants permission to query queued and active fax jobs.                                                                                                                     |
| FAX\_JOB\_SUBMIT   | Grants permission to send a fax transmission to one or more recipients.                                                                                                    |
| FAX\_PORT\_QUERY   | Grants permission to query configuration, status, and routing method data at the port level. This access right includes the ability to obtain and close a fax port handle. |
| FAX\_PORT\_SET     | Grants permission to modify configuration and routing method data at the port level. This access right includes the ability to enable or disable a fax routing method.     |



 

For more information about the rights users must have to query and modify port data, see [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

 

 



