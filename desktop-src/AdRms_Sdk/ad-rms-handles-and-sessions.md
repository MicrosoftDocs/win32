---
Description: Active Directory Rights Management Services functions use the following data types to provide opaque handles to objects. These objects are variously called sessions, bound licenses, libraries, crypto-providers, and environments.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3e031dec-ac80-4363-8786-2680d498cb5c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Handles and Sessions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Handles and Sessions

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services functions use the following data types to provide opaque handles to objects. These objects are variously called sessions, bound licenses, libraries, crypto-providers, and environments.

-   **DRMENVHANDLE** is a handle specifically for secure environments.
-   **DRMHSESSION** is a handle to a client or license storage session.
-   **DRMPUBHANDLE** is a handle to issuance licenses, rights, and users.
-   **DRMQUERYHANDLE** is a handle to unbound objects within a license.
-   **DRMHANDLE** is a handle for everything else, including bound license objects.

Create, copy, and delete these objects with their appropriate functions. It is important to use these functions for duplicating and closing objects, so the system can maintain a correct reference count and manage resources appropriately. Also, closing a handle or session properly clears sensitive information out of memory. Closing a handle or session closes all objects within that handle, so be sure all contained objects are properly closed before closing the object. Each handle type has the following duplication and closing methods.



| Handle         | Duplication function                                                   | Closing function                                               |
|----------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| DRMENVHANDLE   | [**DRMDuplicateEnvironmentHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicateenvironmenthandle) | [**DRMCloseEnvironmentHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcloseenvironmenthandle) |
| DRMHSESSION    | [**DRMDuplicateSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatesession)                     | [**DRMCloseSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosesession)                     |
| DRMQUERYHANDLE | None                                                                   | [**DRMCloseQueryHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosequeryhandle)             |
| DRMPUBHANDLE   | [**DRMDuplicatePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatepubhandle)                 | [**DRMClosePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosepubhandle)                 |
| DRMHANDLE      | [**DRMDuplicateHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatehandle)                       | [**DRMCloseHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosehandle)                       |



 

When declaring and initializing a handle, it should be set to a special \**\_INVALID* value, not **NULL** or zero, as shown here.


```C++
DRMENVHANDLE hEnv = DRMENVHANDLE_INVALID;
DRMHSESSION hSession = DRMHSESSION_INVALID;
DRMQUERYHANDLE hQuery = DRMQUERYHANDLE_INVALID;
DRMPUBHANDLE hPub = DRMPUBHANDLE_INVALID;
DRMHANDLE hHandle = DRMHANDLE_INVALID;

```



Similarly, when checking the value of a handle, be sure to compare it to the \**\_INVALID* value, not **NULL**, as shown.


```C++
if (hEnv == DRMENVHANDLE_INVALID)
//Handle error...

```



The **DRMHANDLE** and **DRMQUERYHANDLE** structures are used for navigating unbound licenses. For more information, see [Querying Licenses](querying-licenses.md).

## Related topics

<dl> <dt>

[AD RMS Functions](ad-rms-functions.md)
</dt> </dl>

 

 



