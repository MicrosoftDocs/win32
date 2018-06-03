---
Description: The following data types are used by the Active Directory Rights Management Services (AD RMS) SOAP web methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1f405503-f3b4-47c7-b6e0-906f14e51161
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS SOAP Data Types
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS SOAP Data Types

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following data types are used by the Active Directory Rights Management Services (AD RMS) SOAP web methods. These data types are documented in the following topics as if they were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the .wsdl page located at the service description page.



| Class                                                                     | Description                                                                                                                                                        |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireContentKeyParams**](-acquirecontentkeyparams.md)               | Contains the information required to request a decrypted content key by using the [**AcquireContentKey**](-acquirecontentkey.md) SOAP web method.                 |
| [**AcquireContentKeyResponse**](-acquirecontentkeyresponse.md)           | Contains a decrypted content key provided by a call to the [**AcquireContentKey**](-acquirecontentkey.md) SOAP web method.                                        |
| [**AcquireIssuanceLicenseParams**](-acquireissuancelicenseparams.md)     | Contains the information required to request a signed issuance license by using the [**AcquireIssuanceLicense**](-acquireissuancelicense.md) SOAP web method.     |
| [**AcquireIssuanceLicenseResponse**](-acquireissuancelicenseresponse.md) | Contains an issuance license chain signed by a call to the [**AcquireIssuanceLicense**](-acquireissuancelicense.md) SOAP web method.                              |
| [**AcquireLicenseParams**](-acquirelicenseparams.md)                     | Contains the information required to request a use license by using the [**AcquireLicense**](-acquirelicense.md) SOAP web method.                                 |
| [**AcquireLicenseResponse**](-acquirelicenseresponse.md)                 | Contains information returned from a use license acquisition attempt that used the [**AcquireLicense**](-acquirelicense.md) SOAP web method.                      |
| [**AcquirePreLicenseParams**](-acquireprelicenseparams.md)               | Contains the information required to request a use license by using the [**AcquirePreLicense**](-acquireprelicense.md) SOAP web method.                           |
| [**AcquirePreLicenseResponse**](-acquireprelicenseresponse.md)           | Contains information returned from a use license acquisition attempt that used the [**AcquirePreLicense**](-acquireprelicense.md) SOAP web method.                |
| [**AuthenticationMode**](-authenticationmode.md)                         | An enumeration type that specifies the authentication mode to be applied to an end user by the [**PreCertify**](-precertify.md) SOAP web method.                  |
| [**EditIssuanceLicenseParams**](-editissuancelicenseparams.md)           | Contains an issuance license that is going to be republished by using the [**EditIssuanceLicense**](-editissuancelicense.md) SOAP web method.                     |
| [**EditIssuanceLicenseResponse**](-editissuancelicenseresponse.md)       | Contains an updated issuance license obtained by the [**EditIssuanceLicense**](-editissuancelicense.md) SOAP web method. This is used in republishing.            |
| [**GuidHash**](-guidhash.md)                                             | Contains a GUID for an AD RMS template and a hash of the template identified by the GUID.                                                                          |
| [**GuidTemplate**](-guidtemplate.md)                                     | Represents a template stored on an AD RMS server.                                                                                                                  |
| [**Identification**](-identification.md)                                 | Contains information used by a [**PrecertifyParams**](-precertifyparams.md) object to identify an end user.                                                       |
| [**LicensorCertChain**](-licensorcertchain.md)                           | Contains the returned server licensor certificate chain for AD RMS in the [**GetLicensorCertificate**](-getlicensorcertificate.md) SOAP web method.               |
| [**PrecertifyParams**](-precertifyparams.md)                             | Contains information used by the [**PreCertify**](-precertify.md) SOAP web method to identify an end user.                                                        |
| [**PrecertifyResponse**](-precertifyresponse.md)                         | Contains a certificate returned by the [**PreCertify**](-precertify.md) SOAP web method.                                                                          |
| [**ServerInfoRequest**](-serverinforequest.md)                           | Defines a property that enables you to specify the type of AD RMS server information to retrieve when you call the [**GetServerInfo**](-getserverinfo.md) method. |
| [**ServerInfoType**](-serverinfotype.md)                                 | Specifies the type of server information retrieved when you call the [**GetServerInfo**](-getserverinfo.md) method.                                               |
| [**TemplateInformation**](-templateinformation.md)                       | Contains information about the templates stored on an AD RMS server.                                                                                               |
| [**VersionData**](-versiondata.md)                                       | Specifies the version of AD RMS required by the client and the server.                                                                                             |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> </dl>

 

 



