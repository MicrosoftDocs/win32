---
Description: Contains the server licensor certificate chain that is returned by the GetLicensorCertificate SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e04b3c14-4b1e-411a-9d65-ae83e4d9c7bb
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: LicensorCertChain class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# LicensorCertChain class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **LicensorCertChain** SOAP data type contains the server licensor certificate chain that is returned by the [**GetLicensorCertificate**](-getlicensorcertificate.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **LicensorCertChain** class is derived from **System.Object**.

## Members

## Fields

The **LicensorCertChain** class has the following fields.



| Field                | Description                                                                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CertificateChain** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the server licensor certificate chain.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/Server.asmx?wsdl

## Remarks

The leaf certificate in this chain holds the public key used to encrypt the content key, which is used to encrypt the content. This license chain can be used in [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense), when using that function with the **DRM\_SERVER\_ISSUANCELICENSE** flag to get the string unsigned publishing license chain.

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**GetLicensorCertificate**](-getlicensorcertificate.md)
</dt> </dl>

 

 




