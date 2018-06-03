---
Description: We recommend that you create a security threat model that describes various kinds of failures and attacks to which your application may be vulnerable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 53738ff5-3333-4036-acef-c4540d0c44df
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a Security Threat Model
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Security Threat Model

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

We recommend that you create a security threat model that describes various kinds of failures and attacks to which your application may be vulnerable. This enables developers to focus attention on these risks at all stages of the development process. A security threat model:

-   Documents the threats to your product.
-   Gauges the probability of various risks, to help determine how much development time should be invested to mitigate each threat.
-   Determines the extent of each risk. Some incidents can cause loss of individual data while others could impact every instance of your installed software, placing all of your end users and their data at risk.

Systemic failure may require revocation of services or exclusion of individual certificates or licenses from service. AD RMS includes revocation and exclusion features. For more information, see [Revocation](revocation.md) and [Exclusion](exclusion.md).

## Related topics

<dl> <dt>

[Recommended Software Development Practices](recommended-software-development-practices.md)
</dt> </dl>

 

 



