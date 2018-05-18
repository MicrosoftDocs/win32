---
title: How-to add explicit owner rights
description: Your application should explicitly add \ 0034;Owner \ 0034; rights when creating a license from scratch (IpcCreateLicenseFromScratch).
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'EF43FAC4-ABB4-459D-B173-972B5716F816'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How-to: add explicit owner rights

Your application should explicitly add "Owner" rights when creating a license from scratch ([**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)).

### Prerequisites

When your application is creating a license handle using [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md), it must also grant the owner full rights (permissions) explicitly.

> [!Note]  
> Setting a user as "owner" using [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md) with the **IPC\_LI\_OWNER** property does not grant the owner full permissions.

 

The following example code only represents the steps involved in creating and adding the specific rights to a given license.

## Instructions

### Step 1: Example scenario

In this example, needed rights are added to a license created with [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md). The example shows the creation and assignment of the rights to the license through a rights list.

The following two rights are added to these users:

-   *Read* permissions assigned to joe@contoso.com
-   *Full* permissions assigned to mary\_kay@contoso.com


```C++
    
// Create User Rights structure 
IPC_USER_RIGHTS ownerRightForOwner = {0};

// Create rights
LPCWSTR rgwszOwnerRights[1] = {IPC_GENERIC_ALL};

// Assign values to members of Rights structure
ownerRightForOwner.User.dwType = IPC_USER_TYPE_IPC;
ownerRightForOwner.User.wszID = IPC_USER_ID_OWNER;
ownerRightForOwner.rgwszRights = rgwszOwnerRights;
ownerRightForOwner.cRights = 1;

// Create User Rights structure for Joe with Read permissions
IPC_USER_RIGHTS joeReadRight = {0};
LPCWSTR rgwszReadRights[1] = {IPC_GENERIC_READ};

// Assign values to members of Rights structure for Joe
joeReadRight.User.dwType = IPC_USER_TYPE_EMAIL;
joeReadRight.User.wszID = L"joe@contoso.com";
joeReadRight.rgwszRights = rgwszReadRights;
joeReadRight.cRights = 1;

// Create User Rights structure for Mary Kay with Full permissions
IPC_USER_RIGHTS mary_kayFullRight = {0};
LPCWSTR rgwszFullRights[1] = {IPC_GENERIC_ALL};

// Assign values to members of Rights structure for Mary Kay
mary_kayFullRight.User.dwType = IPC_USER_TYPE_EMAIL;
mary_kayFullRight.User.wszID = L"mary_kay@contoso.com";
mary_kayFullRight.rgwszRights = rgwszFullRights;
mary_kayFullRight.cRights = 1;

// Create User Rights List and assign the above rights
size_t uNoOfUserRights = 3;
PIPC_USER_RIGHTS_LIST pUserRightsList = NULL;
pUserRightsList = reinterpret_cast<PIPC_USER_RIGHTS_LIST>(new BYTE[ sizeof(IPC_USER_RIGHTS_LIST) +
    uNoOfUserRights * sizeof(IPC_USER_RIGHTS)]);

if(pUserRightsList == NULL)
{
    // Handle error
}

// Assign values to members of Rights List structure for Joe and Mary Kay
(*pUserRightsList).cbSize = sizeof(IPC_USER_RIGHTS_LIST);
(*pUserRightsList).cUserRights = uNoOfUserRights;
(*pUserRightsList).rgUserRights[0] = ownerRightForOwner;
(*pUserRightsList).rgUserRights[1] = joeReadRight;
(*pUserRightsList).rgUserRights[2] = mary_kayFullRight;

    
// Set the Rights List property on the license via its handle
// hLicense is a license handle created with IpcCreateLicenseFromScratch
hr = IpcSetLicenseProperty(hLicense, FALSE, IPC_LI_USER_RIGHTS_LIST, pUserRightsList);
    
if(FAILED(hr))
{
    // Handle the error
}
```



## Related topics

<dl> <dt>

[Developer notes](developer-notes.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> </dl>

 

 




