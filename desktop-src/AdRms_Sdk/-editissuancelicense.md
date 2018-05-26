---
Description: The EditIssuanceLicense SOAP web method creates a new signed issuance license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ad22a0bc-8b75-4534-a94a-4520e2397371
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EditIssuanceLicense method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EditIssuanceLicense method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **EditIssuanceLicense** SOAP web method creates a new signed [*issuance license*](i-gly.md#-rm-issuance-license-gly). This method accomplishes this by performing the following steps:

1.  Put the content key from the supplied signed issuance license into the new issuance license.
2.  Sign the new issuance license.
3.  Return the new, signed issuance license.

> \[!Important\]  
> When you use this method to enable license republishing, keep in mind that the content key for the file does not change. An implication of this is that it may be possible for users who have been added to the license to continue to access the content, even after they have been subsequently removed from the license.

 

> \[!Important\]  
> The **EditIssuanceLicense** method on AD RMS has its access control list (ACL) set to "System" by default. To use this method, you must change the ACL for EditIssuanceLicense.asmx to a value that will allow this function to be used. It is very important to understand that only approved computers or (occasionally) users should have access to this function because anyone with access to this function can gain full rights to any license with the "Allow\_Server\_Editing"/"True" pair issued by this service.

 

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public EditIssuanceLicenseResponse[] EditIssuanceLicense(
  EditIssuanceLicenseParams[] RequestParams
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
<td><pre><code>Public Function EditIssuanceLicense( _
  ByVal RequestParams() As EditIssuanceLicenseParams _
) As EditIssuanceLicenseResponse()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*RequestParams* 
</dt> <dd>

An array of [**EditIssuanceLicenseParams**](-editissuancelicenseparams.md) objects that contains the signed issuance license and the new issuance license with the new rights to incorporate.

> [!Note]  
> Servers will only accept requests that consist of arrays that contain a single element. All other requests will fail.

 

</dd> </dl>

## Return value

An array of [**EditIssuanceLicenseResponse**](-editissuancelicenseresponse.md) objects that contains the new signed issuance license chain. The new issuance license contains the content key from the old issuance license.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/EditIssuanceLicense.asmx

## Remarks

The **VersionDataValue** and **Credentials** properties of the SOAP proxy object must be set before calling this method.

For this request to succeed, a requesting party must be on a list of allowed editors created by the AD RMS administrator, the license to republish must be a valid signed issuance license from this deployment, and the issuance license must include the application-specific tag "Allow\_Server\_Editing", with the (string) value "True". This value is added during issuance license creation by using the [**DRMSetApplicationSpecificData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetapplicationspecificdata?branch=master) method.

This function validates the received signed issuance license before processing any further.

## Requirements



|                    |                                                        |
|--------------------|--------------------------------------------------------|
| Product<br/> | Rights Management Services 1.0 SP2 or later<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**EditIssuanceLicenseParams**](-editissuancelicenseparams.md)
</dt> <dt>

[**EditIssuanceLicenseResponse**](-editissuancelicenseresponse.md)
</dt> </dl>

 

 




