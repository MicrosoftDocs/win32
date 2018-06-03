---
Description: A lockbox is a dynamic link library (DLL) that can be used to increase the security of the environment in which an Active Directory Rights Management Services (AD RMS) application runs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d67b7326-e447-4bfa-b015-1b546b68d7e2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Lockboxes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Lockboxes

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A lockbox is a dynamic link library (DLL) that can be used to increase the security of the environment in which an Active Directory Rights Management Services (AD RMS) application runs. The lockbox verifies all licenses and certificates used by the application and, for AD RMS clients, protects the process space by limiting access to required and optional modules identified in the application manifest. To create a secure environment, you can call [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment) and specify the lockbox path, the signed manifest, and the machine certificate.

Four lockboxes are installed with AD RMS. You can call [**DRMGetSecurityProvider**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsecurityprovider) to retrieve the path of the appropriate DLL for your certificate hierarchy (Production or Pre-production) and your operating system type (server or client).

| Lockbox DLL           | Description                                      |
|-----------------------|--------------------------------------------------|
| Secproc\_isv.dll      | Client lockbox for the Pre-production hierarchy. |
| Secproc.dll           | Client lockbox for the Production hierarchy.     |
| Secproc\_ssp\_isv.dll | Server lockbox for the Pre-production hierarchy. |
| Secproc\_ssp.dll      | Server lockbox for the Production hierarchy.     |



 

Use a client lockbox for applications running on a client. Use a server lockbox for applications running on an AD RMS server that both publish and consume protected content. If your server-based application publishes but does not consume protected content, you can use the SOAP APIs included with the SDK rather than a lockbox. The following table identifies the features associated with each type of lockbox and with the SOAP APIs. 

| Feature                                                    | Server lockbox                                                                                                                                                                                                             | Client lockbox                                                                        | SOAP APIs (no lockbox)                                                                                                          |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Availability                                               | RMS client 1.0 SP2<br/> Windows Vista<br/> Windows Server 2008<br/>                                                                                                                                      | RMS client 1.0 SP2<br/> Windows Vista<br/> Windows Server 2008<br/> | RMS client 1.0 SP2<br/> Windows Vista<br/> Windows Server 2008<br/>                                           |
| Supported RMS server versions                              | RMS client 1.0 SP2 and later.<br/>                                                                                                                                                                                   | All.<br/>                                                                       | All.<br/>                                                                                                                 |
| Common scenarios                                           | Server applications that publish, consume, or process RMS-protected content. For example, a virus scanner, an email server that filters out spam, a document library or archival tool, a workflow engine, or a web portal. | Client applications that publish and consume protected content.                       | Server applications that need to publish RMS-protected content but that cannot use the server lockbox due to technical reasons. |
| Supports publishing RMS-protected content                  | Yes.                                                                                                                                                                                                                       | Yes.                                                                                  | Yes.                                                                                                                            |
| Supports consuming RMS-protected content                   | Yes.                                                                                                                                                                                                                       | Yes.                                                                                  | No.                                                                                                                             |
| Machine activation                                         | Occurs locally.                                                                                                                                                                                                            | Occurs locally.                                                                       | Not supported.                                                                                                                  |
| Executable file name must be listed in manifest            | No.                                                                                                                                                                                                                        | Yes.                                                                                  | Manifests are not required.                                                                                                     |
| Immediate callers into Msdrm.dll must be named in manifest | No.                                                                                                                                                                                                                        | Yes.                                                                                  | Manifests are not required.                                                                                                     |
| Executable must be in native code                          | No.                                                                                                                                                                                                                        | No.                                                                                   | No.                                                                                                                             |
| Supported on virtual servers                               | Yes.                                                                                                                                                                                                                       | Yes.                                                                                  | No.                                                                                                                             |
| Supports multithreaded applications                        | Yes.                                                                                                                                                                                                                       | No.                                                                                   | Yes.                                                                                                                            |



 

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 




