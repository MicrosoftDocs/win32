---
Description: Contains the information required to request a use license by using the AcquirePreLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c87f3079-1c3f-4c33-a07d-9857774b151f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquirePreLicenseParams class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# AcquirePreLicenseParams class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquirePreLicenseParams** SOAP data type contains the information required to request a use license by using the [**AcquirePreLicense**](-acquireprelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseParams** class is derived from **System.Object**.

## Members

## Fields

The **AcquirePreLicenseParams** class has the following fields.



| Field                  | Description                                                                                                                                                                                                                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LicenseeIdentities** | Data type: [String\[\]](https://msdn.microsoft.com/library/system.string.aspx)<br/> An array of strings that contains the licensee identifiers. These identifiers can either be a fully qualified Windows email address (for example, "someone@example.com"), or a Windows SID.<br/> |
| **IssuanceLicense**    | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the issuance licenses (leaf certificate in the chain only) to use in licensing.<br/>                                                                   |
| **ApplicationData**    | This field is not currently used.<br/>                                                                                                                                                                                                                                                     |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/License.asmx?wsdl

## Remarks

This class is used by [**AcquirePreLicense**](-acquireprelicense.md) to get a use license for one or more people using the same issuance license.

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

[**AcquirePreLicenseResponse**](-acquireprelicenseresponse.md)
</dt> </dl>

 

 




