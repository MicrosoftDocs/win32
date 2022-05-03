---
title: Package query API
description: Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows app, and a manifest file that describes the software to Windows.
ms.assetid: EDDFC8B1-E224-4921-BED6-FC81711BA5BF
ms.topic: article
ms.date: 05/02/2022
ms.custom: 19H1
---

# Package query API

Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows app, and a manifest file that describes the software to Windows.

## In this section

| Topic | Description |
|-|-|
| [**ClosePackageInfo**](/windows/win32/api/appmodel/nf-appmodel-closepackageinfo) | Closes a reference to the specified package information. |
| [**FindPackagesByPackageFamily**](/windows/win32/api/appmodel/nf-appmodel-findpackagesbypackagefamily) | Finds the packages with the specified family name for the current user.  |
| [**FormatApplicationUserModelId**](/windows/win32/api/appmodel/nf-appmodel-formatapplicationusermodelid) | Constructs an [application user model ID](appx-packaging-glossary.md) from the package family name and the package relative application ID (PRAID).  |
| [**GetApplicationUserModelId**](/windows/win32/api/Appmodel/nf-appmodel-getapplicationusermodelid) | Gets the [application user model ID](appx-packaging-glossary.md) for the specified process. |
| [**GetApplicationUserModelIdFromToken**](/windows/win32/api/Appmodel/nf-appmodel-getapplicationusermodelidfromtoken) | Gets the [application user model ID](appx-packaging-glossary.md) for the specified token. |
| [**GetCurrentApplicationUserModelId**](/windows/win32/api/Appmodel/nf-appmodel-getcurrentapplicationusermodelid) | Gets the [application user model ID](appx-packaging-glossary.md) for the current process. |
| [**GetCurrentPackageFamilyName**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefamilyname) | Gets the package family name for the calling process. |
| [**GetCurrentPackageFullName**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefullname) | Gets the package full name for the calling process. |
| [**GetCurrentPackageId**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageid) | Gets the package identifier (ID) for the calling process. |
| [**GetCurrentPackageInfo**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo) | Gets the package information for the calling process. |
| [**GetCurrentPackageInfo2**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo2) | Gets the package information for the calling process, with the option to specify the package folder type. |
| [**GetCurrentPackageInfo3**](/windows/win32/appxpkg/appmodel/nf-appmodel-getcurrentpackageinfo3) | Gets the package information for the calling process, with the option to specify the package folder type. |
| [**GetCurrentPackagePath**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagepath) | Gets the package path for the calling process. |
| [**GetCurrentPackagePath2**](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagepath2) | Gets the package path for the calling process, with the option to specify the package folder type. |
| [**GetPackageApplicationIds**](/windows/win32/api/appmodel/nf-appmodel-getpackageapplicationids) | Gets the IDs of apps in the specified package. |
| [**GetPackageFamilyName**](/windows/win32/api/appmodel/nf-appmodel-getpackagefamilyname) | Gets the package family name for the specified process. |
| [**GetPackageFamilyNameFromToken**](/windows/win32/api/appmodel/nf-appmodel-getpackagefamilynamefromtoken) | Gets the package family name for the specified token. |
| [**GetPackageFullName**](/windows/win32/api/appmodel/nf-appmodel-getpackagefullname) | Gets the package full name for the specified process. |
| [**GetPackageFullNameFromToken**](/windows/win32/api/appmodel/nf-appmodel-getpackagefullnamefromtoken) | Gets the package full name for the specified token. |
| [**GetPackageId**](/windows/win32/api/appmodel/nf-appmodel-getpackageid) | Gets the package identifier (ID) for the specified process. |
| [**GetPackageInfo**](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo) | Gets the package information for the specified package. |
| [**GetPackageInfo2**](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo2) | Gets the package information for the specified package, with the option to specify the package folder type. |
| [**GetPackagePath**](/windows/win32/api/appmodel/nf-appmodel-getpackagepath) | Gets the path for the specified package. |
| [**GetPackagePathByFullName**](/windows/win32/api/appmodel/nf-appmodel-getpackagepathbyfullname) | Gets the path of the specified package. |
| [**GetPackagePathByFullName2**](/windows/win32/api/appmodel/nf-appmodel-getpackagepathbyfullname2) | Gets the path of the specified package, with the option to specify the package folder type. |
| [**GetPackagesByPackageFamily**](/windows/win32/api/appmodel/nf-appmodel-getpackagesbypackagefamily) | Gets the packages with the specified family name for the current user.  |
| [**GetStagedPackageOrigin**](/windows/win32/api/appmodel/nf-appmodel-getstagedpackageorigin) | Gets the origin of the specified package. |
| [**GetStagedPackagePathByFullName**](/windows/win32/api/appmodel/nf-appmodel-getstagedpackagepathbyfullname) | Gets the path of the specified staged package. |
| [**GetStagedPackagePathByFullName2**](/windows/win32/api/appmodel/nf-appmodel-getstagedpackagepathbyfullname2) | Gets the path of the specified staged package, with the option to specify the package folder type. |
| [**OpenPackageInfoByFullName**](/windows/win32/api/appmodel/nf-appmodel-openpackageinfobyfullname) | Opens the package information of the specified package. |
| [**PackageFamilyNameFromFullName**](/windows/win32/api/appmodel/nf-appmodel-packagefamilynamefromfullname) | Gets the package family name for the specified package full name. |
| [**PackageFamilyNameFromId**](/windows/win32/api/appmodel/nf-appmodel-packagefamilynamefromid) | Gets the package family name for the specified package identifier. |
| [**PackageFullNameFromId**](/windows/win32/api/appmodel/nf-appmodel-packagefullnamefromid) | Gets the package full name for the specified package identifier (ID). |
| [**PackageIdFromFullName**](/windows/win32/api/appmodel/nf-appmodel-packageidfromfullname) | Gets the package identifier (ID) for the specified package full name. |
| [**PackageNameAndPublisherIdFromFamilyName**](/windows/win32/api/appmodel/nf-appmodel-packagenameandpublisheridfromfamilyname) | Gets the package name and publisher identifier (ID) for the specified package family name. |
| [**ParseApplicationUserModelId**](/windows/win32/api/appmodel/nf-appmodel-parseapplicationusermodelid) | Deconstructs an [application user model ID](appx-packaging-glossary.md) to its package family name and package relative application ID (PRAID). |
| [**PackageOrigin**](/windows/win32/api/appmodel/ne-appmodel-packageorigin) | Specifies the origin of a package.  |
| [**Identity constants**](identity-constants.md) | Specifies the length of the strings for the package's identity fields. |
| [**Package constants**](package-constants.md) | Specifies how packages are to be processed. |
| [**PACKAGE\_ID**](/windows/win32/api/appmodel/ns-appmodel-package_id) | Represents package identification information, such as name, version, and publisher. |
| [**PACKAGE\_INFO**](/windows/win32/api/appmodel/ns-appmodel-package_info) | Represents package identification information that includes the package identifier, full name, and install location. |
| [**PACKAGE\_VERSION**](/windows/win32/api/appmodel/ns-appmodel-package_version) | Represents the package version information. |

## Related topics

**Conceptual**

* [App packages and deployment](/previous-versions/windows/apps/hh464929(v=win.10))
* [Glossary](appx-packaging-glossary.md)

**API reference**

* [App package manifest schema](/uwp/schemas/appxpackage/appx-package-manifest)
* [Packaging API](interfaces.md)
* [Package deployment API](package-deployment-api.md)
