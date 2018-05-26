---
Description: To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.
ms.assetid: 05a16915-6b47-4d51-b62a-5a4d92b87e50
title: Installer Function Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installer Function Reference

To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.

## User Interface and Logging Functions



| Name                                                     | Description                                                                           |
|----------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MsiSetInternalUI**](/windows/win32/Msi/nf-msi-msisetinternalui?branch=master)             | Enables the internal user interface of the installer.                                 |
| [**MsiSetExternalUI**](/windows/win32/Msi/nf-msi-msisetexternaluia?branch=master)             | Enables an external user-interface handler that receives messages in a string format. |
| [**MsiSetExternalUIRecord**](/windows/win32/Msi/nf-msi-msisetexternaluirecord?branch=master) | Enables an external user-interface handler that receives messages in a record format. |
| [**MsiEnableLog**](/windows/win32/Msi/nf-msi-msienableloga?branch=master)                     | Sets the log mode for all installations in the calling process.                       |



 

## Handle Management Functions



| Name                                             | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| [**MsiCloseHandle**](/windows/win32/Msi/nf-msi-msiclosehandle?branch=master)         | Closes an open installation handle.                           |
| [**MsiCloseAllHandles**](/windows/win32/Msi/nf-msi-msicloseallhandles?branch=master) | Closes all open installation handles. Do not use for cleanup. |



 

## Installation and Configuration Functions



| Name                                                                     | Description                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiAdvertiseProduct**](/windows/win32/Msi/nf-msi-msiadvertiseproducta?branch=master)                       | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseProductEx**](/windows/win32/Msi/nf-msi-msiadvertiseproductexa?branch=master)                   | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseScript**](/windows/win32/Msi/nf-msi-msiadvertisescripta?branch=master)                         | Copies an advertise script file into specified locations.                                                                                                                                                                    |
| [**MsiInstallProduct**](/windows/win32/Msi/nf-msi-msiinstallproducta?branch=master)                           | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master)                       | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProductEx**](/windows/win32/Msi/nf-msi-msiconfigureproductexa?branch=master)                   | Installs or removes an application or application suite. A product command-line can be specified.                                                                                                                            |
| [**MsiReinstallProduct**](/windows/win32/Msi/nf-msi-msireinstallproducta?branch=master)                       | Reinstalls or repairs an installation.                                                                                                                                                                                       |
| [**MsiConfigureFeature**](/windows/win32/Msi/nf-msi-msiconfigurefeaturea?branch=master)                       | Configures the installed state of a feature.                                                                                                                                                                                 |
| [**MsiReinstallFeature**](/windows/win32/Msi/nf-msi-msireinstallfeaturea?branch=master)                       | Validates or repairs features.                                                                                                                                                                                               |
| [**MsiInstallMissingComponent**](/windows/win32/Msi/nf-msi-msiinstallmissingcomponenta?branch=master)         | Installs missing components.                                                                                                                                                                                                 |
| [**MsiInstallMissingFile**](/windows/win32/Msi/nf-msi-msiinstallmissingfilea?branch=master)                   | Installs missing files.                                                                                                                                                                                                      |
| [**MsiNotifySidChange**](/windows/win32/Msi/nf-msi-msinotifysidchangea?branch=master)                         | Notifies and updates the Windows Installer internal information with changes to user SIDs. Available beginning with Windows Installer 3.1.                                                                                   |
| [**MsiProcessAdvertiseScript**](/windows/win32/Msi/nf-msi-msiprocessadvertisescripta?branch=master)           | Processes an advertise script file into specified locations.                                                                                                                                                                 |
| [**MsiSourceListAddSource**](/windows/win32/Msi/nf-msi-msisourcelistaddsourcea?branch=master)                 | Adds or reorders the sources of a patch or product in a specified context.                                                                                                                                                   |
| [**MsiSourceListAddSourceEx**](/windows/win32/Msi/nf-msi-msisourcelistaddsourceexa?branch=master)             | Adds or reorders the sources of a patch or product in a specified context. Creates a source list for a patch that does not exist in a specified context. Available in Windows Installer  3.0.                                |
| [**MsiSourceListClearSource**](/windows/win32/Msi/nf-msi-msisourcelistclearsourcea?branch=master)             | Removes an existing source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                               |
| [**MsiSourceListClearAll**](/windows/win32/Msi/nf-msi-msisourcelistclearalla?branch=master)                   | Removes all the existing sources of a specific source type for a specified product instance.                                                                                                                                 |
| [**MsiSourceListClearAllEx**](/windows/win32/Msi/nf-msi-msisourcelistclearallexa?branch=master)               | Removes all the existing sources of a specific source type for a specified product instance. Available in Windows Installer  3.0.                                                                                            |
| [**MsiSourceListForceResolution**](/windows/win32/Msi/nf-msi-msisourcelistforceresolutiona?branch=master)     | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list.                                      |
| [**MsiSourceListForceResolutionEx**](/windows/win32/Msi/nf-msi-msisourcelistforceresolutionexa?branch=master) | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list. Available in Windows Installer  3.0. |
| [**MsiSourceListGetInfo**](/windows/win32/Msi/nf-msi-msisourcelistgetinfoa?branch=master)                     | Retrieves information about the source list for a product or patch in a specific context.                                                                                                                                    |
| [**MsiSourceListSetInfo**](/windows/win32/Msi/nf-msi-msisourcelistsetinfoa?branch=master)                     | Sets the most recently used source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                       |
| [**MsiSourceListEnumMediaDisks**](/windows/win32/Msi/nf-msi-msisourcelistenummediadisksa?branch=master)       | Enumerates the list of disks registered for the media source for a patch or product. Available in Windows Installer  3.0.                                                                                                    |
| [**MsiSourceListAddMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistaddmediadiska?branch=master)           | Adds or updates a disk of the media source of a registered product or patch. Available in Windows Installer  3.0.                                                                                                            |
| [**MsiSourceListClearMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistclearmediadiska?branch=master)      | Removes an existing registered disk under the media source for a product or patch in a specific context. Available in Windows Installer  3.0.                                                                                |
| [**MsiSourceListEnumSources**](/windows/win32/Msi/nf-msi-msisourcelistenumsourcesa?branch=master)             | Enumerates the sources in the source list of a specified patch or product. Available in Windows Installer  3.0.                                                                                                              |



 

## Component-Specific Functions



| Name                                                                     | Description                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiProvideAssembly**](/windows/win32/Msi/nf-msi-msiprovideassemblya?branch=master)                         | Installs and returns the full component path for an assembly.                                                                                                                                                                 |
| [**MsiProvideComponent**](/windows/win32/Msi/nf-msi-msiprovidecomponenta?branch=master)                       | Installs and returns the full component path of a component.                                                                                                                                                                  |
| [**MsiProvideQualifiedComponent**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponenta?branch=master)     | Installs and returns the full component path of a qualified component.                                                                                                                                                        |
| [**MsiProvideQualifiedComponentEx**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponentexa?branch=master) | Installs and returns the full component path of a qualified component that is published by a product.                                                                                                                         |
| [**MsiGetComponentPath**](/windows/win32/Msi/nf-msi-msigetcomponentpatha?branch=master)                       | Returns the full path or registry key to an installed component.                                                                                                                                                              |
| [**MsiGetComponentPathEx**](/windows/win32/Msi/nf-msi-msigetcomponentpathexa?branch=master)                   | Returns the full path or registry key to an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/> |
| [**MsiLocateComponent**](/windows/win32/Msi/nf-msi-msilocatecomponenta?branch=master)                         | Returns the full path to an installed component without a product code.                                                                                                                                                       |
| [**MsiQueryComponentState**](/windows/win32/Msi/nf-msi-msiquerycomponentstatea?branch=master)                 | Returns the installed state for a component. Can query components of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |



 

## Application-Only Functions



| Name                                             | Description                                                            |
|--------------------------------------------------|------------------------------------------------------------------------|
| [**MsiCollectUserInfo**](/windows/win32/Msi/nf-msi-msicollectuserinfoa?branch=master) | Stores user information from an installation wizard.                   |
| [**MsiUseFeature**](/windows/win32/Msi/nf-msi-msiusefeaturea?branch=master)           | Increments usage count for a feature and indicates installation state. |
| [**MsiUseFeatureEx**](/windows/win32/Msi/nf-msi-msiusefeatureexa?branch=master)       | Increments usage count for a feature and indicates installation state. |
| [**MsiGetProductCode**](/windows/win32/Msi/nf-msi-msigetproductcodea?branch=master)   | Returns product code using the component code.                         |



 

## System Status Functions



| Name                                                             | Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiEnumProducts**](/windows/win32/Msi/nf-msi-msienumproductsa?branch=master)                       | Enumerates advertised products.                                                                                                                                                                                                   |
| [**MsiEnumProductsEx**](/windows/win32/Msi/nf-msi-msienumproductsexa?branch=master)                   | Enumerates through all the instances of advertised or installed products in a specified context. Available in Windows Installer  3.0 or later.                                                                                    |
| [**MsiEnumRelatedProducts**](/windows/win32/Msi/nf-msi-msienumrelatedproductsa?branch=master)         | Enumerates currently installed products having a specified upgrade code.                                                                                                                                                          |
| [**MsiEnumFeatures**](/windows/win32/Msi/nf-msi-msienumfeaturesa?branch=master)                       | Enumerates published features.                                                                                                                                                                                                    |
| [**MsiEnumComponents**](/windows/win32/Msi/nf-msi-msienumcomponentsa?branch=master)                   | Enumerates the installed components.                                                                                                                                                                                              |
| [**MsiEnumComponentsEx**](/windows/win32/Msi/nf-msi-msienumcomponentsexa?branch=master)               | Enumerates the installed components across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                 |
| [**MsiEnumClients**](/windows/win32/Msi/nf-msi-msienumclientsa?branch=master)                         | Enumerates the clients of an installed component.                                                                                                                                                                                 |
| [**MsiEnumClientsEx**](/windows/win32/Msi/nf-msi-msienumclientsexa?branch=master)                     | Enumerates the clients of an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                    |
| [**MsiEnumComponentQualifiers**](/windows/win32/Msi/nf-msi-msienumcomponentqualifiersa?branch=master) | Enumerates the advertised qualifiers for a component.                                                                                                                                                                             |
| [**MsiQueryFeatureState**](/windows/win32/Msi/nf-msi-msiqueryfeaturestatea?branch=master)             | Returns the installed state of a feature.                                                                                                                                                                                         |
| [**MsiQueryFeatureStateEx**](/windows/win32/Msi/nf-msi-msiqueryfeaturestateexa?branch=master)         | Returns the installed state for a product feature. Can query features of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |
| [**MsiQueryProductState**](/windows/win32/Msi/nf-msi-msiqueryproductstatea?branch=master)             | Returns the installed state for an application or application suite.                                                                                                                                                              |
| [**MsiGetFeatureUsage**](/windows/win32/Msi/nf-msi-msigetfeatureusagea?branch=master)                 | Returns usage metrics for a feature.                                                                                                                                                                                              |
| [**MsiGetProductInfo**](/windows/win32/Msi/nf-msi-msigetproductinfoa?branch=master)                   | Returns product information for published and installed products.                                                                                                                                                                 |
| [**MsiGetProductInfoEx**](/windows/win32/Msi/nf-msi-msigetproductinfoexa?branch=master)               | Returns product information for advertised and installed products. Can retrieve information on an instance of a product installed under a user account other than the current user. Available in Windows Installer  3.0 or later. |
| [**MsiGetUserInfo**](/windows/win32/Msi/nf-msi-msigetuserinfoa?branch=master)                         | Returns registered user information for an installed product.                                                                                                                                                                     |



 

## Product Query Functions



| Name                                                               | Description                                                                            |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**MsiOpenProduct**](/windows/win32/Msi/nf-msi-msiopenproducta?branch=master)                           | Opens a product to use with the functions that access the database.                    |
| [**MsiOpenPackage**](/windows/win32/Msi/nf-msi-msiopenpackagea?branch=master)                           | Opens a package to use with the functions that access the database.                    |
| [**MsiOpenPackageEx**](/windows/win32/Msi/nf-msi-msiopenpackageexa?branch=master)                       | Opens a package to use with the functions that access the database.                    |
| [**MsiIsProductElevated**](/windows/win32/Msi/nf-msi-msiisproductelevateda?branch=master)               | Checks whether the product is installed with elevated privileges.                      |
| [**MsiGetProductInfoFromScript**](/windows/win32/Msi/nf-msi-msigetproductinfofromscripta?branch=master) | Returns product information for an installer script file.                              |
| [**MsiGetProductProperty**](/windows/win32/Msi/nf-msi-msigetproductpropertya?branch=master)             | Retrieves properties in the product database.                                          |
| [**MsiGetShortcutTarget**](/windows/win32/Msi/nf-msi-msigetshortcuttargeta?branch=master)               | Examines a shortcut and returns its product, feature name, and component if available. |
| [**MsiGetFeatureInfo**](/windows/win32/Msi/nf-msi-msigetfeatureinfoa?branch=master)                     | Returns descriptive information for a feature.                                         |
| [**MsiVerifyPackage**](/windows/win32/Msi/nf-msi-msiverifypackagea?branch=master)                       | Verifies that a specified file is an installation package.                             |



 

## Patching Functions



| Name                                                                   | Description                                                                                                                                                        |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiApplyPatch**](/windows/win32/Msi/nf-msi-msiapplypatcha?branch=master)                                 | Invokes an installation and applies a patch package.                                                                                                               |
| [**MsiEnumPatches**](/windows/win32/Msi/nf-msi-msisourcelistaddmediadiska?branch=master)                    | Returns the GUID for each patch that is applied to a product, and a list of transforms from each patch that apply to the product.                                  |
| [**MsiGetPatchInfo**](/windows/win32/Msi/nf-msi-msigetpatchinfoa?branch=master)                             | Returns information about a patch.                                                                                                                                 |
| [**MsiRemovePatches**](/windows/win32/Msi/nf-msi-msiremovepatchesa?branch=master)                           | Uninstalls a patch from a product. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDeterminePatchSequence**](/windows/win32/Msi/nf-msi-msideterminepatchsequencea?branch=master)         | Determines the best application sequence for a set of patches and product. Available in Windows Installer 3.0.                                                     |
| [**MsiApplyMultiplePatches**](/windows/win32/Msi/nf-msi-msiapplymultiplepatchesa?branch=master)             | Applies one or more patches to products. Available in Windows Installer 3.0.                                                                                       |
| [**MsiEnumPatchesEx**](/windows/win32/Msi/nf-msi-msienumpatchesexa?branch=master)                           | Enumerates all patches applied for a product in a particular context or across all contexts. Available in Windows Installer 3.0.                                   |
| [**MsiGetPatchFileList**](/windows/win32/Msi/nf-msi-msigetpatchfilelista?branch=master)                     | When provided a list of .msp files this function retrieves the list of files that can be updated by the patches for the targe. Available in Windows Installer 4.0. |
| [**MsiGetPatchInfoEx**](/windows/win32/Msi/nf-msi-msigetpatchinfoexa?branch=master)                         | Queries for information about the application of a specified patch to a specified product. Available in Windows Installer 3.0.                                     |
| [**MsiExtractPatchXMLData**](/windows/win32/Msi/nf-msi-msiextractpatchxmldataa?branch=master)               | Extracts information from a patch. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDetermineApplicablePatches**](/windows/win32/Msi/nf-msi-msidetermineapplicablepatchesa?branch=master) | Determines the best set of patches required to update a product or set of products. Available in Windows Installer 3.0.                                            |



 

## File Query Functions



| Name                                                                     | Description                                                                                                 |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**MsiGetFileHash**](/windows/win32/Msi/nf-msi-msigetfilehasha?branch=master)                                 | Takes the path to a file and returns a 128-bit hash of that file.                                           |
| [**MsiGetFileSignatureInformation**](/windows/win32/Msi/nf-msi-msigetfilesignatureinformationa?branch=master) | Takes the path to a file that has been digitally signed and returns the file's signer certificate and hash. |
| [**MsiGetFileVersion**](/windows/win32/Msi/nf-msi-msigetfileversiona?branch=master)                           | Returns the version string and language string.                                                             |



 

## Transaction Management Functions



| Name                                               | Description                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiBeginTransaction**](/windows/win32/Msi/nf-msi-msibegintransactiona?branch=master) | Starts transaction processing of a multiple-package installation and returns an identifier for the transaction. This function is available beginning with Windows Installer 4.5.                    |
| [**MsiJoinTransaction**](/windows/win32/Msi/nf-msi-msijointransaction?branch=master)   | Requests that the Windows Installer make the current process the owner of the transaction installing a multi-package installation. This function is available beginning with Windows Installer 4.5. |
| [**MsiEndTransaction**](/windows/win32/Msi/nf-msi-msiendtransaction?branch=master)     | Commits or rolls back all the installations belonging to the transaction. This function is available beginning with Windows Installer 4.5.                                                          |



 

## Database Functions

In addition to the Windows Installer functions identified in the previous tables, you can manipulate information in the installation database by using the database access functions that are described in the [Database Functions](database-functions.md) section.

## Installer Structures

In addition, some information in the installation database is handled using the structures described in the [Installer Structures](installer-structures.md) section.

 

 




