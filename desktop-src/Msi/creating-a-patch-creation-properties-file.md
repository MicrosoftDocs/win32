---
description: To reproduce the sample patch package, you need a software tool capable of creating and editing a Windows Installer patch package.
ms.assetid: 0653d8f6-89b0-4c56-ae51-3c7cb7df2909
title: Creating a Patch Creation Properties File
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Patch Creation Properties File

To reproduce the sample patch package, you need a software tool capable of creating and editing a Windows Installer patch package. Several patch package creation tools are available from independent software vendors. The example discussed in the following sections uses a Windows Installer database editor called Orca to author a patch creation properties file (.pcp extension). The .pcp file may be used with the utilities [Msimsp.exe](msimsp-exe.md) and [Patchwiz.dll](patchwiz-dll.md) to generate a Windows Installer patch package (.msp extension). Orca, Msimsp.exe, and Patchwiz.dll are provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

A blank patch creation properties file, template.pcp, is also provided with the SDK. Make a copy of template.pcp and rename this copy MNP2000.pcp. Use Orca or another database editor to enter the following data into the Properties table of MNP2000.pcp. The Properties table contains global settings for the patch package.

[Properties Table](properties-table-patchwiz-dll-.md)



| Name                               | Value                                  |
|------------------------------------|----------------------------------------|
| AllowProductCodeMismatches         | 1                                      |
| AllowProductVersionMajorMismatches | 1                                      |
| ApiPatchingSymbolFlags             | 0x00000000                             |
| DontRemoveTempFolderWhenFinished   | 1                                      |
| IncludeWholeFilesOnly              | 0                                      |
| ListOfPatchGUIDsToReplace          |                                        |
| ListOfTargetProductCodes           | \*                                     |
| PatchGUID                          | {5406B219-A1AC-4BC4-8695-72292C8195AC} |
| PatchOutputPath                    | c:\\output.msp                         |
| PatchSourceList                    | PatchSourceList                        |



 

Use the database editor to enter the following data into the ImageFamilies table of MNP2000.pcp. The ImageFamilies table contains information to be added to the [Media table](media-table.md) during patching.

[ImageFamilies Table](imagefamilies-table-patchwiz-dll-.md)



| Family  | MediaSrcPropName | MediaDiskId | FileSequenceStart | DiskPrompt | VolumeLabel |
|---------|------------------|-------------|-------------------|------------|-------------|
| MNPapps | MNPSrcPropName   | 2           | 1000              |            |             |



 

Enter the following data into the UpgradedImages table of MNP2000.pcp. The UpgradedImages table contains information about the Upgraded image you created in [Planning a Small Update Patch](planning-a-small-update-patch.md).

[UpgradedImages Table](upgradedimages-table-patchwiz-dll-.md)



| Upgraded   | MsiPath                                           | PatchMsiPath | SymbolPaths | Family  |
|------------|---------------------------------------------------|--------------|-------------|---------|
| MNP\_fixed | C:\\Note\_Installer\\Patch\\Upgraded\\MNP2000.msi |              |             | MNPapps |



 

Enter the following data into the TargetImages table of MNP2000.pcp. The TargetImages table contains information about the Target image.

[TargetImages Table](targetimages-table-patchwiz-dll-.md)



| Target     | MsiPath                                         | SymbolPaths | Upgraded   | Order | ProductValidateFlags | IgnoreMissingSrcFiles |
|------------|-------------------------------------------------|-------------|------------|-------|----------------------|-----------------------|
| MNP\_error | C:\\Note\_Installer\\Patch\\Target\\MNP2000.msi |             | MNP\_fixed | 1     |                      | 0                     |



 

For the sample patch package, leave the following tables in MNP2000.pcp blank.

[UpgradedFiles\_OptionalData Table](upgradedfiles-optionaldata-table-patchwiz-dll-.md)

[FamilyFileRanges Table](familyfileranges-table-patchwiz-dll-.md)

[TargetFiles\_OptionalData Table](targetfiles-optionaldata-table-patchwiz-dll-.md)

[ExternalFiles Table](externalfiles-table-patchwiz-dll-.md)

[UpgradedFilesToIgnore Table](upgradedfilestoignore-table-patchwiz-dll-.md)

[Continue](generating-a-patch-package.md)

 

 



