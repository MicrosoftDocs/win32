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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a License From a License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The *hBoundLicense* parameter in the [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) function enables an application to reuse data from an existing issuance license when creating a new license. To reuse an existing license, your application can perform the following steps:

1.  Obtain a signed issuance license for which the user is granted the VIEWRIGHTSDATA or OWNER right.
2.  Call [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master) to bind to the license. For a complete source code example that shows how to bind to a license, see the [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md) topic in the discussion of content decryption later in this documentation.
3.  Call [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master), passing in the bound license handle and the signed issuance license or template. The following data is retrieved from the existing license:
    -   Users (from [**DRMCreateUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateuser?branch=master))
    -   Rights (from [**DRMCreateRight**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateright?branch=master))
    -   Application-specific data (from [**DRMSetApplicationSpecificData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetapplicationspecificdata?branch=master))
    -   Metadata (from [**DRMSetMetaData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetmetadata?branch=master))
    -   Name and description (from [**DRMSetNameAndDescription**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetnameanddescription?branch=master))
    -   Revocation point (from [**DRMSetRevocationPoint**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetrevocationpoint?branch=master))
    -   Usage policy (from [**DRMSetUsagePolicy**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetusagepolicy?branch=master))

## Related topics

<dl> <dt>

[Creating an Issuance License](creating-an-issuance-license.md)
</dt> <dt>

[Creating a License From a Template](creating-a-license-from-a-template.md)
</dt> <dt>

[Creating a License From Scratch](creating-a-license-from-scratch.md)
</dt> </dl>

 

 



