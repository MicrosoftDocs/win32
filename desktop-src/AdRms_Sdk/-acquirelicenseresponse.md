---
Description: Contains information returned from a use license acquisition attempt that used the AcquireLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3ebccbb4-7e4f-498f-baa9-f992003a593b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireLicenseResponse class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# AcquireLicenseResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireLicenseResponse** SOAP data type contains information returned from a use license acquisition attempt that used the [**AcquireLicense**](-acquirelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseResponse** class is derived from **System.Object**.

## Members

## Fields

The **AcquireLicenseResponse** class has the following fields.



| Field                     | Description                                                                                                                                                                                                                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CertificateChain**      | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the common licensor chain needed for the use license(s). The use license appears at node zero \[0\], and the licensor chain begins at node one \[1\].<br/> |
| **ReferenceCertificates** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> This field is not currently used.<br/>                                                                                                                                                         |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/License.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**AcquireLicense**](-acquirelicense.md)
</dt> <dt>

[**AcquireLicenseResponse**](-acquirelicenseresponse.md)
</dt> </dl>

 

 




