---
Description: Retrieves a certificate that can be used to acquire a license for a user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c050c24c-e1ce-4786-9f8a-1a7a44431528
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: PreCertify method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PreCertify method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **PreCertify** SOAP web method retrieves a certificate that can be used to acquire a license for a user account.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public PrecertifyResponse[] PreCertify(
  PrecertifyParams[] RequestParams
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
<td><pre><code>Public Function PreCertify( _
  ByVal RequestParams() As PrecertifyParams _
) As PrecertifyResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*RequestParams* 
</dt> <dd>

An array of [**PrecertifyParams**](-precertifyparams.md) objects that identify the end users to be certified.

> [!Note]  
> If you pass more than one array item (one user), the AD RMS server throws a [System.ArgumentException](https://msdn.microsoft.com/library/system.argumentexception.aspx) object.

 

</dd> </dl>

## Return value

An array of [**PrecertifyResponse**](-precertifyresponse.md) objects that contain the public portions of the rights account certificates for the specified users.

> [!Note]  
> The array can contain only one [**PrecertifyResponse**](-precertifyresponse.md) object because only one user can be specified on input.

 

## Web Service URL

*ServerURL*/\_wmcs/Certification/Precertification.asmx

## Remarks

Unlike the [**AcquirePreLicense**](-acquireprelicense.md) method, the **PreCertify** method can precertify accounts in different forests. To use this method to retrieve an end user license, first determine which forest the user resides in, call **PreCertify** on the AD RMS server in that forest, acquire the issuance license (usually from the protected content), and then call [**AcquireLicense**](-acquirelicense.md) on the server in the current forest.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**PrecertifyParams**](-precertifyparams.md)
</dt> <dt>

[**PrecertifyResponse**](-precertifyresponse.md)
</dt> </dl>

 

 




