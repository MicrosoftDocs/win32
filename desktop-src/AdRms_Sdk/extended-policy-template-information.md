---
Description: The extended rights policy of a template controls how content licenses are to be implemented.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4c5441a3-0b2f-4965-a15f-371f01bdee6d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Extended Policy Template Information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extended Policy Template Information

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The extended rights policy of a template controls how content licenses are to be implemented. The extended rights policy template settings are specified by using the Active Directory Rights Management Services (AD RMS) administration site. The available settings control persistence of author rights, whether trusted browsers are supported, license persistence within the content, and enforcement of any application-specific data.

If the **Require a new license each time content is consumed** setting is checked, the following XrML content is stored in the issuance license and use license. If this content is in a license, the application must not persist the end-user license for the AD RMS-protected document.

``` syntax
<AUTHENTICATEDDATA id="APPSPECIFIC"
 name="NOLICCACHE">1</AUTHENTICATEDDATA>
```

If the **RM-protected content can be viewed in trusted browsers** setting is checked, the following XrML content is stored in the issuance license and use license.

``` syntax
<AUTHENTICATEDDATA id="APPSPECIFIC"
 name="VIEWER">1</AUTHENTICATEDDATA>
```

If this content is in a license, then applications that choose to can publish the content in the MIME Encapsulation of Aggregate HTML Documents (MHTML) format. Content in the MHTML format can be viewed by the Active Directory Rights Management Add-on for Internet Explorer. For more information, see [Publishing Content](publishing-content.md).

> [!Note]  
> To programmatically extract information from the **AUTHENTICATEDDATA** node, use the [**DRMGetBoundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattribute) function with *wszAttribute* set to **g\_wszQUERY\_APPDATANAME**. [**DRMGetBoundLicenseAttributeCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattributecount) can be used to determine the count of such elements, and then **DRMGetBoundLicenseAttribute** can be used in a loop, with *wszAttribute* set to **g\_wszQUERY\_APPDATAVALUE**, to get the value of a specific element. See [Querying Licenses](querying-licenses.md) for more information about how to query a license programmatically.

 

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Templates](templates.md)
</dt> </dl>

 

 



