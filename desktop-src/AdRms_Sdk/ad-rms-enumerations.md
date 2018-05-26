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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AD RMS Enumerations

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK contains the following enumeration types.



| Structure or enumeration                                              | Description                                                                                                                                                 |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_DISTRIBUTION\_POINT\_INFO**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drm_distribution_point_info?branch=master) | Specifies the type of distribution point to retrieve information about when calling [**DRMGetIssuanceLicenseInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetissuancelicenseinfo?branch=master).         |
| [**DRM\_STATUS\_MSG**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drm_status_msg?branch=master)                            | Used by the custom callback function to specify why it is being called.                                                                                     |
| [**DRM\_USAGEPOLICY\_TYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drm_usagepolicy_type?branch=master)                | Specifies or retrieves the usage policy type when calling [**DRMSetUsagePolicy**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetusagepolicy?branch=master) or [**DRMGetUsagePolicy**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetusagepolicy?branch=master). |
| [**DRMATTESTTYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmattesttype?branch=master)                                | Specifies the type of signature to create for a data blob.                                                                                                  |
| [**DRMENCODINGTYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmencodingtype?branch=master)                            | Identifies possible encoding types used in licenses.                                                                                                        |
| [**DRMGLOBALOPTIONS**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmglobaloptions?branch=master)                          | Specifies which transport protocol is used and whether the server lockbox is used.                                                                          |
| [**DRMSECURITYPROVIDERTYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmsecurityprovidertype?branch=master)            | Specifies the type of secure environment used.                                                                                                              |
| [**DRMSPECTYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmspectype?branch=master)                                    | Specifies the type of security or library provider to use.                                                                                                  |
| [**DRMTIMETYPE**](/windows/previous-versions/Msdrmdefs/ne-msdrmdefs-_drmtimetype?branch=master)                                    | Specifies whether the time represented is universal or local.                                                                                               |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



