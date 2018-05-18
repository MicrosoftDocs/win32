---
Description: 'To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.'
ms.assetid: '05a16915-6b47-4d51-b62a-5a4d92b87e50'
title: Installer Function Reference
---

# Installer Function Reference

To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.

## User Interface and Logging Functions



| Name                                                     | Description                                                                           |
|----------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MsiSetInternalUI**](msisetinternalui.md)             | Enables the internal user interface of the installer.                                 |
| [**MsiSetExternalUI**](msisetexternalui.md)             | Enables an external user-interface handler that receives messages in a string format. |
| [**MsiSetExternalUIRecord**](msisetexternaluirecord.md) | Enables an external user-interface handler that receives messages in a record format. |
| [**MsiEnableLog**](msienablelog.md)                     | Sets the log mode for all installations in the calling process.                       |



 

## Handle Management Functions



| Name                                             | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| [**MsiCloseHandle**](msiclosehandle.md)         | Closes an open installation handle.                           |
| [**MsiCloseAllHandles**](msicloseallhandles.md) | Closes all open installation handles. Do not use for cleanup. |



 

## Installation and Configuration Functions



| Name                                                                     | Description                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiAdvertiseProduct**](msiadvertiseproduct.md)                       | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseProductEx**](msiadvertiseproductex.md)                   | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseScript**](msiadvertisescript.md)                         | Copies an advertise script file into specified locations.                                                                                                                                                                    |
| [**MsiInstallProduct**](msiinstallproduct.md)                           | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProduct**](msiconfigureproduct.md)                       | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProductEx**](msiconfigureproductex.md)                   | Installs or removes an application or application suite. A product command-line can be specified.                                                                                                                            |
| [**MsiReinstallProduct**](msireinstallproduct.md)                       | Reinstalls or repairs an installation.                                                                                                                                                                                       |
| [**MsiConfigureFeature**](msiconfigurefeature.md)                       | Configures the installed state of a feature.                                                                                                                                                                                 |
| [**MsiReinstallFeature**](msireinstallfeature.md)                       | Validates or repairs features.                                                                                                                                                                                               |
| [**MsiInstallMissingComponent**](msiinstallmissingcomponent.md)         | Installs missing components.                                                                                                                                                                                                 |
| [**MsiInstallMissingFile**](msiinstallmissingfile.md)                   | Installs missing files.                                                                                                                                                                                                      |
| [**MsiNotifySidChange**](msinotifysidchange.md)                         | Notifies and updates the Windows Installer internal information with changes to user SIDs. Available beginning with Windows Installer 3.1.                                                                                   |
| [**MsiProcessAdvertiseScript**](msiprocessadvertisescript.md)           | Processes an advertise script file into specified locations.                                                                                                                                                                 |
| [**MsiSourceListAddSource**](msisourcelistaddsource.md)                 | Adds or reorders the sources of a patch or product in a specified context.                                                                                                                                                   |
| [**MsiSourceListAddSourceEx**](msisourcelistaddsourceex.md)             | Adds or reorders the sources of a patch or product in a specified context. Creates a source list for a patch that does not exist in a specified context. Available in Windows Installer  3.0.                                |
| [**MsiSourceListClearSource**](msisourcelistclearsource.md)             | Removes an existing source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                               |
| [**MsiSourceListClearAll**](msisourcelistclearall.md)                   | Removes all the existing sources of a specific source type for a specified product instance.                                                                                                                                 |
| [**MsiSourceListClearAllEx**](msisourcelistclearallex.md)               | Removes all the existing sources of a specific source type for a specified product instance. Available in Windows Installer  3.0.                                                                                            |
| [**MsiSourceListForceResolution**](msisourcelistforceresolution.md)     | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list.                                      |
| [**MsiSourceListForceResolutionEx**](msisourcelistforceresolutionex.md) | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list. Available in Windows Installer  3.0. |
| [**MsiSourceListGetInfo**](msisourcelistgetinfo.md)                     | Retrieves information about the source list for a product or patch in a specific context.                                                                                                                                    |
| [**MsiSourceListSetInfo**](msisourcelistsetinfo.md)                     | Sets the most recently used source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                       |
| [**MsiSourceListEnumMediaDisks**](msisourcelistenummediadisks.md)       | Enumerates the list of disks registered for the media source for a patch or product. Available in Windows Installer  3.0.                                                                                                    |
| [**MsiSourceListAddMediaDisk**](msisourcelistaddmediadisk.md)           | Adds or updates a disk of the media source of a registered product or patch. Available in Windows Installer  3.0.                                                                                                            |
| [**MsiSourceListClearMediaDisk**](msisourcelistclearmediadisks.md)      | Removes an existing registered disk under the media source for a product or patch in a specific context. Available in Windows Installer  3.0.                                                                                |
| [**MsiSourceListEnumSources**](msisourcelistenumsources.md)             | Enumerates the sources in the source list of a specified patch or product. Available in Windows Installer  3.0.                                                                                                              |



 

## Component-Specific Functions



| Name                                                                     | Description                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiProvideAssembly**](msiprovideassembly.md)                         | Installs and returns the full component path for an assembly.                                                                                                                                                                 |
| [**MsiProvideComponent**](msiprovidecomponent.md)                       | Installs and returns the full component path of a component.                                                                                                                                                                  |
| [**MsiProvideQualifiedComponent**](msiprovidequalifiedcomponent.md)     | Installs and returns the full component path of a qualified component.                                                                                                                                                        |
| [**MsiProvideQualifiedComponentEx**](msiprovidequalifiedcomponentex.md) | Installs and returns the full component path of a qualified component that is published by a product.                                                                                                                         |
| [**MsiGetComponentPath**](msigetcomponentpath.md)                       | Returns the full path or registry key to an installed component.                                                                                                                                                              |
| [**MsiGetComponentPathEx**](msigetcomponentpathex.md)                   | Returns the full path or registry key to an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/> |
| [**MsiLocateComponent**](msilocatecomponent.md)                         | Returns the full path to an installed component without a product code.                                                                                                                                                       |
| [**MsiQueryComponentState**](msiquerycomponentstate.md)                 | Returns the installed state for a component. Can query components of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |



 

## Application-Only Functions



| Name                                             | Description                                                            |
|--------------------------------------------------|------------------------------------------------------------------------|
| [**MsiCollectUserInfo**](msicollectuserinfo.md) | Stores user information from an installation wizard.                   |
| [**MsiUseFeature**](msiusefeature.md)           | Increments usage count for a feature and indicates installation state. |
| [**MsiUseFeatureEx**](msiusefeatureex.md)       | Increments usage count for a feature and indicates installation state. |
| [**MsiGetProductCode**](msigetproductcode.md)   | Returns product code using the component code.                         |



 

## System Status Functions



| Name                                                             | Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiEnumProducts**](msienumproducts.md)                       | Enumerates advertised products.                                                                                                                                                                                                   |
| [**MsiEnumProductsEx**](msienumproductsex.md)                   | Enumerates through all the instances of advertised or installed products in a specified context. Available in Windows Installer  3.0 or later.                                                                                    |
| [**MsiEnumRelatedProducts**](msienumrelatedproducts.md)         | Enumerates currently installed products having a specified upgrade code.                                                                                                                                                          |
| [**MsiEnumFeatures**](msienumfeatures.md)                       | Enumerates published features.                                                                                                                                                                                                    |
| [**MsiEnumComponents**](msienumcomponents.md)                   | Enumerates the installed components.                                                                                                                                                                                              |
| [**MsiEnumComponentsEx**](msienumcomponentsex.md)               | Enumerates the installed components across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                 |
| [**MsiEnumClients**](msienumclients.md)                         | Enumerates the clients of an installed component.                                                                                                                                                                                 |
| [**MsiEnumClientsEx**](msienumclientsex.md)                     | Enumerates the clients of an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                    |
| [**MsiEnumComponentQualifiers**](msienumcomponentqualifiers.md) | Enumerates the advertised qualifiers for a component.                                                                                                                                                                             |
| [**MsiQueryFeatureState**](msiqueryfeaturestate.md)             | Returns the installed state of a feature.                                                                                                                                                                                         |
| [**MsiQueryFeatureStateEx**](msiqueryfeaturestateex.md)         | Returns the installed state for a product feature. Can query features of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |
| [**MsiQueryProductState**](msiqueryproductstate.md)             | Returns the installed state for an application or application suite.                                                                                                                                                              |
| [**MsiGetFeatureUsage**](msigetfeatureusage.md)                 | Returns usage metrics for a feature.                                                                                                                                                                                              |
| [**MsiGetProductInfo**](msigetproductinfo.md)                   | Returns product information for published and installed products.                                                                                                                                                                 |
| [**MsiGetProductInfoEx**](msigetproductinfoex.md)               | Returns product information for advertised and installed products. Can retrieve information on an instance of a product installed under a user account other than the current user. Available in Windows Installer  3.0 or later. |
| [**MsiGetUserInfo**](msigetuserinfo.md)                         | Returns registered user information for an installed product.                                                                                                                                                                     |



 

## Product Query Functions



| Name                                                               | Description                                                                            |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**MsiOpenProduct**](msiopenproduct.md)                           | Opens a product to use with the functions that access the database.                    |
| [**MsiOpenPackage**](msiopenpackage.md)                           | Opens a package to use with the functions that access the database.                    |
| [**MsiOpenPackageEx**](msiopenpackageex.md)                       | Opens a package to use with the functions that access the database.                    |
| [**MsiIsProductElevated**](msiisproductelevated.md)               | Checks whether the product is installed with elevated privileges.                      |
| [**MsiGetProductInfoFromScript**](msigetproductinfofromscript.md) | Returns product information for an installer script file.                              |
| [**MsiGetProductProperty**](msigetproductproperty.md)             | Retrieves properties in the product database.                                          |
| [**MsiGetShortcutTarget**](msigetshortcuttarget.md)               | Examines a shortcut and returns its product, feature name, and component if available. |
| [**MsiGetFeatureInfo**](msigetfeatureinfo.md)                     | Returns descriptive information for a feature.                                         |
| [**MsiVerifyPackage**](msiverifypackage.md)                       | Verifies that a specified file is an installation package.                             |



 

## Patching Functions



| Name                                                                   | Description                                                                                                                                                        |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiApplyPatch**](msiapplypatch.md)                                 | Invokes an installation and applies a patch package.                                                                                                               |
| [**MsiEnumPatches**](msisourcelistaddmediadisk.md)                    | Returns the GUID for each patch that is applied to a product, and a list of transforms from each patch that apply to the product.                                  |
| [**MsiGetPatchInfo**](msigetpatchinfo.md)                             | Returns information about a patch.                                                                                                                                 |
| [**MsiRemovePatches**](msiremovepatches.md)                           | Uninstalls a patch from a product. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDeterminePatchSequence**](msideterminepatchsequence.md)         | Determines the best application sequence for a set of patches and product. Available in Windows Installer 3.0.                                                     |
| [**MsiApplyMultiplePatches**](msiapplymultiplepatches.md)             | Applies one or more patches to products. Available in Windows Installer 3.0.                                                                                       |
| [**MsiEnumPatchesEx**](msienumpatchesex.md)                           | Enumerates all patches applied for a product in a particular context or across all contexts. Available in Windows Installer 3.0.                                   |
| [**MsiGetPatchFileList**](msigetpatchfilelist.md)                     | When provided a list of .msp files this function retrieves the list of files that can be updated by the patches for the targe. Available in Windows Installer 4.0. |
| [**MsiGetPatchInfoEx**](msigetpatchinfoex.md)                         | Queries for information about the application of a specified patch to a specified product. Available in Windows Installer 3.0.                                     |
| [**MsiExtractPatchXMLData**](msiextractpatchxmldata.md)               | Extracts information from a patch. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDetermineApplicablePatches**](msidetermineapplicablepatches.md) | Determines the best set of patches required to update a product or set of products. Available in Windows Installer 3.0.                                            |



 

## File Query Functions



| Name                                                                     | Description                                                                                                 |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**MsiGetFileHash**](msigetfilehash.md)                                 | Takes the path to a file and returns a 128-bit hash of that file.                                           |
| [**MsiGetFileSignatureInformation**](msigetfilesignatureinformation.md) | Takes the path to a file that has been digitally signed and returns the file's signer certificate and hash. |
| [**MsiGetFileVersion**](msigetfileversion.md)                           | Returns the version string and language string.                                                             |



 

## Transaction Management Functions



| Name                                               | Description                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiBeginTransaction**](msibegintransaction.md) | Starts transaction processing of a multiple-package installation and returns an identifier for the transaction. This function is available beginning with Windows Installer 4.5.                    |
| [**MsiJoinTransaction**](msijointransaction.md)   | Requests that the Windows Installer make the current process the owner of the transaction installing a multi-package installation. This function is available beginning with Windows Installer 4.5. |
| [**MsiEndTransaction**](msiendtransaction.md)     | Commits or rolls back all the installations belonging to the transaction. This function is available beginning with Windows Installer 4.5.                                                          |



 

## Database Functions

In addition to the Windows Installer functions identified in the previous tables, you can manipulate information in the installation database by using the database access functions that are described in the [Database Functions](database-functions.md) section.

## Installer Structures

In addition, some information in the installation database is handled using the structures described in the [Installer Structures](installer-structures.md) section.

 

 




