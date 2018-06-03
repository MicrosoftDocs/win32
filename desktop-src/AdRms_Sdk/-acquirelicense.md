---
Description: Returns one or more signed use licenses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4fc8187d-8fa1-44aa-a3b6-8376d4dfc25f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireLicense method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AcquireLicense method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireLicense** SOAP web method returns one or more signed use licenses.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public AcquireLicenseResponse[] AcquireLicense(
  AcquireLicenseParams[] RequestParams
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
<td><pre><code>Public Function AcquireLicense( _
  ByVal RequestParams() As AcquireLicenseParams _
) As AcquireLicenseResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*RequestParams* 
</dt> <dd>

An array of [**AcquireLicenseParams**](-acquirelicenseparams.md) objects, each of which contains the following fields.

<dt>

<span id="LicenseeCerts"></span><span id="licenseecerts"></span><span id="LICENSEECERTS"></span>

<span id="LicenseeCerts"></span><span id="licenseecerts"></span><span id="LICENSEECERTS"></span>****LicenseeCerts**** ()


</dt> <dd>

Contains the user identity account certificate.

</dd> <dt>

<span id="IssuanceLicense"></span><span id="issuancelicense"></span><span id="ISSUANCELICENSE"></span>

<span id="IssuanceLicense"></span><span id="issuancelicense"></span><span id="ISSUANCELICENSE"></span>****IssuanceLicense**** ()


</dt> <dd>

Contains the issuance license.

</dd> <dt>

<span id="ApplicationData"></span><span id="applicationdata"></span><span id="APPLICATIONDATA"></span>

<span id="ApplicationData"></span><span id="applicationdata"></span><span id="APPLICATIONDATA"></span>****ApplicationData**** ()


</dt> <dd>

This field is not supported.

</dd> </dl>

The first [**AcquireLicenseParams**](-acquirelicenseparams.md) object in the array must contain a value for the **IssuanceLicense** field. Subsequent objects in the array can contain a value for this field, but if they do not, the last value specified is used with the current **LicenseeCerts** value.

> [!Note]  
> Starting with RMS 1.0 SP2, enterprise servers can accept an array that contains more than a single element. Multiple elements are not, however, supported during license acquisition performed by using the Windows Live ID certification service.

 

</dd> </dl>

## Return value

An array of [**AcquireLicenseResponse**](-acquirelicenseresponse.md) objects that contain the signed use licenses, if granted.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/License.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

Starting with RMS 1.0 SP2, batch sizes greater than one are supported on enterprise servers. That is, the array of [**AcquireLicenseParams**](-acquirelicenseparams.md) objects that you send to the server can contain more than one element. Therefore, the array of [**AcquireLicenseResponse**](-acquirelicenseresponse.md) objects returned can contain multiple elements. One use license is retrieved for each valid request.

A single certificate chain returned by this function contains the common chain for the license. When a client receives this response, it must construct a certificate chain that a consuming application can use. For more information, see [**AcquireLicenseResponse**](-acquirelicenseresponse.md). You can use Windows Live ID with this function.

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

[**AcquireLicenseParams**](-acquirelicenseparams.md)
</dt> <dt>

[**AcquireLicenseResponse**](-acquirelicenseresponse.md)
</dt> </dl>

 

 




