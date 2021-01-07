---
description: The suggested action sequences for a basic InstallExecuteSequence table in a Windows Installer database.
ms.assetid: 7f337f37-1528-4b7e-a628-f9d235510a6f
title: Suggested InstallExecuteSequence
ms.topic: article
ms.date: 05/31/2018
---

# Suggested InstallExecuteSequence



| Action                                                          | Condition                          | Sequence |
|-----------------------------------------------------------------|------------------------------------|----------|
| [LaunchConditions](launchconditions-action.md)                 |                                    | 100      |
| [AppSearch](appsearch-action.md)                               |                                    | 400      |
| [CCPSearch](ccpsearch-action.md)                               | NOT [**Installed**](installed.md) | 500      |
| [RMCCPSearch](rmccpsearch-action.md)                           | NOT [**Installed**](installed.md) | 600      |
| [ValidateProductID](validateproductid-action.md)               |                                    | 700      |
| [CostInitialize](costinitialize-action.md)                     |                                    | 800      |
| [FileCost](filecost-action.md)                                 |                                    | 900      |
| [CostFinalize](costfinalize-action.md)                         |                                    | 1000     |
| [SetODBCFolders](setodbcfolders-action.md)                     |                                    | 1100     |
| [InstallValidate](installvalidate-action.md)                   |                                    | 1400     |
| [InstallInitialize](installinitialize-action.md)               |                                    | 1500     |
| [AllocateRegistrySpace](allocateregistryspace-action.md)       | NOT [**Installed**](installed.md) | 1550     |
| [ProcessComponents](processcomponents-action.md)               |                                    | 1600     |
| [UnpublishComponents](unpublishcomponents-action.md)           |                                    | 1700     |
| [UnpublishFeatures](unpublishfeatures-action.md)               |                                    | 1800     |
| [StopServices](stopservices-action.md)                         | [**VersionNT**](versionnt.md)     | 1900     |
| [DeleteServices](deleteservices-action.md)                     | [**VersionNT**](versionnt.md)     | 2000     |
| [UnregisterComPlus](unregistercomplus-action.md)               |                                    | 2100     |
| [SelfUnregModules](selfunregmodules-action.md)                 |                                    | 2200     |
| [UnregisterTypeLibraries](unregistertypelibraries-action.md)   |                                    | 2300     |
| [RemoveODBC](removeodbc-action.md)                             |                                    | 2400     |
| [UnregisterFonts](unregisterfonts-action.md)                   |                                    | 2500     |
| [RemoveRegistryValues](removeregistryvalues-action.md)         |                                    | 2600     |
| [UnregisterClassInfo](unregisterclassinfo-action.md)           |                                    | 2700     |
| [UnregisterExtensionInfo](unregisterextensioninfo-action.md)   |                                    | 2800     |
| [UnregisterProgIdInfo](unregisterprogidinfo-action.md)         |                                    | 2900     |
| [UnregisterMIMEInfo](unregistermimeinfo-action.md)             |                                    | 3000     |
| [RemoveIniValues](removeinivalues-action.md)                   |                                    | 3100     |
| [RemoveShortcuts](removeshortcuts-action.md)                   |                                    | 3200     |
| [RemoveEnvironmentStrings](removeenvironmentstrings-action.md) |                                    | 3300     |
| [RemoveDuplicateFiles](removeduplicatefiles-action.md)         |                                    | 3400     |
| [RemoveFiles](removefiles-action.md)                           |                                    | 3500     |
| [RemoveFolders](removefolders-action.md)                       |                                    | 3600     |
| [CreateFolders](createfolders-action.md)                       |                                    | 3700     |
| [MoveFiles](movefiles-action.md)                               |                                    | 3800     |
| [InstallFiles](installfiles-action.md)                         |                                    | 4000     |
| [PatchFiles](patchfiles-action.md)                             |                                    | 4090     |
| [DuplicateFiles](duplicatefiles-action.md)                     |                                    | 4210     |
| [BindImage](bindimage-action.md)                               |                                    | 4300     |
| [CreateShortcuts](createshortcuts-action.md)                   |                                    | 4500     |
| [RegisterClassInfo](registerclassinfo-action.md)               |                                    | 4600     |
| [RegisterExtensionInfo](registerextensioninfo-action.md)       |                                    | 4700     |
| [RegisterProgIdInfo](registerprogidinfo-action.md)             |                                    | 4800     |
| [RegisterMIMEInfo](registermimeinfo-action.md)                 |                                    | 4900     |
| [WriteRegistryValues](writeregistryvalues-action.md)           |                                    | 5000     |
| [WriteIniValues](writeinivalues-action.md)                     |                                    | 5100     |
| [WriteEnvironmentStrings](writeenvironmentstrings-action.md)   |                                    | 5200     |
| [RegisterFonts](registerfonts-action.md)                       |                                    | 5300     |
| [InstallODBC](installodbc-action.md)                           |                                    | 5400     |
| [RegisterTypeLibraries](registertypelibraries-action.md)       |                                    | 5500     |
| [SelfRegModules](selfregmodules-action.md)                     |                                    | 5600     |
| [RegisterComPlus](registercomplus-action.md)                   |                                    | 5700     |
| [InstallServices](installservices-action.md)                   | [**VersionNT**](versionnt.md)     | 5800     |
| [StartServices](startservices-action.md)                       | [**VersionNT**](versionnt.md)     | 5900     |
| [RegisterUser](registeruser-action.md)                         |                                    | 6000     |
| [RegisterProduct](registerproduct-action.md)                   |                                    | 6100     |
| [PublishComponents](publishcomponents-action.md)               |                                    | 6200     |
| [PublishFeatures](publishfeatures-action.md)                   |                                    | 6300     |
| [PublishProduct](publishproduct-action.md)                     |                                    | 6400     |
| [InstallFinalize](installfinalize-action.md)                   |                                    | 6600     |



 

 

 



