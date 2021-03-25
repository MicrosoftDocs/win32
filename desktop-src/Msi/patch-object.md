---
description: The Patch object represents a unique instance of a patch that has been registered or applied.The object can be instantiated with the Patch property as &\#0034;WindowsInstaller.Installer.Patch(PatchCode, ProductCode, UserSid, Context)&\#0034;.
ms.assetid: c1283179-f2c8-42b8-a713-1c82e456f97c
title: Patch object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch object

The **Patch** object represents a unique instance of a patch that has been registered or applied.

The object can be instantiated with the **Patch** property as "WindowsInstaller.Installer.Patch(*PatchCode*, *ProductCode*, *UserSid*, *Context*)". For a machine context, the *UserSid* parameter must be an empty string. The *ProductCode* can be set to an empty string for patches that are registered only and not yet applied to any product. The *ProductCode* can be set to an empty string when only reading or updating a patch's source list information.

## Members

The **Patch** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Patch** object has these methods.



| Method                                                               | Description                                                                                                                             |
|:---------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**SourceListAddMediaDisk**](patch-sourcelistaddmediadisk.md)       | Add a disk to the set of registered disks.<br/>                                                                                   |
| [**SourceListAddSource**](patch-sourcelistaddsource.md)             | Add a network or URL source to the source list. <br/>                                                                             |
| [**SourceListClearAll**](patch-sourcelistclearall.md)               | Clears the complete source list of the specified type of sources.<br/>                                                            |
| [**SourceListClearMediaDisk**](patch-sourcelistclearmediadisk.md)   | Remove a disk from the set of registered disks from the source list. <br/>                                                        |
| [**SourceListClearSource**](patch-sourcelistclearsource.md)         | Remove a network or URL source from the source list.<br/>                                                                         |
| [**SourceListForceResolution**](patch-sourcelistforceresolution.md) | Clears the last used source from the source list. This forces a source list resolution the next time the source is required.<br/> |



 

### Properties

The **Patch** object has these properties.



| Property                                                  | Description                                                                                                |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**Context**](patch-context.md)<br/>               | Context of this patch instance is an MSIINSTALLCONTEXT value.<br/>                                   |
| [**MediaDisks**](patch-mediadisks.md)<br/>         | Enumerates all the media disks for this patch instance.<br/>                                         |
| [**PatchCode**](patch-patchcode.md)<br/>           | Returns the patch code.<br/>                                                                         |
| [**PatchProperty**](patch-patchproperty.md)<br/>   | Gets property information about a specific patch applied to a specific instance of the product.<br/> |
| [**ProductCode**](patch-productcode.md)<br/>       | Returns the product code.<br/>                                                                       |
| [**SourceListInfo**](patch-sourcelistinfo.md)<br/> | Gets and sets the source information properties. This is a read or write property.<br/>              |
| [**Sources**](patch-sources.md)<br/>               | Enumerates all the sources for this patch instance.<br/>                                             |
| [**State**](patch-state.md)<br/>                   | Installation state of the patch.<br/>                                                                |
| [**UserSid**](patch-usersid.md)<br/>               | Returns the User SID, under the account this patch instance is available.<br/>                       |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IPatch is defined as 000C10A1-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                            |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




