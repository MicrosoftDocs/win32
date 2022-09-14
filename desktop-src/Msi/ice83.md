---
description: ICE83 validates the MsiAssembly table.
ms.assetid: dd290c73-6528-482d-8276-ac56d0fec181
title: ICE83
ms.topic: article
ms.date: 05/31/2018
---

# ICE83

ICE83 validates the [MsiAssembly table](msiassembly-table.md). This ICE custom action posts an error if the key path for a component containing a Win32 assembly is set to the manifest file. Explicitly the error is posted if the value entered in the KeyPath field of the [Component table](component-table.md) equals the value entered in the File\_Manifest field of the MsiAssembly table. This ICE custom action posts an error if there is at least one record in the MsiAssembly table and the [InstallExecuteSequence table](installexecutesequence-table.md) does not contain both the [MsiPublishAssemblies Action](msipublishassemblies-action.md) and [MsiUnpublishAssemblies Action](msiunpublishassemblies-action.md).

## Result

ICE83 posts the following errors.



| ICE83 error                                                                                                   | Description                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The key path for Win32 SXS Assembly (Component\_=\[1\]) SHOULD NOT be its manifest file                       | ICE83 posts this error when the KeyPath field for a Win32 Assembly is set to its manifest file (Component.KeyPath == MsiAssembly.File\_Manifest). \[1\] is KeyPath in Component table                          |
| Both MsiPublishAssemblies AND MsiUnpublishAssemblies actions MUST be present in InstallExecuteSequence table. | ICE83 posts this error when there is at least one entry in the MsiAssembly table but the InstallExecuteSequence table does not contain both the MsiAssemblyPublish action and the MsiAssemblyUnpublish action. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



