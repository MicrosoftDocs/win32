---
Description: After creating an issuance license, you can add users and rights to it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 712e3ae7-c7c3-4a98-9593-86d17564dc96
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Adding Information to a License
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Information to a License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

After creating an [*issuance license*](https://www.bing.com/search?q=*issuance license*), you can add users and rights to it. Note that rights are case-sensitive. That is, you should add the EDIT right, not the Edit right. The following example shows how to create a user and an EDIT right, and how to grant that right to the user.

> [!Note]  
> The owner specified by *hOwner* in [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense) is the Owner principal, not the OWNER right. Merely specifying someone as the *hOwner* in **DRMCreateIssuanceLicense** does not grant them the OWNER right; granting yourself (or anyone else) the OWNER right must be done explicitly by using [**DRMAddRightWithUser**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmaddrightwithuser). Zero, one, or more users can be granted the OWNER right, which never expires. For more information, see the *hOwner* parameter of **DRMCreateIssuanceLicense**.

 


```C++
int AddMetadata(DRMPUBHANDLE* phIssuanceLicense)
{
  HRESULT hr = S_OK;
  DRMPUBHANDLE hUser;
  DRMPUBHANDLE hRight;
  GUID guid;
  LPWSTR wszGUID;
  DWORD uiGUIDLength;
  SYSTEMTIME stTimeFrom;
  SYSTEMTIME stTimeUntil;

  // Create a user.
  hr = DRMCreateUser( 
          L"someone@example.com",   // user name
          L"MyID",                  // user ID
          L"Windows",               // type of user ID
          &amp;hUser                    // user object handle 
          );     
  if(FAILED(hr)) goto e_Exit;

  // Create a right for the user.
  hr = DRMCreateRight( 
          L"EDIT",            // name of the right
          &amp;stTimeFrom,        // beginning validity time
          &amp;stTimeUntil,       // ending validity time
          0,                  // count of extended elements
          NULL,               // extended information name
          NULL,               // extended information value
          &amp;hRight             // rights object handle
          );
  if(FAILED(hr)) goto e_Exit;

  // Add the right and user to the license.
  hr = DRMAddRightWithUser( 
          *phIssuanceLicense, // issuance license handle
          hRight,             // handle of right to add
          hUser );            // handle of user to add
  if(FAILED(hr)) goto e_Exit;

  // Add metadata to the license.
  // Create a GUID to use as a unique content ID.
  hr = CoCreateGuid( &amp;guid );
  if(FAILED(hr)) goto e_Exit;

  wszGUID = new WCHAR[ GUID_STRING_LENGTH ];
  if(FAILED(hr)) goto e_Exit;

  uiGUIDLength = StringFromGUID2( 
          guid, 
          wszGUID, 
          GUID_STRING_LENGTH );
  if( 0 == uiGUIDLength )
  {
     hr = E_FAIL;
     goto e_Exit;
  }

  // Set the content ID in the issuance license.
  hr = DRMSetMetaData( 
          *phIssuanceLicense,   // issuance license handle
          wszGUID,              // content ID
          L"MS-GUID",           // type of content ID
          NULL,                 // optional SKU ID
          NULL,                 // SKU ID type
          NULL,                 // content type
          NULL                  // content name
          );
  if(FAILED(hr)) goto e_Exit;

e_Exit:

  // Perform cleanup and return.

  return hr;
}
```



After you create an [*issuance license*](https://www.bing.com/search?q=*issuance license*) and add users and rights to it, you can add other information to it as well:

-   To add name-value pairs that contain custom values, use the [**DRMSetApplicationSpecificData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetapplicationspecificdata) function. This data can be used by a consuming application to perform many tasks.
-   To add names and descriptions of the license in multiple human languages, use the [**DRMSetNameAndDescription**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetnameanddescription) function.
-   To add a revocation point, use the [**DRMSetRevocationPoint**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetrevocationpoint) function. A revocation point is a location where an application can download a revocation list that describes users, machine certificates, and many other principals that should be prevented from using a use license.
-   To add restrictions on what applications must or cannot use this license, use [**DRMSetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetusagepolicy).

## Related topics

<dl> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



