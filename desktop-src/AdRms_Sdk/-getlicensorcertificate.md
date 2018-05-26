---
Description: The GetLicensorCertificate SOAP web method returns the active server licensor certificate chain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bf0984e0-419c-49a0-b681-46630af25f67
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: GetLicensorCertificate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetLicensorCertificate method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **GetLicensorCertificate** SOAP web method returns the active server licensor certificate chain.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public LicensorCertChain GetLicensorCertificate();
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
<td><pre><code>Public Function GetLicensorCertificate() As LicensorCertChain</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

This method returns the active server licensor certificate chain.

If an error occurs, this method will throw a **SoapException**. The inner exception will be a serialized exception that contains additional information about the error. Some of the more common inner exceptions are listed in the Exceptions section.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/Server.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

The AD RMS server licensor certificate chain holds the AD RMS public key used to identify the deployment and encrypt the content key in an issuance license. This certificate chain can be used in [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master), when using that function with the **DRM\_SERVER\_ISSUANCELICENSE** flag to get the string unsigned [*issuance license*](i-gly.md#-rm-issuance-license-gly) chain. However, you must first convert it into an acceptable chain by using the [**DRMConstructCertificateChain**](/windows/previous-versions/Msdrm/nf-msdrm-drmconstructcertificatechain?branch=master) function.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**LicensorCertChain**](-licensorcertchain.md)
</dt> </dl>

 

 




