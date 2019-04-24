---
title: Package query API
description: Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.
ms.assetid: EDDFC8B1-E224-4921-BED6-FC81711BA5BF
ms.topic: article
ms.date: 05/31/2018
ms.custom: 19H1
---

# Package query API

Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.

## In this section



| Topic                                                                                                 | Description                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClosePackageInfo**](/windows/desktop/api/AppModel/nf-appmodel-closepackageinfo)<br/>                                               | Closes a reference to the specified package information.<br/>                                                                                              |
| [**FindPackagesByPackageFamily**](/windows/desktop/api/AppModel/nf-appmodel-findpackagesbypackagefamily)<br/>                         | Finds the packages with the specified family name for the current user. <br/>                                                                              |
| [**FormatApplicationUserModelId**](/windows/desktop/api/AppModel/nf-appmodel-formatapplicationusermodelid)<br/>                       | Constructs an [application user model ID](appx-packaging-glossary.md) from the package family name and the package relative application ID (PRAID). <br/> |
| [**GetApplicationUserModelId**](/windows/desktop/api/Appmodel/nf-appmodel-getapplicationusermodelid)<br/>                             | Gets the [application user model ID](appx-packaging-glossary.md) for the specified process.<br/>                                                          |
| [**GetApplicationUserModelIdFromToken**](/windows/desktop/api/Appmodel/nf-appmodel-getapplicationusermodelidfromtoken)<br/>           | Gets the [application user model ID](appx-packaging-glossary.md) for the specified token.<br/>                                                            |
| [**GetCurrentApplicationUserModelId**](/windows/desktop/api/Appmodel/nf-appmodel-getcurrentapplicationusermodelid)<br/>               | Gets the [application user model ID](appx-packaging-glossary.md) for the current process.<br/>                                                            |
| [**GetCurrentPackageFamilyName**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackagefamilyname)<br/>                         | Gets the package family name for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackageFullName**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackagefullname)<br/>                             | Gets the package full name for the calling process.<br/>                                                                                                   |
| [**GetCurrentPackageId**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackageid)<br/>                                         | Gets the package identifier (ID) for the calling process.<br/>                                                                                             |
| [**GetCurrentPackageInfo**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackageinfo)<br/>                                     | Gets the package information for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackageInfo2**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackageinfo2)<br/>                                     | Gets the package information for the calling process, with the option to specify the package folder type.<br/>                                                                                               |
| [**GetCurrentPackagePath**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackagepath)<br/>                                     | Gets the package path for the calling process.<br/>                                                                                                        |
| [**GetCurrentPackagePath2**](/windows/desktop/api/AppModel/nf-appmodel-getcurrentpackagepath2)<br/>                                     | Gets the package path for the calling process, with the option to specify the package folder type.<br/>                                                                                                        |
| [**GetPackageApplicationIds**](/windows/desktop/api/AppModel/nf-appmodel-getpackageapplicationids)<br/>                               | Gets the IDs of apps in the specified package.<br/>                                                                                                        |
| [**GetPackageFamilyName**](/windows/desktop/api/AppModel/nf-appmodel-getpackagefamilyname)<br/>                                       | Gets the package family name for the specified process.<br/>                                                                                               |
| [**GetPackageFamilyNameFromToken**](/windows/desktop/api/AppModel/nf-appmodel-getpackagefamilynamefromtoken)<br/>                     | Gets the package family name for the specified token.<br/>                                                                                                 |
| [**GetPackageFullName**](/windows/desktop/api/AppModel/nf-appmodel-getpackagefullname)<br/>                                           | Gets the package full name for the specified process.<br/>                                                                                                 |
| [**GetPackageFullNameFromToken**](/windows/desktop/api/AppModel/nf-appmodel-getpackagefullnamefromtoken)<br/>                         | Gets the package full name for the specified token.<br/>                                                                                                   |
| [**GetPackageId**](/windows/desktop/api/AppModel/nf-appmodel-getpackageid)<br/>                                                       | Gets the package identifier (ID) for the specified process.<br/>                                                                                           |
| [**GetPackageInfo**](/windows/desktop/api/AppModel/nf-appmodel-getpackageinfo)<br/>                                                   | Gets the package information for the specified package.<br/>                                                                                               |
| [**GetPackageInfo2**](/windows/desktop/api/AppModel/nf-appmodel-getpackageinfo2)<br/>                                                   | Gets the package information for the specified package, with the option to specify the package folder type.<br/>                                                                                               |
| [**GetPackagePath**](/windows/desktop/api/AppModel/nf-appmodel-getpackagepath)<br/>                                                   | Gets the path for the specified package.<br/>                                                                                                              |
| [**GetPackagePathByFullName**](/windows/desktop/api/AppModel/nf-appmodel-getpackagepathbyfullname)<br/>                               | Gets the path of the specified package.<br/>                                                                                                               |
| [**GetPackagePathByFullName2**](/windows/desktop/api/AppModel/nf-appmodel-getpackagepathbyfullname2)<br/>                               | Gets the path of the specified package, with the option to specify the package folder type.<br/>                                                                                                               |
| [**GetPackagesByPackageFamily**](/windows/desktop/api/AppModel/nf-appmodel-getpackagesbypackagefamily)<br/>                           | Gets the packages with the specified family name for the current user. <br/>                                                                               |
| [**GetStagedPackageOrigin**](/windows/desktop/api/AppModel/nf-appmodel-getstagedpackageorigin)<br/>                                   | Gets the origin of the specified package.<br/>                                                                                                             |
| [**GetStagedPackagePathByFullName**](/windows/desktop/api/AppModel/nf-appmodel-getstagedpackagepathbyfullname)<br/>                   | Gets the path of the specified staged package.<br/>                                                                                                        |
| [**GetStagedPackagePathByFullName2**](/windows/desktop/api/AppModel/nf-appmodel-getstagedpackagepathbyfullname2)<br/>                   | Gets the path of the specified staged package, with the option to specify the package folder type.<br/>                                                                                                        |
| [**OpenPackageInfoByFullName**](/windows/desktop/api/AppModel/nf-appmodel-openpackageinfobyfullname)<br/>                             | Opens the package information of the specified package.<br/>                                                                                               |
| [**PackageFamilyNameFromFullName**](/windows/desktop/api/AppModel/nf-appmodel-packagefamilynamefromfullname)<br/>                     | Gets the package family name for the specified package full name.<br/>                                                                                     |
| [**PackageFamilyNameFromId**](/windows/desktop/api/AppModel/nf-appmodel-packagefamilynamefromid)<br/>                                 | Gets the package family name for the specified package identifier.<br/>                                                                                    |
| [**PackageFullNameFromId**](/windows/desktop/api/AppModel/nf-appmodel-packagefullnamefromid)<br/>                                     | Gets the package full name for the specified package identifier (ID).<br/>                                                                                 |
| [**PackageIdFromFullName**](/windows/desktop/api/AppModel/nf-appmodel-packageidfromfullname)<br/>                                     | Gets the package identifier (ID) for the specified package full name.<br/>                                                                                 |
| [**PackageNameAndPublisherIdFromFamilyName**](/windows/desktop/api/AppModel/nf-appmodel-packagenameandpublisheridfromfamilyname)<br/> | Gets the package name and publisher identifier (ID) for the specified package family name.<br/>                                                            |
| [**ParseApplicationUserModelId**](/windows/desktop/api/AppModel/nf-appmodel-parseapplicationusermodelid)<br/>                         | Deconstructs an [application user model ID](appx-packaging-glossary.md) to its package family name and package relative application ID (PRAID).<br/>      |
| [**PackageOrigin**](/windows/desktop/api/AppModel/ne-appmodel-packageorigin)<br/>                                                     | Specifies the origin of a package. <br/>                                                                                                                   |
| [**Identity constants**](identity-constants.md)<br/>                                           | Specifies the length of the strings for the package's identity fields.<br/>                                                                                |
| [**Package constants**](package-constants.md)<br/>                                             | Specifies how packages are to be processed.<br/>                                                                                                           |
| [**PACKAGE\_ID**](/windows/desktop/api/AppModel/ns-appmodel-package_id)<br/>                                                          | Represents package identification information, such as name, version, and publisher.<br/>                                                                  |
| [**PACKAGE\_INFO**](/windows/desktop/api/AppModel/ns-appmodel-package_info)<br/>                                                      | Represents package identification information that includes the package identifier, full name, and install location.<br/>                                  |
| [**PACKAGE\_VERSION**](/windows/desktop/api/AppModel/ns-appmodel-package_version)<br/>                                                | Represents the package version information.<br/>                                                                                                           |



 

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

 

 





