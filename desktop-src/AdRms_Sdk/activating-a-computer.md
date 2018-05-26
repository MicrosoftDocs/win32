---
Description: Before a specific computer can be used to encrypt or decrypt content, you must sign it into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f6980a9b-9e3c-47e4-b1c3-7e244ca77e44
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Activating a Computer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Activating a Computer

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Before a specific computer can be used to encrypt or decrypt content, you must sign it into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy. This process, called activating a computer, returns a certificate chain. The root of the chain is a Microsoft certification authority (CA) certificate, and the chain ends with a signed [*machine certificate*](m-gly.md#-rm-machine-certificate-gly) that uniquely identifies the computer being used. You can use the [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function to activate a computer. This is an asynchronous function that returns immediately to your application while processing the activation request on another thread. It delivers the result to a callback function that you must create. For more information, see [Creating a Callback Function](creating-a-callback-function.md).

After you activate the computer, you must also activate the account of the logged-on user to retrieve a [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly) that signs the account into the same hierarchy as the computer. For more information, see [Activating a User](activating-a-user.md). Activating a computer that has already been activated overwrites the machine certificate, thereby requiring that you also renew the rights account certificate. Therefore, you should check the current activation state to avoid inadvertently activating the computer more than once. You can call [**DRMIsActivated**](/windows/previous-versions/Msdrm/nf-msdrm-drmisactivated?branch=master) to check the state.

Computer activation is performed locally by the AD RMS client. There is no interaction with an AD RMS activation service. The client notifies your callback function when activation is complete and then installs the machine certificate in the appropriate store.

The following topics discuss computer activation and machine certificates in more detail.

| Topic                                                                    | Description                                                          |
|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Machine Certificates](machine-certificates.md)                         | Discusses the general XrML contents of a machine certificate.        |
| [Machine Certificate Store](machine-certificate-store.md)               | Lists the certificate stores by operating system and AD RMS version. |
| [Machine Certificate XML Example](machine-certificate-xml-example.md)   | Contains a complete XrML certificate example.                        |
| [Machine Certificate Code Example](machine-certificate-code-example.md) | Contains a C++ example that activates a computer.                    |



 

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



