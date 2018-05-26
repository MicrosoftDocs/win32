---
Description: Contains an updated publishing license obtained by the EditIssuanceLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 76684083-6085-4824-b7d6-6ab8a049c38f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EditIssuanceLicenseResponse class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# EditIssuanceLicenseResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **EditIssuanceLicenseResponse** SOAP data type contains an updated publishing license obtained by the [**EditIssuanceLicense**](-editissuancelicense.md) SOAP web method. This is used in republishing.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **EditIssuanceLicenseResponse** class is derived from **System.Object**.

## Members

## Fields

The **EditIssuanceLicenseResponse** class has the following fields.



| Field                | Description                                                                                                                                                                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CertificateChain** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes in which the first element in the array contains the updated signed issuance license. Only the first element of this array is used.<br/> |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/EditIssuanceLicense.asmx?wsdl

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

[**EditIssuanceLicense**](-editissuancelicense.md)
</dt> <dt>

[**EditIssuanceLicenseParams**](-editissuancelicenseparams.md)
</dt> </dl>

 

 




