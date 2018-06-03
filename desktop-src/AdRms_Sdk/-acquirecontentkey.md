---
Description: Acquires a decrypted content key from a server that has been decommissioned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2759e1cc-39fd-46e0-b0d3-cf563b8c09d9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireContentKey method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AcquireContentKey method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireContentKey** SOAP web method acquires a decrypted content key from a server that has been decommissioned.

> \[!Important\]  
> It is very important to understand that only approved computers or (occasionally) users should have access to this function because anyone with access to this function can obtain a decrypted content key.

 

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public AcquireContentKeyResponse[] AcquireContentKey(
  AcquireContentKeyParams[] paramsSoap
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public Function AcquireContentKey( _
  ByVal paramsSoap() As AcquireContentKeyParams _
) As AcquireContentKeyResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*paramsSoap* 
</dt> <dd>

An array of [**AcquireContentKeyParams**](-acquirecontentkeyparams.md) objects that contain the issuance licenses to obtain the decrypted content key for.

</dd> </dl>

## Return value

An array of [**AcquireContentKeyResponse**](-acquirecontentkeyresponse.md) objects that contain the decrypted content keys.

## Web Service Description Page

*ServerURL*/\_wmcs/Decommission/Decommission.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

For this web method to succeed, the server must have been decommissioned by the administrator and the proper access control lists (ACLs) must have been set on the virtual root of the server. For more information about decommissioning, see the AD RMS product documentation.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**AcquireContentKeyParams**](-acquirecontentkeyparams.md)
</dt> <dt>

[**AcquireContentKeyResponse**](-acquirecontentkeyresponse.md)
</dt> </dl>

 

 




