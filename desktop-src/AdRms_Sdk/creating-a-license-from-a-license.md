---
Description: The hBoundLicense parameter in the DRMCreateIssuanceLicense function enables an application to reuse data from an existing issuance license when creating a new license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 143f6a53-3b3e-433d-8e16-9b1f1c6cbbc0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a License From a License
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a License From a License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The *hBoundLicense* parameter in the [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense) function enables an application to reuse data from an existing issuance license when creating a new license. To reuse an existing license, your application can perform the following steps:

1.  Obtain a signed issuance license for which the user is granted the VIEWRIGHTSDATA or OWNER right.
2.  Call [**DRMCreateBoundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateboundlicense) to bind to the license. For a complete source code example that shows how to bind to a license, see the [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md) topic in the discussion of content decryption later in this documentation.
3.  Call [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense), passing in the bound license handle and the signed issuance license or template. The following data is retrieved from the existing license:
    -   Users (from [**DRMCreateUser**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateuser))
    -   Rights (from [**DRMCreateRight**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateright))
    -   Application-specific data (from [**DRMSetApplicationSpecificData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetapplicationspecificdata))
    -   Metadata (from [**DRMSetMetaData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetmetadata))
    -   Name and description (from [**DRMSetNameAndDescription**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetnameanddescription))
    -   Revocation point (from [**DRMSetRevocationPoint**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetrevocationpoint))
    -   Usage policy (from [**DRMSetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetusagepolicy))

## Related topics

<dl> <dt>

[Creating an Issuance License](creating-an-issuance-license.md)
</dt> <dt>

[Creating a License From a Template](creating-a-license-from-a-template.md)
</dt> <dt>

[Creating a License From Scratch](creating-a-license-from-scratch.md)
</dt> </dl>

 

 



