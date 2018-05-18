---
title: Package query API
description: Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.
ms.assetid: 'EDDFC8B1-E224-4921-BED6-FC81711BA5BF'
---

# Package query API

Learn about the package query API, which you can use to get info about the app packages installed on the system. Each app package contains the files that constitute a Windows Store app, and a manifest file that describes the software to Windows.

## In this section



| Topic                                                                                                 | Description                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClosePackageInfo**](closepackageinfo.md)<br/>                                               | Closes a reference to the specified package information.<br/>                                                                                              |
| [**FindPackagesByPackageFamily**](findpackagesbypackagefamily.md)<br/>                         | Finds the packages with the specified family name for the current user. <br/>                                                                              |
| [**FormatApplicationUserModelId**](formatapplicationusermodelid.md)<br/>                       | Constructs an [application user model ID](appx-packaging-glossary.md) from the package family name and the package relative application ID (PRAID). <br/> |
| [**GetApplicationUserModelId**](getapplicationusermodelid.md)<br/>                             | Gets the [application user model ID](appx-packaging-glossary.md) for the specified process.<br/>                                                          |
| [**GetApplicationUserModelIdFromToken**](getapplicationusermodelidfromtoken.md)<br/>           | Gets the [application user model ID](appx-packaging-glossary.md) for the specified token.<br/>                                                            |
| [**GetCurrentApplicationUserModelId**](getcurrentapplicationusermodelid.md)<br/>               | Gets the [application user model ID](appx-packaging-glossary.md) for the current process.<br/>                                                            |
| [**GetCurrentPackageFamilyName**](getcurrentpackagefamilyname.md)<br/>                         | Gets the package family name for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackageFullName**](getcurrentpackagefullname.md)<br/>                             | Gets the package full name for the calling process.<br/>                                                                                                   |
| [**GetCurrentPackageId**](getcurrentpackageid.md)<br/>                                         | Gets the package identifier (ID) for the calling process.<br/>                                                                                             |
| [**GetCurrentPackageInfo**](getcurrentpackageinfo.md)<br/>                                     | Gets the package information for the calling process.<br/>                                                                                                 |
| [**GetCurrentPackagePath**](getcurrentpackagepath.md)<br/>                                     | Gets the package path for the calling process.<br/>                                                                                                        |
| [**GetPackageApplicationIds**](getpackageapplicationids.md)<br/>                               | Gets the IDs of apps in the specified package.<br/>                                                                                                        |
| [**GetPackageFamilyName**](getpackagefamilyname.md)<br/>                                       | Gets the package family name for the specified process.<br/>                                                                                               |
| [**GetPackageFamilyNameFromToken**](getpackagefamilynamefromtoken.md)<br/>                     | Gets the package family name for the specified token.<br/>                                                                                                 |
| [**GetPackageFullName**](getpackagefullname.md)<br/>                                           | Gets the package full name for the specified process.<br/>                                                                                                 |
| [**GetPackageFullNameFromToken**](getpackagefullnamefromtoken.md)<br/>                         | Gets the package full name for the specified token.<br/>                                                                                                   |
| [**GetPackageId**](getpackageid.md)<br/>                                                       | Gets the package identifier (ID) for the specified process.<br/>                                                                                           |
| [**GetPackageInfo**](getpackageinfo.md)<br/>                                                   | Gets the package information for the specified package.<br/>                                                                                               |
| [**GetPackagePath**](getpackagepath.md)<br/>                                                   | Gets the path for the specified package.<br/>                                                                                                              |
| [**GetPackagePathByFullName**](getpackagepathbyfullname.md)<br/>                               | Gets the path of the specified package.<br/>                                                                                                               |
| [**GetPackagesByPackageFamily**](getpackagesbypackagefamily.md)<br/>                           | Gets the packages with the specified family name for the current user. <br/>                                                                               |
| [**GetStagedPackageOrigin**](getstagedpackageorigin.md)<br/>                                   | Gets the origin of the specified package.<br/>                                                                                                             |
| [**GetStagedPackagePathByFullName**](getstagedpackagepathbyfullname.md)<br/>                   | Gets the path of the specified staged package.<br/>                                                                                                        |
| [**OpenPackageInfoByFullName**](openpackageinfobyfullname.md)<br/>                             | Opens the package information of the specified package.<br/>                                                                                               |
| [**PackageFamilyNameFromFullName**](packagefamilynamefromfullname.md)<br/>                     | Gets the package family name for the specified package full name.<br/>                                                                                     |
| [**PackageFamilyNameFromId**](packagefamilynamefromid.md)<br/>                                 | Gets the package family name for the specified package identifier.<br/>                                                                                    |
| [**PackageFullNameFromId**](packagefullnamefromid.md)<br/>                                     | Gets the package full name for the specified package identifier (ID).<br/>                                                                                 |
| [**PackageIdFromFullName**](packageidfromfullname.md)<br/>                                     | Gets the package identifier (ID) for the specified package full name.<br/>                                                                                 |
| [**PackageNameAndPublisherIdFromFamilyName**](packagenameandpublisheridfromfamilyname.md)<br/> | Gets the package name and publisher identifier (ID) for the specified package family name.<br/>                                                            |
| [**ParseApplicationUserModelId**](parseapplicationusermodelid.md)<br/>                         | Deconstructs an [application user model ID](appx-packaging-glossary.md) to its package family name and package relative application ID (PRAID).<br/>      |
| [**PackageOrigin**](packageorigin.md)<br/>                                                     | Specifies the origin of a package. <br/>                                                                                                                   |
| [**Identity constants**](identity-constants.md)<br/>                                           | Specifies the length of the strings for the package's identity fields.<br/>                                                                                |
| [**Package constants**](package-constants.md)<br/>                                             | Specifies how packages are to be processed.<br/>                                                                                                           |
| [**PACKAGE\_ID**](package-id.md)<br/>                                                          | Represents package identification information, such as name, version, and publisher.<br/>                                                                  |
| [**PACKAGE\_INFO**](package-info.md)<br/>                                                      | Represents package identification information that includes the package identifier, full name, and install location.<br/>                                  |
| [**PACKAGE\_VERSION**](package-version.md)<br/>                                                | Represents the package version information.<br/>                                                                                                           |



 

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

 

 





