---
description: The Windows Installer has the following standard actions.
ms.assetid: 219b5eb6-501f-4e30-b398-4ed5e0cdf2ab
title: Standard Actions Reference
ms.topic: article
ms.date: 05/31/2018
---

# Standard Actions Reference

The Windows Installer has the following standard actions.



| Action name                                                     | Brief description of action                                                                                                                                                   |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ADMIN](admin-action.md)                                       | A top-level action used for an administrative installation.                                                                                                                   |
| [ADVERTISE](advertise-action.md)                               | A top-level action called to install or remove advertised components.                                                                                                         |
| [AllocateRegistrySpace](allocateregistryspace-action.md)       | Validates that the free space specified by [**AVAILABLEFREEREG**](availablefreereg.md) exists in the registry.                                                               |
| [AppSearch](appsearch-action.md)                               | Searches for previous versions of products and determines that upgrades are installed.                                                                                        |
| [BindImage](bindimage-action.md)                               | Binds executables to imported DLLs.                                                                                                                                           |
| [CCPSearch](ccpsearch-action.md)                               | Uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.                                              |
| [CostFinalize](costfinalize-action.md)                         | Ends the internal installation costing process begun by the [CostInitialize action](costinitialize-action.md).                                                               |
| [CostInitialize](costinitialize-action.md)                     | Starts the installation costing process.                                                                                                                                      |
| [CreateFolders](createfolders-action.md)                       | Creates empty folders for components.                                                                                                                                         |
| [CreateShortcuts](createshortcuts-action.md)                   | Creates shortcuts.                                                                                                                                                            |
| [DeleteServices](deleteservices-action.md)                     | Removes system services.                                                                                                                                                      |
| [DisableRollback](disablerollback-action.md)                   | Disables rollback for the remainder of the installation.                                                                                                                      |
| [DuplicateFiles](duplicatefiles-action.md)                     | Duplicates files installed by the InstallFiles action.                                                                                                                        |
| [ExecuteAction](executeaction-action.md)                       | Checks the [**EXECUTEACTION**](executeaction.md) property to determine which top-level action begins the execution sequence, then runs that action.                          |
| [FileCost](filecost-action.md)                                 | Initializes disk cost calculation with the installer. Disk costing is not finalized until the CostFinalize action is executed.                                                |
| [FindRelatedProducts](findrelatedproducts-action.md)           | Detects correspondence between the [Upgrade table](upgrade-table.md) and installed products.                                                                                 |
| [ForceReboot](forcereboot-action.md)                           | Used in the action sequence to prompt the user for a restart of the system during the installation.                                                                           |
| [INSTALL](install-action.md)                                   | A top-level action called to install or remove components.                                                                                                                    |
| [InstallAdminPackage](installadminpackage-action.md)           | Copies the installer database to the administrative installation point.                                                                                                       |
| [InstallExecute](installexecute-action.md)                     | Runs a script containing all operations in the action sequence since either the start of the installation or the last InstallFinalize action. Does not end the transaction.   |
| [InstallFiles](installfiles-action.md)                         | Copies files from the source to the destination directory.                                                                                                                    |
| [InstallFinalize](installfinalize-action.md)                   | Runs a script containing all operations in the action sequence since either the start of the installation or the last InstallFinalize action. Marks the end of a transaction. |
| [InstallInitialize](installinitialize-action.md)               | Marks the beginning of a transaction.                                                                                                                                         |
| [InstallSFPCatalogFile](installsfpcatalogfile-action.md)       | The InstallSFPCatalogFile action installs the catalogs used by Windows Me for Windows File Protection.                                                                        |
| [InstallValidate](installvalidate-action.md)                   | Verifies that all volumes with attributed costs have sufficient space for the installation.                                                                                   |
| [IsolateComponents](isolatecomponents-action.md)               | Processes the [IsolatedComponent table](isolatedcomponent-table.md)                                                                                                          |
| [LaunchConditions](launchconditions-action.md)                 | Evaluates a set of conditional statements contained in the LaunchCondition table that must all evaluate to True before the installation can proceed.                          |
| [MigrateFeatureStates](migratefeaturestates-action.md)         | Migrates current feature states to the pending installation.                                                                                                                  |
| [MoveFiles](movefiles-action.md)                               | Locates existing files and moves or copies those files to a new location.                                                                                                     |
| [MsiConfigureServices](msiconfigureservices-action.md)         | Configures a service for the system. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                           |
| [MsiPublishAssemblies action](msipublishassemblies-action.md)  | Manages the advertisement of common language runtime assemblies and Win32 assemblies that are being installed.                                                                |
| [MsiUnpublishAssemblies](msiunpublishassemblies-action.md)     | Manages the advertisement of common language runtime assemblies and Win32 assemblies that are being removed.                                                                  |
| [InstallODBC](installodbc-action.md)                           | Installs the ODBC drivers, translators, and data sources.                                                                                                                     |
| [InstallServices](installservices-action.md)                   | Registers a service with the system.                                                                                                                                          |
| [PatchFiles](patchfiles-action.md)                             | Queries the Patch table to determine which patches are applied to specific files and then performs the byte-wise patching of the files.                                       |
| [ProcessComponents](processcomponents-action.md)               | Registers components, their key paths, and component clients.                                                                                                                 |
| [PublishComponents](publishcomponents-action.md)               | Advertises the components specified in the PublishComponent table.                                                                                                            |
| [PublishFeatures](publishfeatures-action.md)                   | Writes the feature state of each feature into the system registry                                                                                                             |
| [PublishProduct](publishproduct-action.md)                     | Publishes product information with the system.                                                                                                                                |
| [RegisterClassInfo](registerclassinfo-action.md)               | Manages the registration of COM class information with the system.                                                                                                            |
| [RegisterComPlus](registercomplus-action.md)                   | The RegisterComPlus action registers COM+ applications.                                                                                                                       |
| [RegisterExtensionInfo](registerextensioninfo-action.md)       | Registers extension related information with the system.                                                                                                                      |
| [RegisterFonts](registerfonts-action.md)                       | Registers installed fonts with the system.                                                                                                                                    |
| [RegisterMIMEInfo](registermimeinfo-action.md)                 | Registers MIME information with the system.                                                                                                                                   |
| [RegisterProduct](registerproduct-action.md)                   | Registers product information with the installer and stores the installer database on the local computer.                                                                     |
| [RegisterProgIdInfo](registerprogidinfo-action.md)             | Registers OLE ProgId information with the system.                                                                                                                             |
| [RegisterTypeLibraries](registertypelibraries-action.md)       | Registers type libraries with the system.                                                                                                                                     |
| [RegisterUser](registeruser-action.md)                         | Registers user information to identify the user of a product.                                                                                                                 |
| [RemoveDuplicateFiles](removeduplicatefiles-action.md)         | Deletes files installed by the DuplicateFiles action.                                                                                                                         |
| [RemoveEnvironmentStrings](removeenvironmentstrings-action.md) | Modifies the values of environment variables.                                                                                                                                 |
| [RemoveExistingProducts](removeexistingproducts-action.md)     | Removes installed versions of a product.                                                                                                                                      |
| [RemoveFiles](removefiles-action.md)                           | Removes files previously installed by the InstallFiles action.                                                                                                                |
| [RemoveFolders](removefolders-action.md)                       | Removes empty folders linked to components set to be removed.                                                                                                                 |
| [RemoveIniValues](removeinivalues-action.md)                   | Deletes .ini file information associated with a component specified in the IniFile table.                                                                                     |
| [RemoveODBC](removeodbc-action.md)                             | Removes ODBC data sources, translators, and drivers.                                                                                                                          |
| [RemoveRegistryValues](removeregistryvalues-action.md)         | Removes an application's registry keys that were created from the Registry table..                                                                                            |
| [RemoveShortcuts](removeshortcuts-action.md)                   | Manages the removal of an advertised shortcut whose feature is selected for uninstallation.                                                                                   |
| [ResolveSource](resolvesource-action.md)                       | Determines the source location and sets the [**SourceDir**](sourcedir.md) property.                                                                                          |
| [RMCCPSearch](rmccpsearch-action.md)                           | Uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.                                              |
| [ScheduleReboot](schedulereboot-action.md)                     | Prompts the user for a system restart at the end of the installation.                                                                                                         |
| [SelfRegModules](selfregmodules-action.md)                     | Processes modules in the SelfReg table and registers them if they are installed.                                                                                              |
| [SelfUnregModules](selfunregmodules-action.md)                 | Unregisters the modules in the SelfReg table that are set to be uninstalled.                                                                                                  |
| [SEQUENCE](sequence-action.md)                                 | Runs the actions in a table specified by the [**SEQUENCE**](sequence.md) property.                                                                                           |
| [SetODBCFolders Action](setodbcfolders-action.md)              | Checks the system for existing ODBC drivers and sets target directory for new ODBC drivers.                                                                                   |
| [StartServices](startservices-action.md)                       | Starts system services.                                                                                                                                                       |
| [StopServices](stopservices-action.md)                         | Stops system services.                                                                                                                                                        |
| [UnpublishComponents](unpublishcomponents-action.md)           | Manages the unadvertisement of components from the PublishComponent table and removes information about published components.                                                 |
| [UnpublishFeatures](unpublishfeatures-action.md)               | Removes the selection-state and feature-component mapping information from the system registry.                                                                               |
| [UnregisterClassInfo](unregisterclassinfo-action.md)           | Manages the removal of COM classes from the system registry.                                                                                                                  |
| [UnregisterComPlus](unregistercomplus-action.md)               | The UnregisterComPlus action removes COM+ applications from the registry.                                                                                                     |
| [UnregisterExtensionInfo](unregisterextensioninfo-action.md)   | Manages the removal of extension-related information from the system.                                                                                                         |
| [UnregisterFonts](unregisterfonts-action.md)                   | Removes registration information about installed fonts from the system.                                                                                                       |
| [UnregisterMIMEInfo](unregistermimeinfo-action.md)             | Unregisters MIME-related information from the system registry.                                                                                                                |
| [UnregisterProgIdInfo](unregisterprogidinfo-action.md)         | Manages the unregistration of OLE ProgId information with the system.                                                                                                         |
| [UnregisterTypeLibraries](unregistertypelibraries-action.md)   | Unregisters type libraries with the system.                                                                                                                                   |
| [ValidateProductID](validateproductid-action.md)               | Sets [**ProductID**](productid.md) property to the full product identifier.                                                                                                  |
| [WriteEnvironmentStrings](writeenvironmentstrings-action.md)   | Modifies the values of environment variables.                                                                                                                                 |
| [WriteIniValues](writeinivalues-action.md)                     | Writes .ini file information.                                                                                                                                                 |
| [WriteRegistryValues](writeregistryvalues-action.md)           | Sets up registry information.                                                                                                                                                 |



 

 

 




