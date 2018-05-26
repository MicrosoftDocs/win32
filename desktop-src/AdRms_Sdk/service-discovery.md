---
Description: You can use the DRMGetServiceLocation function to find the URL of an Active Directory Rights Management Services (AD RMS) certification, licensing, or publishing web service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3b5b7d6a-a891-40c0-9140-0b59c5b440c3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Service Discovery
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Service Discovery

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can use the [**DRMGetServiceLocation**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetservicelocation?branch=master) function to find the URL of an Active Directory Rights Management Services (AD RMS) certification, licensing, or publishing web service. **DRMGetServiceLocation** first searches to see if a URL for the requested service is specified in the registry. If not, the system searches by using Active Directory (in an enterprise) or Windows Live ID (on the Internet). For more information, see the following:

-   [**DRMGetServiceLocation**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetservicelocation?branch=master)
-   [OfflineSigning\_GetServiceURL.cpp](offlinesigning-getserviceurl-cpp.md)
-   [OnlineSigning\_GetServiceURL.cpp](onlinesigning-getserviceurl-cpp.md)
-   [UserActivation\_GetServiceURL.cpp](useractivation-getserviceurl-cpp.md)

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[AD RMS Server](ad-rms-server.md)
</dt> </dl>

 

 



