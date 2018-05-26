---
title: Creating the Security Catalog
description: The security catalog contains the cryptographic hashes of all files included in the troubleshooting pack.
ms.assetid: 294eef16-25c3-4e42-99db-297a692eea2d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the Security Catalog

The security catalog contains the cryptographic hashes of all files included in the troubleshooting pack. When you run a troubleshooting pack, WTP gets the security catalog from the pack's folder and confirms that the files in the folder match those specified in the security catalog. If any of the files have been modified or if there are any additional unsigned files present, the pack is not run. The security catalog must be code signed by a certificate that chains up to a trusted root authority on the computer. For details, see [Signing the Security Catalog](signing-the-security-catalog.md).

The name of the security catalog must be DiagPackage.cat.

To create a security catalog, use the [**Makecat.exe**](https://msdn.microsoft.com/library/windows/desktop/aa386967) tool that is included in the \\Bin folder of the Windows SDK. The following shows an example .cdf file for the PopupBlocker troubleshooting example:

``` syntax
[CatalogHeader]
Name=DiagPackage.cat              
PublicVersion=0x0000001
EncodingType=0x00010001
CATATTR1=0x10010001:OSAttr:2:6.1 

[CatalogFiles]
<hash>PopupBlocker.diagpkg=PopupBlocker.diagpkg
<hash>PopupBlocker.diagpkgATTR1=0x10010001:Filename:PopupBlocker.diagpkg
<hash>DetectPopupBlockerSettings.ps1=DetectPopupBlockerSettings.ps1
<hash>DetectPopupBlockerSettings.ps1ATTR1=0x10010001:Filename:DetectPopupBlockerSettings.ps1
<hash>ResolvePopupBlockerSettings.ps1=ResolvePopupBlockerSettings.ps1
<hash>ResolvePopupBlockerSettings.ps1ATTR1=0x10010001:Filename:ResolvePopupBlockerSettings.ps1
<hash>PopupBlocker.cdf=PopupBlocker.cdf
<hash>PopupBlocker.cdfATTR1=0x10010001:Filename:PopupBlocker.cdf
```

Note that if the pack was localized, the .cdf file must also contain an entry for the language-neutral resource DLL. For details on creating a security catalog for localized resources, see [Localizing the Troubleshooting Pack](localizing-the-troubleshooting-package.md).

The following command creates the catalog file.

**makecat -v PopupBlocker.cdf**

 

 




