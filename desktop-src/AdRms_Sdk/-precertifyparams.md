---
Description: Contains information required by the PreCertify SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3e37b753-12a8-40b4-8e2e-35699da380d8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: PrecertifyParams class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# PrecertifyParams class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **PrecertifyParams** SOAP data type contains information required by the [**PreCertify**](-precertify.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquirePreLicenseParams** class is derived from **System.Object**.

## Members

## Fields

The **PrecertifyParams** class has the following fields.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Identification</strong></td>
<td>Data type: [<strong>Identification</strong>](-identification.md)<br/> An [<strong>Identification</strong>](-identification.md) object that specifies the authentication mode. This object contains the following fields:<br/> <dl> <dt><span id="AuthenticationMode"></span><span id="authenticationmode"></span><span id="AUTHENTICATIONMODE"></span>AuthenticationMode</dt> <dd> The authentication type. This field must be set to Windows.<br/> </dd> <dt><span id="Id"></span><span id="id"></span><span id="ID"></span>Id</dt> <dd> A security identifier (SID) for the user. Specify this value only if an email address is not specified in the <em>UserName</em> field. Otherwise, set this value to <strong>NULL</strong>.<br/> </dd> <dt><span id="Email"></span><span id="email"></span><span id="EMAIL"></span>Email</dt> <dd> This field must be <strong>NULL</strong>.<br/> </dd> <dt><span id="ProxyAddresses"></span><span id="proxyaddresses"></span><span id="PROXYADDRESSES"></span>ProxyAddresses</dt> <dd> This field must be <strong>NULL</strong>.<br/> </dd> </dl>
<blockquote>
[!Note]<br />
Prior to Windows Server 2008, only the AuthenticationMode and Id fields were supported.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>UserName</strong></td>
<td>Data type: [String](https://msdn.microsoft.com/library/system.string.aspx)<br/> A string value that contains the email address of the user to be certified. If this field is empty, specify a SID for the Id value of the [<strong>Identification</strong>](-identification.md) object.<br/></td>
</tr>
</tbody>
</table>



 

## Web Service Description Page

*ServerURL*/\_wmcs/Certification/Precertification.asmx?wsdl

## Remarks

This class is used by the [**PreCertify**](-precertify.md) method to acquire rights account certificates for end users. The certificates can be used to acquire end user licenses to decrypt content. The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

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

[**PreCertify**](-precertify.md)
</dt> <dt>

[**PrecertifyResponse**](-precertifyresponse.md)
</dt> </dl>

 

 




