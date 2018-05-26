---
Description: Signs and returns one issuance license chain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1dc1dc7f-4e63-4cc6-aa34-a8e44ce79655
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireIssuanceLicense method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AcquireIssuanceLicense method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireIssuanceLicense** SOAP web method signs and returns one [*issuance license*](i-gly.md#-rm-issuance-license-gly) chain.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public AcquireIssuanceLicenseResponse[] AcquireIssuanceLicense(
  AcquireIssuanceLicenseParams[] RequestParams
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
<td><pre><code>Public Function AcquireIssuanceLicense( _
  ByVal RequestParams() As AcquireIssuanceLicenseParams _
) As AcquireIssuanceLicenseResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*RequestParams* 
</dt> <dd>

An array of [**AcquireIssuanceLicenseParams**](-acquireissuancelicenseparams.md) objects that specifies request parameters. This array can contain only one element.

> [!Note]  
> Servers will only accept requests that consist of arrays that contain a single element. All other requests will fail.

 

</dd> </dl>

## Return value

An array of [**AcquireIssuanceLicenseResponse**](-acquireissuancelicenseresponse.md) objects that represent the signed issuance license chain.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/Publish.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

A signed issuance license chain is used to obtain a use license for a piece of content. Only the leaf certificate in this chain (array index 0 in each [**AcquireIssuanceLicenseResponse**](-acquireissuancelicenseresponse.md) item) is used to acquire a use license with [**AcquirePreLicense**](-acquireprelicense.md), or update a signed issuance license with [**EditIssuanceLicense**](-editissuancelicense.md).

If the AD RMS client and server versions are not identical, an issuance license cannot be signed online.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**AcquireIssuanceLicenseParams**](-acquireissuancelicenseparams.md)
</dt> <dt>

[**AcquireIssuanceLicenseResponse**](-acquireissuancelicenseresponse.md)
</dt> </dl>

 

 




