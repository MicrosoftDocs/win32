---
description: An Installer object must be initially created to load the automation support that is required for COM to access the installer functions. This object provides wrappers to create the top-level objects and access their methods.
ms.assetid: fefc3e39-073e-4869-86b7-27d20a3b337b
title: Installer object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer object

An **Installer** object must be initially created to load the automation support that is required for COM to access the installer functions. This object provides wrappers to create the top-level objects and access their methods.

You can create the **Installer** object from the ProgId "WindowsInstaller.Installer".

## Members

The **Installer** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Installer** object has these methods.



| Method                                                                   | Description                                                                                                                                                                                     |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddSource**](installer-addsource.md)                                 | Adds a source to the list of valid network sources in the sourcelist.<br/>                                                                                                                |
| [**AdvertiseProduct**](installer-advertiseproduct.md)                   | Advertises an installation package.<br/>                                                                                                                                                  |
| [**AdvertiseScript**](installer-advertisescript.md)                     | Advertises an installation package. <br/>                                                                                                                                                 |
| [**ApplyMultiplePatches**](installer-applymultiplepatches.md)           | Applies one or more patches to products eligible to receive the patch. Sets the [**PATCH**](patch.md) property to the path of the patch packages provided.<br/>                          |
| [**ApplyPatch**](installer-applypatch.md)                               | Invokes an installation and sets the [**PATCH**](patch.md) property to the path of the patch package for each product listed by the patch package as eligible to receive the patch.<br/> |
| [**ClearSourceList**](installer-clearsourcelist.md)                     | Removes all network sources from the sourcelist.<br/>                                                                                                                                     |
| [**CollectUserInfo**](installer-collectuserinfo.md)                     | Invokes a user interface wizard sequence that collects and stores both user information and the product code.<br/>                                                                        |
| [**ConfigureFeature**](installer-configurefeature.md)                   | Configures the installed state of a product feature.<br/>                                                                                                                                 |
| [**ConfigureProduct**](installer-configureproduct.md)                   | Installs or uninstalls a product.<br/>                                                                                                                                                    |
| [**CreateAdvertiseScript**](installer-createadvertisescript.md)         | Generates an advertise script.<br/>                                                                                                                                                       |
| [**CreateRecord**](installer-createrecord.md)                           | Returns a new [**Record**](record-object.md) object with the requested number of fields.<br/>                                                                                            |
| [**EnableLog**](installer-enablelog.md)                                 | Enables logging of the selected message type for all subsequent installation sessions in the current process space.<br/>                                                                  |
| [**ExtractPatchXMLData**](installer-extractpatchxmldata.md)             | Extracts information from a patch as an XML string.<br/>                                                                                                                                  |
| [**FileHash**](installer-filehash.md)                                   | Takes the path to a file and returns a 128-bit hash of that file.<br/>                                                                                                                    |
| [**FileSignatureInfo**](installer-filesignatureinfo.md)                 | Takes the path to a file and returns a **SAFEARRAY** of bytes that represents the hash or the encoded certificate.<br/>                                                                   |
| [**FileSize**](installer-filesize.md)                                   | Returns the size of the specified file.<br/>                                                                                                                                              |
| [**FileVersion**](installer-fileversion.md)                             | Returns the version string or language string of the specified path.<br/>                                                                                                                 |
| [**ForceSourceListResolution**](installer-forcesourcelistresolution.md) | Forces the installer to search the source list for a valid product source the next time a source is required.<br/>                                                                        |
| [**InstallProduct**](installer-installproduct.md)                       | Opens an installer package and initializes an installation session.<br/>                                                                                                                  |
| [**LastErrorRecord**](installer-lasterrorrecord.md)                     | Returns a [**Record**](record-object.md) object that contains error parameters for the most recent error from the function that produced the error record.<br/>                          |
| [**OpenDatabase**](installer-opendatabase.md)                           | Opens an existing database or creates a new one.<br/>                                                                                                                                     |
| [**OpenPackage**](installer-openpackage.md)                             | Opens an installer package for use with functions that access the product database and install engine.<br/>                                                                               |
| [**OpenProduct**](installer-openproduct.md)                             | Opens an installer package for an installed product using the product code.<br/>                                                                                                          |
| [**ProvideAssembly**](installer-provideassembly.md)                     | Returns the installed path of an assembly.<br/>                                                                                                                                           |
| [**ProvideComponent**](installer-providecomponent.md)                   | Returns the full component path and performs any necessary installation.<br/>                                                                                                             |
| [**ProvideQualifiedComponent**](installer-providequalifiedcomponent.md) | Returns the full component path and performs any necessary installation.<br/>                                                                                                             |
| [**RegistryValue**](installer-registryvalue.md)                         | Reads information about a specified registry key of value.<br/>                                                                                                                           |
| [**ReinstallFeature**](installer-reinstallfeature.md)                   | Reinstalls features or corrects problems with installed features.<br/>                                                                                                                    |
| [**ReinstallProduct**](installer-reinstallproduct.md)                   | Reinstalls a product or corrects installation problems in an installed product.<br/>                                                                                                      |
| [**RemovePatches**](installer-removepatches.md)                         | Removes one or more patches to products eligible to receive the patch. <br/>                                                                                                              |
| [**UseFeature**](installer-usefeature.md)                               | Increments the usage count for a particular feature and returns the installation state for that feature.<br/>                                                                             |



 

### Properties

The **Installer** object has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                                                                                                                            |
|:----------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClientsEx**](installer-components.md)<br/>                        |                       | Returns a [**RecordList**](recordlist-object.md) object that lists products that use a specified installed component.<br/> **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>       |
| [**ComponentClients**](installer-componentclients.md)<br/>           |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of clients of a specified component.<br/>                                                                                                                           |
| [**ComponentPath**](installer-componentpath.md)<br/>                 |                       | Returns the full path to an installed component.<br/>                                                                                                                                                                                            |
| [**ComponentPathEx**](installer-componentpathex.md)<br/>             |                       | Returns a [**RecordList**](recordlist-object.md) object that gives the full path of a specified installed component. <br/> **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>       |
| [**ComponentQualifiers**](installer-componentqualifiers.md)<br/>     |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of registered qualifiers for the specified component.<br/>                                                                                                          |
| [**Components**](installer-components.md)<br/>                       |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of installed components for all products.<br/>                                                                                                                      |
| [**ComponentsEx**](installer-componentsex.md)<br/>                   |                       | Returns a [**RecordList**](recordlist-object.md) object that lists installed components.<br/> **[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                    |
| [**Environment**](installer-environment.md)<br/>                     | Read/write<br/> | The string value for an environment variable of the current process.<br/>                                                                                                                                                                        |
| [**FeatureParent**](installer-featureparent.md)<br/>                 |                       | Specifies the parent feature of a feature.<br/>                                                                                                                                                                                                  |
| [**Features**](installer-features.md)<br/>                           |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of published features for the specified product.<br/>                                                                                                               |
| [**FeatureState**](installer-featurestate.md)<br/>                   |                       | Returns the installed state of a feature.<br/>                                                                                                                                                                                                   |
| [**FeatureUsageCount**](installer-featureusagecount.md)<br/>         |                       | Returns the number of times that the feature has been used.<br/>                                                                                                                                                                                 |
| [**FeatureUsageDate**](installer-featureusagedate.md)<br/>           |                       | Returns the date that the specified feature was last used.<br/>                                                                                                                                                                                  |
| [**FileAttributes**](installer-fileattributes.md)<br/>               |                       | Returns a number that represents the combined file attributes for the designated path to a file or folder.<br/>                                                                                                                                  |
| [**Patches**](installer-patches.md)<br/>                             |                       | Returns a [**StringList**](stringlist-object.md) object that contains all the patches applied to the product.<br/>                                                                                                                              |
| [**PatchesEx**](installer-patchesex.md)<br/>                         |                       | Enumerates a collection of [**Patch**](patch-object.md) objects.<br/>                                                                                                                                                                           |
| [**PatchFiles**](installer-patchfiles.md)<br/>                       |                       | Returns a [**StringList**](stringlist-object.md) object that contains a list of files that can be updated by the provided list of patches.<br/>                                                                                                 |
| [**PatchInfo**](installer-patchinfo.md)<br/>                         |                       | Returns information about a patch.<br/>                                                                                                                                                                                                          |
| [**PatchTransforms**](installer-patchtransforms.md)<br/>             |                       | Returns the semicolon delimited list of transforms that are in the specified patch package and applied to the specified product.<br/>                                                                                                            |
| [**ProductElevated**](installer-productelevated.md)<br/>             |                       | Returns True if the product is managed or False if the product is not managed.<br/>                                                                                                                                                              |
| [**ProductInfo**](installer-productinfo.md)<br/>                     |                       | Returns the value of the specified attribute for an installed or published product.<br/>                                                                                                                                                         |
| [**ProductInfoFromScript**](installer-productinfofromscript.md)<br/> |                       | Returns the value of the specified attribute that is stored in an advertise script.<br/>                                                                                                                                                         |
| [**Products**](installer-products.md)<br/>                           |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of all products installed or advertised for the current user and machine. <br/>                                                                                     |
| [**ProductsEx**](installer-productsex.md)<br/>                       |                       | Enumerates a collection of [**Product**](product-object.md) objects.<br/>                                                                                                                                                                       |
| [**ProductState**](installer-productstate-property.md)<br/>          |                       | Returns the install state information for a product.<br/>                                                                                                                                                                                        |
| [**QualifierDescription**](installer-qualifierdescription.md)<br/>   |                       | Returns a text string that describes the qualified component.<br/>                                                                                                                                                                               |
| [**RelatedProducts**](installer-relatedproducts.md)<br/>             |                       | Returns a [**StringList**](stringlist-object.md) object enumerating the set of all products installed or advertised for the current user and machine with a specified [**UpgradeCode**](upgradecode.md) property in their property table.<br/> |
| [**ShortcutTarget**](installer-shortcuttarget.md)<br/>               |                       | Examines a shortcut and returns its product, feature name and component if available.<br/>                                                                                                                                                       |
| [**SummaryInformation**](installer-summaryinformation.md)<br/>       |                       | Returns a [**SummaryInfo**](summaryinfo-object.md) object that can be used to examine, update and add properties to the summary information stream of a package or transform.<br/>                                                              |
| [**UILevel**](installer-uilevel.md)<br/>                             | Read/write<br/> | Indicates the type of user interface to be used when opening and processing subsequent packages within the current process space.<br/>                                                                                                           |
| [**Version**](installer-version.md)<br/>                             |                       | Returns the string representation of the current version of Windows Installer.<br/>                                                                                                                                                              |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[Using the Automation Interface](using-the-automation-interface.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




