---
title: Package query API
description: Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.
ms.assetid: EDDFC8B1-E224-4921-BED6-FC81711BA5BF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Package query API

Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.

## In this section



| Topic                                                                                                 | Description                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClosePackageInfo**](/windows/win32/AppModel/nf-appmodel-closepackageinfo?branch=master)<br/>                                               | Closes a reference to the specified package information.<br/>                                                                                              |
| [**FindPackagesByPackageFamily**](/windows/win32/AppModel/nf-appmodel-findpackagesbypackagefamily?branch=master)<br/>                         | Finds the packages with the specified family name for the current user. <br/>                                                                              |
| [**FormatApplicationUserModelId**](/windows/win32/AppModel/nf-appmodel-formatapplicationusermodelid?branch=master)<br/>                       | Constructs an [application user model ID](appx-packaging-glossary.md) from the package family name and the package relative application ID (PRAID). <br/> |
| [**GetApplicationUserModelId**](/windows/win32/Appmodel/nf-appmodel-getapplicationusermodelid?branch=master)<br/>                             | Gets the [application user model ID](appx-packaging-glossary.md) for the specified process.<br/>                                                          |
| [**GetApplicationUserModelIdFromToken**](/windows/win32/Appmodel/nf-appmodel-getapplicationusermodelidfromtoken?branch=master)<br/>           | Gets the [application user model ID](appx-packaging-glossary.md) for the specified token.<br/>                                                            |
| [**GetCurrentApplicationUserModelId**](/windows/win32/Appmodel/nf-appmodel-getcurrentapplicationusermodelid?branch=master)<br/>               | Gets the [application user model ID](appx-packaging-glossary.md) for the current process.<br/>                                                            |
| [**GetCurrentPackageFamilyName**](/windows/win32/AppModel/nf-appmodel-getcurrentpackagefamilyname?branch=master)<br/>                         | Gets the package family name for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackageFullName**](/windows/win32/AppModel/nf-appmodel-getcurrentpackagefullname?branch=master)<br/>                             | Gets the package full name for the calling process.<br/>                                                                                                   |
| [**GetCurrentPackageId**](/windows/win32/AppModel/nf-appmodel-getcurrentpackageid?branch=master)<br/>                                         | Gets the package identifier (ID) for the calling process.<br/>                                                                                             |
| [**GetCurrentPackageInfo**](/windows/win32/AppModel/nf-appmodel-getcurrentpackageinfo?branch=master)<br/>                                     | Gets the package information for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackagePath**](/windows/win32/AppModel/nf-appmodel-getcurrentpackagepath?branch=master)<br/>                                     | Gets the package path for the calling process.<br/>                                                                                                        |
| [**GetPackageApplicationIds**](/windows/win32/AppModel/nf-appmodel-getpackageapplicationids?branch=master)<br/>                               | Gets the IDs of apps in the specified package.<br/>                                                                                                        |
| [**GetPackageFamilyName**](/windows/win32/AppModel/nf-appmodel-getpackagefamilyname?branch=master)<br/>                                       | Gets the package family name for the specified process.<br/>                                                                                               |
| [**GetPackageFamilyNameFromToken**](/windows/win32/AppModel/nf-appmodel-getpackagefamilynamefromtoken?branch=master)<br/>                     | Gets the package family name for the specified token.<br/>                                                                                                 |
| [**GetPackageFullName**](/windows/win32/AppModel/nf-appmodel-getpackagefullname?branch=master)<br/>                                           | Gets the package full name for the specified process.<br/>                                                                                                 |
| [**GetPackageFullNameFromToken**](/windows/win32/AppModel/nf-appmodel-getpackagefullnamefromtoken?branch=master)<br/>                         | Gets the package full name for the specified token.<br/>                                                                                                   |
| [**GetPackageId**](/windows/win32/AppModel/nf-appmodel-getpackageid?branch=master)<br/>                                                       | Gets the package identifier (ID) for the specified process.<br/>                                                                                           |
| [**GetPackageInfo**](/windows/win32/AppModel/nf-appmodel-getpackageinfo?branch=master)<br/>                                                   | Gets the package information for the specified package.<br/>                                                                                               |
| [**GetPackagePath**](/windows/win32/AppModel/nf-appmodel-getpackagepath?branch=master)<br/>                                                   | Gets the path for the specified package.<br/>                                                                                                              |
| [**GetPackagePathByFullName**](/windows/win32/AppModel/nf-appmodel-getpackagepathbyfullname?branch=master)<br/>                               | Gets the path of the specified package.<br/>                                                                                                               |
| [**GetPackagesByPackageFamily**](/windows/win32/AppModel/nf-appmodel-getpackagesbypackagefamily?branch=master)<br/>                           | Gets the packages with the specified family name for the current user. <br/>                                                                               |
| [**GetStagedPackageOrigin**](/windows/win32/AppModel/nf-appmodel-getstagedpackageorigin?branch=master)<br/>                                   | Gets the origin of the specified package.<br/>                                                                                                             |
| [**GetStagedPackagePathByFullName**](/windows/win32/AppModel/nf-appmodel-getstagedpackagepathbyfullname?branch=master)<br/>                   | Gets the path of the specified staged package.<br/>                                                                                                        |
| [**OpenPackageInfoByFullName**](/windows/win32/AppModel/nf-appmodel-openpackageinfobyfullname?branch=master)<br/>                             | Opens the package information of the specified package.<br/>                                                                                               |
| [**PackageFamilyNameFromFullName**](/windows/win32/AppModel/nf-appmodel-packagefamilynamefromfullname?branch=master)<br/>                     | Gets the package family name for the specified package full name.<br/>                                                                                     |
| [**PackageFamilyNameFromId**](/windows/win32/AppModel/nf-appmodel-packagefamilynamefromid?branch=master)<br/>                                 | Gets the package family name for the specified package identifier.<br/>                                                                                    |
| [**PackageFullNameFromId**](/windows/win32/AppModel/nf-appmodel-packagefullnamefromid?branch=master)<br/>                                     | Gets the package full name for the specified package identifier (ID).<br/>                                                                                 |
| [**PackageIdFromFullName**](/windows/win32/AppModel/nf-appmodel-packageidfromfullname?branch=master)<br/>                                     | Gets the package identifier (ID) for the specified package full name.<br/>                                                                                 |
| [**PackageNameAndPublisherIdFromFamilyName**](/windows/win32/AppModel/nf-appmodel-packagenameandpublisheridfromfamilyname?branch=master)<br/> | Gets the package name and publisher identifier (ID) for the specified package family name.<br/>                                                            |
| [**ParseApplicationUserModelId**](/windows/win32/AppModel/nf-appmodel-parseapplicationusermodelid?branch=master)<br/>                         | Deconstructs an [application user model ID](appx-packaging-glossary.md) to its package family name and package relative application ID (PRAID).<br/>      |
| [**PackageOrigin**](/windows/win32/AppModel/ne-appmodel-packageorigin?branch=master)<br/>                                                     | Specifies the origin of a package. <br/>                                                                                                                   |
| [**Identity constants**](identity-constants.md)<br/>                                           | Specifies the length of the strings for the package's identity fields.<br/>                                                                                |
| [**Package constants**](package-constants.md)<br/>                                             | Specifies how packages are to be processed.<br/>                                                                                                           |
| [**PACKAGE\_ID**](/windows/win32/AppModel/ns-appmodel-package_id?branch=master)<br/>                                                          | Represents package identification information, such as name, version, and publisher.<br/>                                                                  |
| [**PACKAGE\_INFO**](/windows/win32/AppModel/ns-appmodel-package_info?branch=master)<br/>                                                      | Represents package identification information that includes the package identifier, full name, and install location.<br/>                                  |
| [**PACKAGE\_VERSION**](/windows/win32/AppModel/ns-appmodel-package_version?branch=master)<br/>                                                | Represents the package version information.<br/>                                                                                                           |



 

## Related topics

<dl> <dt>

**Concepts**
</dt> <dt>

[App packages and deployment](https://msdn.microsoft.com/library/windows/apps/hh464929)
</dt> <dt>

[Glossary](appx-packaging-glossary.md)
</dt> <dt>

**Reference**
</dt> <dt>

[App package manifest schema](https://msdn.microsoft.com/library/windows/apps/br211474)
</dt> <dt>

[Packaging API](interfaces.md)
</dt> <dt>

[Package deployment API](package-deployment-api.md)
</dt> </dl>

 

 





