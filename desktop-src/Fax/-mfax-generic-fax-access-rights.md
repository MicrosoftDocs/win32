---
Description: This topic describes generic fax access rights.
ms.assetid: e762ddce-237a-4b30-a52c-269fed36dcac
title: Generic Fax Access Rights
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Generic Fax Access Rights

If you are using the Microsoft Component Object Model (COM) implementation, your fax client application cannot access this functionality at this time.

The Fax Service Client API defines the following generic fax access rights. Generic rights implicitly grant to users the indicated specific fax access rights.



| Value            | Meaning                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_READ        | Includes the read-only rights granted by the following specific access rights: FAX\_JOB\_QUERY, FAX\_CONFIG\_QUERY, and FAX\_PORT\_QUERY.                                                                                            |
| FAX\_WRITE       | This access is identical to the permissions granted by the FAX\_JOB\_SUBMIT specific access right. Note that this right does not include permission to modify data at the port or server levels.                                     |
| FAX\_ALL\_ACCESS | Includes all read/write administrative permissions granted by the following specific access rights: FAX\_CONFIG\_QUERY, FAX\_CONFIG\_SET, FAX\_JOB\_MANAGE, FAX\_JOB\_QUERY, FAX\_JOB\_SUBMIT, FAX\_PORT\_QUERY, and FAX\_PORT\_SET. |



 

For more information about the rights users must have to query and modify port data, see [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

 

 



