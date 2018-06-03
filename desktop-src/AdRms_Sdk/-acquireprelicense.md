---
Description: Returns one use license for a proxy use license requester.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fa21a8fd-6c35-4ef9-bf94-b1229b3a8b60
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquirePreLicense method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AcquirePreLicense method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquirePreLicense** SOAP web method returns one use license for a proxy use license requester.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public AcquirePreLicenseResponse[] AcquirePreLicense(
  AcquirePreLicenseParams[] RequestParams
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
<td><pre><code>Public Function AcquirePreLicense( _
  ByVal RequestParams() As AcquirePreLicenseParams _
) As AcquirePreLicenseResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*RequestParams* 
</dt> <dd>

An array of [**AcquirePreLicenseParams**](-acquireprelicenseparams.md) objects that contain information required for one or more use license requests.

> [!Note]  
> Servers will only accept requests that consist of arrays that contain a single element. All other requests will fail.

 

</dd> </dl>

## Return value

An array of [**AcquirePreLicenseResponse**](-acquireprelicenseresponse.md) objects that contain the signed use license, if granted.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/License.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

This function retrieves a signed use license that corresponds to one issuance license. Prelicensing is done on behalf of the license recipient by a service, such as Microsoft SharePoint Team Services. The purpose of this function is to enable a publisher to request a use license at publishing time so that it can provide an end user with all the required licenses to consume a piece of content without having to contact a server.

The returned certificate chain contains the common chain for the license. When a client receives this response, it must construct a certificate chain that a rights management consuming application can use as described in [**AcquirePreLicenseResponse**](-acquireprelicenseresponse.md).

Note that you cannot use Passport identification to acquire a use license by using this function. The only way Passport identification can be used to acquire a use license is for the end user to request the license by using the [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) function.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**AcquireIssuanceLicense**](-acquireissuancelicense.md)
</dt> <dt>

[**AcquirePreLicenseParams**](-acquireprelicenseparams.md)
</dt> <dt>

[**AcquirePreLicenseResponse**](-acquireprelicenseresponse.md)
</dt> </dl>

 

 




