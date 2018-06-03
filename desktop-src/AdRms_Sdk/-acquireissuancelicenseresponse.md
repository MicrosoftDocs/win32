---
Description: Contains an issuance license chain signed by a call to the AcquireIssuanceLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5f4b9dff-d9c3-4bcd-a987-6dff9ef5bc57
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireIssuanceLicenseResponse class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AcquireIssuanceLicenseResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireIssuanceLicenseResponse** SOAP data type contains an issuance license chain signed by a call to the [**AcquireIssuanceLicense**](-acquireissuancelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquireIssuanceLicenseResponse** class is derived from **System.Object**.

## Members

## Fields

The **AcquireIssuanceLicenseResponse** class has the following fields.



| Field                | Description                                                                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CertificateChain** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the signed issuance license chain.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/Publish.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page. Only the leaf certificate in this chain (array index zero in each **AcquireIssuanceLicenseResponse** item) is used to acquire a use license with [**AcquirePreLicense**](-acquireprelicense.md) or update a signed publishing license with [**EditIssuanceLicense**](-editissuancelicense.md).

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> <dt>

[**AcquireIssuanceLicense**](-acquireissuancelicense.md)
</dt> <dt>

[**AcquireIssuanceLicenseParams**](-acquireissuancelicenseparams.md)
</dt> </dl>

 

 




