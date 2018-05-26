---
Description: The Active Directory Rights Management Services (AD RMS) server exposes several XML web services that can be used to make SOAP calls directly to the AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6373a3a2-0e51-4d5f-b215-069751ed0b5e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS SOAP Web Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AD RMS SOAP Web Methods

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) server exposes several XML web services that can be used to make SOAP calls directly to the AD RMS server. These SOAP web methods are documented in the following topics as if they were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266). AD RMS exposes the following SOAP web methods.



| Method                                                            | Description                                                                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireContentKey**](-acquirecontentkey.md)                   | Acquires a decrypted content key from a server that has been decommissioned.                                                                                                      |
| [**AcquireIssuanceLicense**](-acquireissuancelicense.md)         | Signs and returns an issuance license chain.                                                                                                                                      |
| [**AcquireLicense**](-acquirelicense.md)                         | Returns one or more signed use licenses.                                                                                                                                          |
| [**AcquirePreLicense**](-acquireprelicense.md)                   | Returns one use license using a submitted user email address or Windows security identifier (SID).                                                                                |
| [**AcquireTemplateInformation**](-acquiretemplateinformation.md) | Returns information about the templates stored on an AD RMS server.                                                                                                               |
| [**AcquireTemplates**](-acquiretemplates.md)                     | Returns one or more AD RMS templates.                                                                                                                                             |
| [**EditIssuanceLicense**](-editissuancelicense.md)               | Takes a content key from a signed issuance license and inserts it into a submitted, unsigned issuance license, signs it, and then returns the new, signed issuance license chain. |
| [**GetLicensorCertificate**](-getlicensorcertificate.md)         | Returns the active server licensor certificate chain.                                                                                                                             |
| [**GetServerInfo**](-getserverinfo.md)                           | Retrieves an **XmlNode** object that contains information about an AD RMS server.                                                                                                 |
| [**PreCertify**](-precertify.md)                                 | Retrieves a certificate that can be used to acquire a license for a user account.                                                                                                 |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> </dl>

 

 



