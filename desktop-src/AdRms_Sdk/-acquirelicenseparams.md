---
Description: Contains the information required to request a use license by using the AcquireLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 91baed1b-3821-4d49-b174-97b3d2adee94
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireLicenseParams class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# AcquireLicenseParams class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireLicenseParams** SOAP data type contains the information required to request a use license by using the [**AcquireLicense**](-acquirelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseParams** class is derived from **System.Object**.

## Members

## Fields

The **AcquireLicenseParams** class has the following fields.



| Field               | Description                                                                                                                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LicenseeCerts**   | Data type: [String](https://msdn.microsoft.com/library/system.string.aspx)<br/> A string that contains the identity account certificate of the user. This is the leaf certificate in the certificate chain.<br/>   |
| **IssuanceLicense** | Data type: [XmlNode\[\]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the issuance licenses (leaf certificate in the chain only) to use in licensing.<br/> |
| **ApplicationData** | This field is not currently used.<br/>                                                                                                                                                                                   |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Licensing/License.asmx?wsdl

## Remarks

The [**AcquireLicense**](-acquirelicense.md) SOAP web method passes an array of one or more **AcquireLicenseParams** objects to a server. The first **AcquireLicenseParams** object in the array must contain a value for the **IssuanceLicense** field. Subsequent objects in the array can contain a value for this field, but if they do not, the last value specified is used with the current **LicenseeCerts** value.

> [!Note]  
> Starting with RMS 1.0 SP2, enterprise servers can accept an array that contains more than a single element. Multiple elements are not, however, supported during license acquisition over the Internet.

 

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

[**AcquireLicenseParams**](-acquirelicenseparams.md)
</dt> </dl>

 

 




