---
Description: The Active Directory Rights Management Services (AD RMS) SDK contains the following enumeration types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bc3a8ab3-9f89-442b-9910-85820b2b2653
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Enumerations
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Enumerations

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK contains the following enumeration types.



| Structure or enumeration                                              | Description                                                                                                                                                 |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_DISTRIBUTION\_POINT\_INFO**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_distribution_point_info) | Specifies the type of distribution point to retrieve information about when calling [**DRMGetIssuanceLicenseInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetissuancelicenseinfo).         |
| [**DRM\_STATUS\_MSG**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_status_msg)                            | Used by the custom callback function to specify why it is being called.                                                                                     |
| [**DRM\_USAGEPOLICY\_TYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drm_usagepolicy_type)                | Specifies or retrieves the usage policy type when calling [**DRMSetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetusagepolicy) or [**DRMGetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetusagepolicy). |
| [**DRMATTESTTYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmattesttype)                                | Specifies the type of signature to create for a data blob.                                                                                                  |
| [**DRMENCODINGTYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmencodingtype)                            | Identifies possible encoding types used in licenses.                                                                                                        |
| [**DRMGLOBALOPTIONS**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmglobaloptions)                          | Specifies which transport protocol is used and whether the server lockbox is used.                                                                          |
| [**DRMSECURITYPROVIDERTYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmsecurityprovidertype)            | Specifies the type of secure environment used.                                                                                                              |
| [**DRMSPECTYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmspectype)                                    | Specifies the type of security or library provider to use.                                                                                                  |
| [**DRMTIMETYPE**](/previous-versions/windows/desktop/api/Msdrmdefs/ne-msdrmdefs-_drmtimetype)                                    | Specifies whether the time represented is universal or local.                                                                                               |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



