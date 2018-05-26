---
Description: Identifies an end user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: eba5c607-8e6b-42fd-93cf-d6eaf5ad1fb5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Identification class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Identification class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **Identification** class identifies an end user. This object is used by the [**PrecertifyParams**](-precertifyparams.md) object.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **GuidHash** class is derived from **System.Object**.

## Members

## Fields

The **Identification** class has the following fields.



| Field                                             | Description                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AuthenticationMode**](-authenticationmode.md) | Data type: [**AuthenticationMode**](-authenticationmode.md)<br/> A value of the [**AuthenticationMode**](-authenticationmode.md) enumeration that specifies the type of authentication to be used.<br/> |
| **Id**                                            | Data type: **String**<br/> A string value that contains the security identifier (SID) of the user.<br/>                                                                                                   |
| **Email**                                         | Data type: **String**<br/> A string value that contains the email address of the user.<br/>                                                                                                               |
| **ProxyAddresses**                                | Data type: **String\[\]**<br/> An array of string values that contain possible user proxy addresses.<br/>                                                                                                 |



 

## Web Service Description Page

*ServerURL*/\_wmcs/Certification/Precertification.asmx?wsdl

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

[**PreCertify**](-precertify.md)
</dt> <dt>

[**PrecertifyParams**](-precertifyparams.md)
</dt> <dt>

[**PrecertifyResponse**](-precertifyresponse.md)
</dt> </dl>

 

 




