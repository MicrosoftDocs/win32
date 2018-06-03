---
Description: To use the preproduction hierarchy, you must configure the registry on both the server computer and client computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b0899bbd-ed54-4dde-8a6c-860218a436b6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Configure the Registry
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configure the Registry

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

To use the preproduction hierarchy, you must configure the registry on both the server computer and client computer.

## Preproduction Server Settings

To specify that you are using the preproduction certificate hierarchy, set the following registry values.

> [!Note]  
> If you are using Windows Server 2008 R2 or Windows Server 2008, set the registry values before installing the AD RMS service. If you are using Windows Server 2003, set the registry values after installing the service, but before provisioning.

 

If you are using AD RMS on Windows Server 2008 R2, you must set the following **REG\_DWORD** value. Change this value to 0 to switch to the production hierarchy.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**Hierarchy** = 0x00000001

If you are using AD RMS on Windows Server 2008 R2 and another AD RMS service is already deployed in Active Directory as a pre-production service, add the following empty string value to the registry.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**GICURL** = ""

If you are using AD RMS on Windows Server 2008, you must set the following **REG\_DWORD** value. Change this value to 0 to switch to the production hierarchy.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**2.0**\\**Hierarchy** = 0x00000001

If you are using AD RMS on Windows Server 2008 and another AD RMS service is already deployed in Active Directory as a pre-production service, add the following empty string value to the registry.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**2.0**\\**GICURL** = ""

If you are using RMS 1.0 SP2 with Windows Server 2003 or earlier, add the following **REG\_SZ** value. When you want to switch to the production hierarchy, remove this value.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

If you are using RMS 1.0 SP2 with Windows Server 2003 or earlier, and another AD RMS service is already deployed in Active Directory as a preproduction service, add the following empty string value to the registry.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**GICURL** = ""

## Preproduction Client Settings

If you are running a 32-bit client on a 32-bit operating system or a 64-bit client on a 64-bit operating system, set the following **REG\_DWORD** value to specify the preproduction hierarchy. Change this value to 0 to switch to the production hierarchy.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**uDRM**\\**Hierarchy** = 0x00000001

If you are running a 32-bit client on a 64-bit operating system, set the following **REG\_DWORD** value. Change this value to 0 to switch to the production hierarchy.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Wow6432Node**\\**Microsoft**\\**uDRM**\\**Hierarchy** = 0x00000001

If you are using AD RMS on Windows 7, you can set the size limit, in bytes, of signed issuance licenses with the following **REG\_DWORD** value (the example sets the limit to 1 MB). If a signed issuance license exceeds the size limit you set, the E\_DRM\_ISSUANCELICENSE\_LENGTH\_LIMIT\_EXCEEDED error is thrown by [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense). The default size limit for an issuance license is 2 MB.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**MSDRM**\\**MaxLengthSignedOfflineIssuanceLicense** = 0x001048576

If you are running a 32-bit client on a 64-bit operating system, use the following setting to set the size limit of signed issuance licenses.

**Computer**\\**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Wow6432Node**\\**Microsoft**\\**MSDRM**\\**MaxLengthSignedOfflineIssuanceLicense** = 0x001048576

The client uses the same license store for both the production hierarchy and preproduction hierarchy. You should restore the client machine to a clean state each time you switch between the production hierarchy and preproduction hierarchy.

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



