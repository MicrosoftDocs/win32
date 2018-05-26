---
Description: Contains a certificate returned by the PreCertify SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 299853d9-75db-4fa4-bfc9-f3af8be2340a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: PrecertifyResponse class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# PrecertifyResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **PrecertifyResponse** SOAP data type contains a certificate returned by the [**PreCertify**](-precertify.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseResponse** class is derived from **System.Object**.

## Members

The **PrecertifyResponse** class has the following fields.



| Field           | Description                                                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Certificate** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An XML node that contains the rights account certificate (RAC) needed to acquire a use license for a user.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Certification/Precertification.asmx?wsdl

## Remarks

Before you can use the **PrecertifyResponse** value in the [**AcquireLicense**](-acquirelicense.md) method, you must convert the returned certificate into a string value. The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                    |
|--------------------|----------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**PreCertify**](-precertify.md)
</dt> <dt>

[**PrecertifyParams**](-precertifyparams.md)
</dt> </dl>

 

 




