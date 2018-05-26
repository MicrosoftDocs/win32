---
Description: The following steps discuss how you can create an issuance license by using only the functions contained in the Active Directory Rights Management Services (AD RMS) SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0eebfdad-682d-45d7-a441-a8a5e6ff79c0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a License From Scratch
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a License From Scratch

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following steps discuss how you can create an issuance license by using only the functions contained in the Active Directory Rights Management Services (AD RMS) SDK.

-   Call [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) to create an empty license.
-   Call [**DRMCreateUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateuser?branch=master) to create a user object.
-   Call [**DRMCreateRight**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateright?branch=master) to create a right for the user.
-   Call [**DRMAddRightWithUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmaddrightwithuser?branch=master) to bind the right and user to the license.
-   Create appropriate metadata and call [**DRMSetMetaData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetmetadata?branch=master) to set it in the license.
-   Call [**DRMSetApplicationSpecificData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetapplicationspecificdata?branch=master) to specify custom information, if any, that can be understood by the consuming application.

These steps are shown by the following code example. For a more complete example, see [OfflineSigning\_GetSignedIL.cpp](offlinesigning-getsignedil-cpp.md).


```C++
// Retrieve the system time to define the validity period
// for the unsigned issuance license.
GetSystemTime( &amp;stTimeFrom );
GetSystemTime( &amp;stTimeUntil );
stTimeUntil.wYear++;

// Create an issuance license, user, and right. Add the 
// right and user pair to the issuance license.
hr = DRMCreateIssuanceLicense( 
        &amp;stTimeFrom,         // starting validity time
        &amp;stTimeUntil,        // ending validity time
        NULL,                // display name for referral URL
        NULL,                // referral URL
        NULL,                // optional owner handle
        NULL,                // issuance license template string
        NULL,                // bound license handle
        &amp;hIssuanceLicense);  // pointer to issuance license
if (FAILED(hr)) goto e_Exit;

// Create a user object.
hr = DRMCreateUser( 
        wszUserId,           // user name
        NULL,                // user ID
        L"Unspecified",      // type of user ID
        &amp;hUser);             // user object handle 
if (FAILED(hr)) goto e_Exit;

// Create a right for the user.
hr = DRMCreateRight( 
        L"EDIT",              // name of the right
        &amp;stTimeFrom,          // beginning validity time
        &amp;stTimeUntil,         // ending validity time
        0,                    // count of extended elements
        NULL,                 // extended information name
        NULL,                 // extended information value
        &amp;hRight);             // rights object handle
if (FAILED(hr)) goto e_Exit;

// Add the right and user to the license.
hr = DRMAddRightWithUser( 
        hIssuanceLicense,     // issuance license handle
        hRight,               // handle of right to add
        hUser );              // handle of user to add
if (FAILED(hr))goto e_Exit;

// Add metadata to the license.
// Create a GUID to use as a unique content ID.
hr = CoCreateGuid( &amp;guid );
if (FAILED(hr)) goto e_Exit;

wwszGUID = new WCHAR[GUID_LENGTH];
if (NULL == wszGUID)
{
  hr = E_OUTOFMEMORY;
  goto e_Exit;
}

uiGUIDLength = StringFromGUID2( guid, pwszGUID, GUID_LENGTH );
if (0 == uiGUIDLength)
{
  hr = E_FAIL;
  goto e_Exit;
}

// Set the content ID in the issuance license.
hr = DRMSetMetaData( 
        hIssuanceLicense,     // issuance license handle
        wszGUID,              // content ID
        L"MS-GUID",           // type of content ID
        NULL,                 // optional SKU ID
        NULL,                 // SKU ID type
        NULL,                 // content type
        NULL);                // content name

e_Exit:

// Perform cleanup and return.
```



To specify an owner for the issuance license, call the [**DRMCreateUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateuser?branch=master) function before calling the [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) function as shown in the following example.

> [!Note]  
> When creating an application using the AD RMS SDK, if your intention is that the user creating the protected content has OWNER rights on the content, then you must explicitly add the OWNER right for that user to the issuance license. Do this by calling [**DRMAddRightWithUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmaddrightwithuser?branch=master). Additionally, take note that the owner specified by *hOwner* is the Owner principal, not the OWNER right. Merely specifying someone as the *hOwner* does not grant them the OWNER right; granting yourself (or anyone else) the OWNER right must be done explicitly by using **DRMAddRightWithUser**. Zero, one, or more users can be granted the OWNER right, which never expires. For more information, see the *hOwner* parameter of [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master).

 


```C++
// Create the owner.
hr = DRMCreateUser( 
        L"someone@example.com",   // user name
        NULL,                     // user ID
        L"WINDOWS",               // type of user ID
        &amp;hOwner);                 // owner handle

if (FAILED(hr)) goto e_Exit;

// Create the empty issuance license.
hr = DRMCreateIssuanceLicense( 
        &amp;stTimeFrom,              // starting validity time
        &amp;stTimeUntil,             // ending validity time
        NULL,                     // display name for URL
        NULL,                     // referral URL
        hOwner,                   // optional owner handle
        NULL,                     // issuance license template
        NULL,                     // bound license handle
        &amp;hIssuanceLicense);       // issuance license handle
          );
if (FAILED(hr)) goto e_Exit;
```



## Related topics

<dl> <dt>

[Creating an Issuance License](creating-an-issuance-license.md)
</dt> <dt>

[Creating a License From a License](creating-a-license-from-a-license.md)
</dt> <dt>

[Creating a License From a Template](creating-a-license-from-a-template.md)
</dt> </dl>

 

 



