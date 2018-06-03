---
Description: A rights policy template is an extensible Rights Markup Language (XrML) version 1.2 document that can be applied to content and used to generate an issuance license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6b99d3d2-3144-450d-8e9d-18c881718ace
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a License From a Template
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a License From a Template

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A rights policy template is an extensible Rights Markup Language (XrML) version 1.2 document that can be applied to content and used to generate an issuance license. Templates can contain the following information:

-   A template name and description.
-   Users and groups that can be granted content licenses.
-   The rights and associated conditions granted to the users.
-   The content expiration policy.
-   A set of extended policies.
-   The template revocation policy.
-   A revocation list.
-   A revocation list refresh interval.
-   A public key file for the revocation list.

## Official Templates

Only the Active Directory Rights Management Services (AD RMS) administrator can create official rights policy templates for an organization. Because the server retains and uses the latest copy of a template when it signs a client issuance license, it is possible that the issuance license submitted by the client was created from an outdated and inaccurate template.

Beginning with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, the AD RMS client can automatically obtain templates from an AD RMS server by using a Windows Management Instrumentation (WMI) job in the task scheduler. If the task is enabled, the AD RMS application should call [**DRMEnumerateLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmenumeratelicense) to enumerate rights policy templates.

> [!Note]  
> Prior to Windows Vista with SP1 and Windows Server 2008, templates could only be distributed by using Group Policy, Systems Management Server, or an out-of-band mechanism.

 

## Unofficial Templates

If you are not an administrator, you can create unofficial templates by first calling [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense) and defining the appropriate validity period, users, rights, and metadata. For more information, see [Creating a License From Scratch](creating-a-license-from-scratch.md). Next call [**DRMGetIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetissuancelicensetemplate) and use the issuance license to create a rights policy template. This is shown in the following example.


```C++
// Call DRMCreateIssuanceLicense (not shown) to retrieve a handle 
// to an unsigned issuance license.
// Call DRMGetIssuanceLicenseTemplate once to retrieve the size of 
// the buffer needed to hold the template.
// Call DRMGetIssuanceLicenseTemplate again to retrieve the
// template.

hr = DRMGetIssuanceLicenseTemplate( 
       hIssuanceLicense,        // issuance license handle
       &amp;uLength,                // length of template buffer
       NULL);                   // NULL for first call
       );
if (FAILED(hr)) goto e_Exit;

// Allocate memory for the template.
PWSTR wszILTemplate = (PWSTR)HeapAlloc( 
       GetProcessHeap(), 
       HEAP_ZERO_MEMORY, 
       sizeof(WCHAR) * (uTLength + 1) );
if (NULL == wszIssuanceLicenseTemplate)
{
  hr = E_OUTOFMEMORY;
  goto e_Exit;
}

// Call DRMGetIssuanceLicenseTemplate again to create the
// template.
hr = DRMGetIssuanceLicenseTemplate( 
       hIssuanceLicense,        // issuance license handle
       &amp;uTLength,               // length of template buffer
       wszILTemplate);          // NULL for first call
       );
if (FAILED(hr)) goto e_Exit;

// Create an owner.
hr = DRMCreateUser( 
       L"someone@example.com",   // user name
       NULL,                     // user ID
       L"WINDOWS",               // type of user ID
       &amp;hOwner);                 // owner handle

// Create a new issuance license by using the template.
hr = DRMCreateIssuanceLicense( 
       &amp;stFrom,                  // starting validity time
       &amp;stUntil,                 // ending validity time
       NULL,                     // display name for URL
       NULL,                     // referral URL
       hOwner,                   // optional owner handle
       wszILTemplate,            // issuance license template 
       NULL,                     // bound license handle
       &amp;hIssuanceLicense);       // issuance license handle
if (FAILED(hr)) goto e_Exit;

e_Exit:

// Perform cleanup and return.
```



> \[!Important\]If the issuance license does not contain metadata, the call to [**DRMGetIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetissuancelicensetemplate) will fail.
>
> Also, when creating issuance licenses that are valid for short time periods, the problem of clock skew can cause failure when the end user attempts to exercise rights. Clock skew occurs when the clocks on the server and client are not exactly aligned. For more information, see [Clock Skew](clock-skew.md).

 

## Related topics

<dl> <dt>

[Creating an Issuance License](creating-an-issuance-license.md)
</dt> <dt>

[Creating a License From a License](creating-a-license-from-a-license.md)
</dt> <dt>

[Creating a License From Scratch](creating-a-license-from-scratch.md)
</dt> </dl>

 

 



