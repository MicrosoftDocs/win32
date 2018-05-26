---
Description: Contains a publishing license that is going to be republished by using the EditIssuanceLicense SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c3acbe5b-473c-4429-9167-5d89259305e9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EditIssuanceLicenseParams class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# EditIssuanceLicenseParams class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **EditIssuanceLicenseParams** SOAP data type contains a publishing license that is going to be republished by using the [**EditIssuanceLicense**](-editissuancelicense.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **EditIssuanceLicenseParams** class is derived from **System.Object**.

## Members

## Fields

The **EditIssuanceLicenseParams** class has the following fields.



| Field                       | Description                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SignedIssuanceLicense**   | Data type: [XmlNode](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An XML node that contains the signed publishing license that will be updated. This is the leaf certificate in the issuance license chain only, not the whole chain leading back to the root issuer.<br/>                                              |
| **UnsignedIssuanceLicense** | Data type: [XmlNode](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An XML node that contains the new issuance license, with the new rights, that will replace rights in the existing license. This is the leaf certificate in the issuance license chain only, not the whole chain leading back to the root issuer.<br/> |



 

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

[**EditIssuanceLicenseResponse**](-editissuancelicenseresponse.md)
</dt> </dl>

 

 




