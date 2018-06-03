---
Description: The Active Directory Rights Management Services (AD RMS) SDK contains the following structures.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 06a0c6d2-108d-4c72-9ae6-8959304602c5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Structures
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Structures

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK contains the following structures.



| Structure or enumeration                                      | Description                                                                                                    |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DRM\_ACTSERV\_INFO**](/previous-versions/windows/desktop/api/Msdrmdefs/ns-msdrmdefs-_drm_actserv_info)                | Contains information about the activation server.                                                              |
| [**DRM\_CLIENT\_VERSION\_INFO**](/previous-versions/windows/desktop/api/Msdrmdefs/ns-msdrmdefs-_drm_client_version_info) | Receives information about the AD RMS client version and certificate hierarchy (Production or Pre-production). |
| [**DRM\_LICENSE\_ACQ\_DATA**](/previous-versions/windows/desktop/api/Msdrmdefs/ns-msdrmdefs-_drm_license_acq_data)       | Contains license acquisition data during nonsilent license acquisition.                                        |
| [**DRMBOUNDLICENSEPARAMS**](/previous-versions/windows/desktop/api/Msdrmdefs/ns-msdrmdefs-_drmboundlicenseparams)        | Contains information used to bind to a license.                                                                |
| [**DRMID**](/previous-versions/windows/desktop/api/Msdrmdefs/ns-msdrmdefs-_drmid)                                        | Contains an object ID.                                                                                         |
| [**DRMPUBHANDLE**](drmpubhandle.md)                          | Data type that contains an opaque handle to an issuance license.                                               |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



