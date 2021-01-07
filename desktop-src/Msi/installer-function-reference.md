---
description: To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.
ms.assetid: 05a16915-6b47-4d51-b62a-5a4d92b87e50
title: Installer Function Reference
ms.topic: article
ms.date: 05/31/2018
---

# Installer Function Reference

To enable Windows Installer in your application, you must use the installer functions. The tables in this topic identify the functions by category.

## User Interface and Logging Functions



| Name                                                     | Description                                                                           |
|----------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)             | Enables the internal user interface of the installer.                                 |
| [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)             | Enables an external user-interface handler that receives messages in a string format. |
| [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord) | Enables an external user-interface handler that receives messages in a record format. |
| [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga)                     | Sets the log mode for all installations in the calling process.                       |



 

## Handle Management Functions



| Name                                             | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| [**MsiCloseHandle**](/windows/desktop/api/Msi/nf-msi-msiclosehandle)         | Closes an open installation handle.                           |
| [**MsiCloseAllHandles**](/windows/desktop/api/Msi/nf-msi-msicloseallhandles) | Closes all open installation handles. Do not use for cleanup. |



 

## Installation and Configuration Functions



| Name                                                                     | Description                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiAdvertiseProduct**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproducta)                       | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa)                   | Advertises a product.                                                                                                                                                                                                        |
| [**MsiAdvertiseScript**](/windows/desktop/api/Msi/nf-msi-msiadvertisescripta)                         | Copies an advertise script file into specified locations.                                                                                                                                                                    |
| [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta)                           | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta)                       | Installs or removes an application or application suite.                                                                                                                                                                     |
| [**MsiConfigureProductEx**](/windows/desktop/api/Msi/nf-msi-msiconfigureproductexa)                   | Installs or removes an application or application suite. A product command-line can be specified.                                                                                                                            |
| [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta)                       | Reinstalls or repairs an installation.                                                                                                                                                                                       |
| [**MsiConfigureFeature**](/windows/desktop/api/Msi/nf-msi-msiconfigurefeaturea)                       | Configures the installed state of a feature.                                                                                                                                                                                 |
| [**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea)                       | Validates or repairs features.                                                                                                                                                                                               |
| [**MsiInstallMissingComponent**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingcomponenta)         | Installs missing components.                                                                                                                                                                                                 |
| [**MsiInstallMissingFile**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingfilea)                   | Installs missing files.                                                                                                                                                                                                      |
| [**MsiNotifySidChange**](/windows/desktop/api/Msi/nf-msi-msinotifysidchangea)                         | Notifies and updates the Windows Installer internal information with changes to user SIDs. Available beginning with Windows Installer 3.1.                                                                                   |
| [**MsiProcessAdvertiseScript**](/windows/desktop/api/Msi/nf-msi-msiprocessadvertisescripta)           | Processes an advertise script file into specified locations.                                                                                                                                                                 |
| [**MsiSourceListAddSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourcea)                 | Adds or reorders the sources of a patch or product in a specified context.                                                                                                                                                   |
| [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa)             | Adds or reorders the sources of a patch or product in a specified context. Creates a source list for a patch that does not exist in a specified context. Available in Windows Installer  3.0.                                |
| [**MsiSourceListClearSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearsourcea)             | Removes an existing source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                               |
| [**MsiSourceListClearAll**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearalla)                   | Removes all the existing sources of a specific source type for a specified product instance.                                                                                                                                 |
| [**MsiSourceListClearAllEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearallexa)               | Removes all the existing sources of a specific source type for a specified product instance. Available in Windows Installer  3.0.                                                                                            |
| [**MsiSourceListForceResolution**](/windows/desktop/api/Msi/nf-msi-msisourcelistforceresolutiona)     | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list.                                      |
| [**MsiSourceListForceResolutionEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistforceresolutionexa) | Removes the registration of the current source of the product or patch, which is registered as the property "LastUsedSource". This function does not affect the registered source list. Available in Windows Installer  3.0. |
| [**MsiSourceListGetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistgetinfoa)                     | Retrieves information about the source list for a product or patch in a specific context.                                                                                                                                    |
| [**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa)                     | Sets the most recently used source for a product or patch in a specified context. Available in Windows Installer  3.0.                                                                                                       |
| [**MsiSourceListEnumMediaDisks**](/windows/desktop/api/Msi/nf-msi-msisourcelistenummediadisksa)       | Enumerates the list of disks registered for the media source for a patch or product. Available in Windows Installer  3.0.                                                                                                    |
| [**MsiSourceListAddMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska)           | Adds or updates a disk of the media source of a registered product or patch. Available in Windows Installer  3.0.                                                                                                            |
| [**MsiSourceListClearMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearmediadiska)      | Removes an existing registered disk under the media source for a product or patch in a specific context. Available in Windows Installer  3.0.                                                                                |
| [**MsiSourceListEnumSources**](/windows/desktop/api/Msi/nf-msi-msisourcelistenumsourcesa)             | Enumerates the sources in the source list of a specified patch or product. Available in Windows Installer  3.0.                                                                                                              |



 

## Component-Specific Functions



| Name                                                                     | Description                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya)                         | Installs and returns the full component path for an assembly.                                                                                                                                                                 |
| [**MsiProvideComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidecomponenta)                       | Installs and returns the full component path of a component.                                                                                                                                                                  |
| [**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta)     | Installs and returns the full component path of a qualified component.                                                                                                                                                        |
| [**MsiProvideQualifiedComponentEx**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponentexa) | Installs and returns the full component path of a qualified component that is published by a product.                                                                                                                         |
| [**MsiGetComponentPath**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpatha)                       | Returns the full path or registry key to an installed component.                                                                                                                                                              |
| [**MsiGetComponentPathEx**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpathexa)                   | Returns the full path or registry key to an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/> |
| [**MsiLocateComponent**](/windows/desktop/api/Msi/nf-msi-msilocatecomponenta)                         | Returns the full path to an installed component without a product code.                                                                                                                                                       |
| [**MsiQueryComponentState**](/windows/desktop/api/Msi/nf-msi-msiquerycomponentstatea)                 | Returns the installed state for a component. Can query components of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |



 

## Application-Only Functions



| Name                                             | Description                                                            |
|--------------------------------------------------|------------------------------------------------------------------------|
| [**MsiCollectUserInfo**](/windows/desktop/api/Msi/nf-msi-msicollectuserinfoa) | Stores user information from an installation wizard.                   |
| [**MsiUseFeature**](/windows/desktop/api/Msi/nf-msi-msiusefeaturea)           | Increments usage count for a feature and indicates installation state. |
| [**MsiUseFeatureEx**](/windows/desktop/api/Msi/nf-msi-msiusefeatureexa)       | Increments usage count for a feature and indicates installation state. |
| [**MsiGetProductCode**](/windows/desktop/api/Msi/nf-msi-msigetproductcodea)   | Returns product code using the component code.                         |



 

## System Status Functions



| Name                                                             | Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiEnumProducts**](/windows/desktop/api/Msi/nf-msi-msienumproductsa)                       | Enumerates advertised products.                                                                                                                                                                                                   |
| [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)                   | Enumerates through all the instances of advertised or installed products in a specified context. Available in Windows Installer  3.0 or later.                                                                                    |
| [**MsiEnumRelatedProducts**](/windows/desktop/api/Msi/nf-msi-msienumrelatedproductsa)         | Enumerates currently installed products having a specified upgrade code.                                                                                                                                                          |
| [**MsiEnumFeatures**](/windows/desktop/api/Msi/nf-msi-msienumfeaturesa)                       | Enumerates published features.                                                                                                                                                                                                    |
| [**MsiEnumComponents**](/windows/desktop/api/Msi/nf-msi-msienumcomponentsa)                   | Enumerates the installed components.                                                                                                                                                                                              |
| [**MsiEnumComponentsEx**](/windows/desktop/api/Msi/nf-msi-msienumcomponentsexa)               | Enumerates the installed components across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                 |
| [**MsiEnumClients**](/windows/desktop/api/Msi/nf-msi-msienumclientsa)                         | Enumerates the clients of an installed component.                                                                                                                                                                                 |
| [**MsiEnumClientsEx**](/windows/desktop/api/Msi/nf-msi-msienumclientsexa)                     | Enumerates the clients of an installed component across user accounts and installation context. **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                    |
| [**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa) | Enumerates the advertised qualifiers for a component.                                                                                                                                                                             |
| [**MsiQueryFeatureState**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestatea)             | Returns the installed state of a feature.                                                                                                                                                                                         |
| [**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa)         | Returns the installed state for a product feature. Can query features of an instance of a product installed under user accounts other than the current user. Available in Windows Installer  3.0 or later.                        |
| [**MsiQueryProductState**](/windows/desktop/api/Msi/nf-msi-msiqueryproductstatea)             | Returns the installed state for an application or application suite.                                                                                                                                                              |
| [**MsiGetFeatureUsage**](/windows/desktop/api/Msi/nf-msi-msigetfeatureusagea)                 | Returns usage metrics for a feature.                                                                                                                                                                                              |
| [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa)                   | Returns product information for published and installed products.                                                                                                                                                                 |
| [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa)               | Returns product information for advertised and installed products. Can retrieve information on an instance of a product installed under a user account other than the current user. Available in Windows Installer  3.0 or later. |
| [**MsiGetUserInfo**](/windows/desktop/api/Msi/nf-msi-msigetuserinfoa)                         | Returns registered user information for an installed product.                                                                                                                                                                     |



 

## Product Query Functions



| Name                                                               | Description                                                                            |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**MsiOpenProduct**](/windows/desktop/api/Msi/nf-msi-msiopenproducta)                           | Opens a product to use with the functions that access the database.                    |
| [**MsiOpenPackage**](/windows/desktop/api/Msi/nf-msi-msiopenpackagea)                           | Opens a package to use with the functions that access the database.                    |
| [**MsiOpenPackageEx**](/windows/desktop/api/Msi/nf-msi-msiopenpackageexa)                       | Opens a package to use with the functions that access the database.                    |
| [**MsiIsProductElevated**](/windows/desktop/api/Msi/nf-msi-msiisproductelevateda)               | Checks whether the product is installed with elevated privileges.                      |
| [**MsiGetProductInfoFromScript**](/windows/desktop/api/Msi/nf-msi-msigetproductinfofromscripta) | Returns product information for an installer script file.                              |
| [**MsiGetProductProperty**](/windows/desktop/api/Msi/nf-msi-msigetproductpropertya)             | Retrieves properties in the product database.                                          |
| [**MsiGetShortcutTarget**](/windows/desktop/api/Msi/nf-msi-msigetshortcuttargeta)               | Examines a shortcut and returns its product, feature name, and component if available. |
| [**MsiGetFeatureInfo**](/windows/desktop/api/Msi/nf-msi-msigetfeatureinfoa)                     | Returns descriptive information for a feature.                                         |
| [**MsiVerifyPackage**](/windows/desktop/api/Msi/nf-msi-msiverifypackagea)                       | Verifies that a specified file is an installation package.                             |



 

## Patching Functions



| Name                                                                   | Description                                                                                                                                                        |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha)                                 | Invokes an installation and applies a patch package.                                                                                                               |
| [**MsiEnumPatches**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska)                    | Returns the GUID for each patch that is applied to a product, and a list of transforms from each patch that apply to the product.                                  |
| [**MsiGetPatchInfo**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoa)                             | Returns information about a patch.                                                                                                                                 |
| [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)                           | Uninstalls a patch from a product. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDeterminePatchSequence**](/windows/desktop/api/Msi/nf-msi-msideterminepatchsequencea)         | Determines the best application sequence for a set of patches and product. Available in Windows Installer 3.0.                                                     |
| [**MsiApplyMultiplePatches**](/windows/desktop/api/Msi/nf-msi-msiapplymultiplepatchesa)             | Applies one or more patches to products. Available in Windows Installer 3.0.                                                                                       |
| [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa)                           | Enumerates all patches applied for a product in a particular context or across all contexts. Available in Windows Installer 3.0.                                   |
| [**MsiGetPatchFileList**](/windows/desktop/api/Msi/nf-msi-msigetpatchfilelista)                     | When provided a list of .msp files this function retrieves the list of files that can be updated by the patches for the targe. Available in Windows Installer 4.0. |
| [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)                         | Queries for information about the application of a specified patch to a specified product. Available in Windows Installer 3.0.                                     |
| [**MsiExtractPatchXMLData**](/windows/desktop/api/Msi/nf-msi-msiextractpatchxmldataa)               | Extracts information from a patch. Available in Windows Installer 3.0.                                                                                             |
| [**MsiDetermineApplicablePatches**](/windows/desktop/api/Msi/nf-msi-msidetermineapplicablepatchesa) | Determines the best set of patches required to update a product or set of products. Available in Windows Installer 3.0.                                            |



 

## File Query Functions



| Name                                                                     | Description                                                                                                 |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha)                                 | Takes the path to a file and returns a 128-bit hash of that file.                                           |
| [**MsiGetFileSignatureInformation**](/windows/desktop/api/Msi/nf-msi-msigetfilesignatureinformationa) | Takes the path to a file that has been digitally signed and returns the file's signer certificate and hash. |
| [**MsiGetFileVersion**](/windows/desktop/api/Msi/nf-msi-msigetfileversiona)                           | Returns the version string and language string.                                                             |



 

## Transaction Management Functions



| Name                                               | Description                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiBeginTransaction**](/windows/desktop/api/Msi/nf-msi-msibegintransactiona) | Starts transaction processing of a multiple-package installation and returns an identifier for the transaction. This function is available beginning with Windows Installer 4.5.                    |
| [**MsiJoinTransaction**](/windows/desktop/api/Msi/nf-msi-msijointransaction)   | Requests that the Windows Installer make the current process the owner of the transaction installing a multi-package installation. This function is available beginning with Windows Installer 4.5. |
| [**MsiEndTransaction**](/windows/desktop/api/Msi/nf-msi-msiendtransaction)     | Commits or rolls back all the installations belonging to the transaction. This function is available beginning with Windows Installer 4.5.                                                          |



 

## Database Functions

In addition to the Windows Installer functions identified in the previous tables, you can manipulate information in the installation database by using the database access functions that are described in the [Database Functions](database-functions.md) section.

## Installer Structures

In addition, some information in the installation database is handled using the structures described in the [Installer Structures](installer-structures.md) section.

 

 




