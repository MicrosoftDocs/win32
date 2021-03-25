---
description: The Product object represents a unique instance of a product that is either advertised, installed or unknown.The object can be instantiated with the Product property as &\#0034;WindowsInstaller.Installer.Product(ProductCode, UserSid, Context)&\#0034;.
ms.assetid: 1fa89239-051a-4b3a-913a-12c7c093f35b
title: Product object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product object

The **Product** object represents a unique instance of a product that is either advertised, installed or unknown.

The object can be instantiated with the **Product** property as "WindowsInstaller.Installer.Product(*ProductCode*, *UserSid*, *Context*)". *UserSid* must be NULL for per-machine context. *UserSid* can be null to specified current user, when context is not per-machine. *ProductCode* and *Context* parameters are required.

## Members

The **Product** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Product** object has these methods.



| Method                                                                 | Description                                                                                                        |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**SourceListAddMediaDisk**](product-sourcelistaddmediadisk.md)       | Add a disk to the set of registered disks.<br/>                                                              |
| [**SourceListAddSource**](product-sourcelistaddsource.md)             | Add a network or URL source to the source list.<br/>                                                         |
| [**SourceListClearAll**](product-sourcelistclearall.md)               | Clears the complete source list of the specified type of sources.<br/>                                       |
| [**SourceListClearMediaDisk**](product-sourcelistclearmediadisk.md)   | Remove a disk from the set of registered disks from the source list.<br/>                                    |
| [**SourceListClearSource**](product-sourcelistclearsource.md)         | Remove a network or URL source from the source list.<br/>                                                    |
| [**SourceListForceResolution**](product-sourcelistforceresolution.md) | Clears the last used source. This forces a source list resolution the next time the source is required.<br/> |



 

### Properties

The **Product** object has these properties.



| Property                                                      | Description                                                                                 |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**ComponentState**](product-componentstate.md)<br/>   | The state of a specified component for this product instance. <br/>                   |
| [**Context**](product-context.md)<br/>                 | Context of this product instance as an MSIINSTALLCONTEXT value. <br/>                 |
| [**FeatureState**](product-featurestate.md)<br/>       | The state of a specified feature for this product instance. <br/>                     |
| [**InstallProperty**](product-installproperty.md)<br/> | The value of a specified property. <br/>                                              |
| [**MediaDisks**](product-mediadisks.md)<br/>           | Enumerates all the media disks for this product instance.<br/>                        |
| [**ProductCode**](product-productcode.md)<br/>         | Returns the product code. <br/>                                                       |
| [**SourceListInfo**](product-sourcelistinfo.md)<br/>   | Get and set the source information properties. This is a read or write property.<br/> |
| [**Sources**](product-sources.md)<br/>                 | Enumerates all the sources for this product instance.<br/>                            |
| [**State**](product-state.md)<br/>                     | Installation state of the product.<br/>                                               |
| [**UserSid**](product-usersid.md)<br/>                 | Returns the User SID, under which account this product instance is available.<br/>    |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




