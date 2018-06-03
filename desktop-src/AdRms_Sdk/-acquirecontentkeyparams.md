---
Description: The AcquireContentKeyParams class contains the information required to request a decrypted content key by using the AcquireContentKey SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1123e310-3932-4bd8-86cb-80c11f4bf2c5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireContentKeyParams class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AcquireContentKeyParams class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireContentKeyParams** class contains the information required to request a decrypted content key by using the [**AcquireContentKey**](-acquirecontentkey.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquireContentKeyParams** class is derived from **System.Object**.

## Members

## Fields

The **AcquireContentKeyParams** class has the following fields.



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
<td><strong>IssuanceLicense</strong></td>
<td>Data type: [XmlNode[]](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx)<br/> An array of XML nodes that contains the issuance licenses to acquire the content keys for.<br/>
<blockquote>
[!Note]<br />
Only the first element of the array is processed.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Web Service Description Page

*ServerURL*/\_wmcs/Decommission/Decommission.asmx?wsdl

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[**AcquireContentKey**](-acquirecontentkey.md)
</dt> <dt>

[AD RMS SOAP Data Types](ad-rms-soap-data-types.md)
</dt> </dl>

 

 




