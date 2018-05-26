---
Description: An issuance license can be created from scratch, from a template, or from an existing license by using the DRMCreateIssuanceLicense function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 495024be-5d97-4869-99f7-b68efb9e8039
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating an Issuance License
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating an Issuance License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An issuance license can be created from scratch, from a template, or from an existing license by using the [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) function. This function returns a pointer to a [**DRMPUBHANDLE**](drmpubhandle.md) value that contains the license handle. For more information, see the following topics:

-   [Creating a License From Scratch](creating-a-license-from-scratch.md)
-   [Creating a License From a Template](creating-a-license-from-a-template.md)
-   [Creating a License From a License](creating-a-license-from-a-license.md)

## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Issuance License XML Examples](issuance-license-xml-examples.md)
</dt> </dl>

 

 



