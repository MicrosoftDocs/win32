---
Description: Contains information returned from a use license acquisition attempt that used the AcquirePreLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 83c9c686-4318-40e4-a20e-226d65db6303
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquirePreLicenseResponse class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# AcquirePreLicenseResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquirePreLicenseResponse** SOAP data type contains information returned from a use license acquisition attempt that used the [**AcquirePreLicense**](-acquireprelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseResponse** class is derived from **System.Object**.

## Members

## Fields

The **AcquirePreLicenseResponse** class has the following fields.



| Field                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Licenses**              | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the use licenses, index correlated to the licensee identities passed in. Each license is the leaf certificate only in the chain leading back to the root issuer. The license must be added to the **CertificateChain** array for a valid license chain that a client can use.<br/> |
| **CertificateChain**      | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the common licensor chain (from the server licensor certificate to the root) needed for the use licenses.<br/>                                                                                                                                                                     |
| **ReferenceCertificates** | This field is not currently used.<br/>                                                                                                                                                                                                                                                                                                                                                                                 |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/License.asmx?wsdl

## Remarks

This class is used by [**AcquirePreLicense**](-acquireprelicense.md) to get a use license for one or more people by using the same issuance license. The retrieved values must be reformatted for a client to use them to acquire a use license. Reformat them in this way:

1.  Convert each **CertificateChain** value into a string array.
2.  Convert the corresponding **Licenses** value into a string value.
3.  Append the license as an initial element in the certificate chain array.
4.  Pass the resulting string array into [**DRMConstructCertificateChain**](/windows/previous-versions/Msdrm/nf-msdrm-drmconstructcertificatechain?branch=master) to create a certificate chain that can be used by an AD RMS-consuming application to acquire a use license.

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**AcquirePreLicense**](-acquireprelicense.md)
</dt> <dt>

[**AcquirePreLicenseParams**](-acquireprelicenseparams.md)
</dt> </dl>

 

 




