---
Description: Contains a decrypted content key provided by a call to the AcquireContentKey SOAP web method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3058286e-14cf-4d8a-a5cb-6432b8a1a569
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireContentKeyResponse class
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AcquireContentKeyResponse class

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireContentKeyResponse** class contains a decrypted content key provided by a call to the [**AcquireContentKey**](-acquirecontentkey.md) SOAP web method.

> [!Note]  
> This SOAP data type is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Inheritance

The **AcquireContentKeyResponse** class is derived from **System.Object**.

## Members

### Properties

The **AcquireContentKeyResponse** class has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><strong>ContentKeyType</strong><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">A [String](https://msdn.microsoft.com/library/system.string.aspx) that identifies the type of content key. This can be one of the following values.<br/>
<dt>&quot;AES&quot;</dt> <dd> The content key is an AES key.<br/> </dd> <dt>&quot;DES&quot;</dt> <dd> The content key is a DES key.<br/> </dd> <dt>&quot;RSA&quot;</dt> <dd> The content key is an RSA key.<br/> </dd> <dt>&quot;Unknown&quot;</dt> <dd> The content key type is not known.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



 

## Fields

The **AcquireContentKeyResponse** class has the following fields.



| Field          | Description                                                                                                                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ContentKey** | Data type: [Byte\[\]](https://msdn.microsoft.com/library/system.byte.aspx)<br/> An array of [Bytes](https://msdn.microsoft.com/library/system.byte.aspx) that contains the decrypted content key.<br/> |



 

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

 

 




