---
description: Windows Installer can optimize patching to reduce the time that is required to apply patches to installed applications.
ms.assetid: 2bb1c94a-55b6-4aee-b86d-ee9e1f8ed290
title: Patch Optimization
ms.topic: article
ms.date: 05/31/2018
---

# Patch Optimization

Windows Installer can optimize patching to reduce the time that is required to apply patches to installed applications.

**Windows Installer 2.0:** Not supported. For versions of Windows Installer released before Windows Installer 3.0, patching runs a complete repair installation of the application, which can take significantly more time.

**Windows Installer 3.0 and later:** The patching process only changes the parts of an application that are modified by a patch.

**Windows Installer 3.1 and later:** Beginning with Windows Installer 3.1, patch optimization requires that all patches in the transaction have the OptimizedInstallMode property set to 1 (one) in the [MsiPatchMetadata Table](msipatchmetadata-table.md).

If a patch only modifies the following tables, Windows Installer 3.0 or later skips the actions that are associated with all the other tables, even if those actions are listed in the sequence tables of the original application installation package (.msi file).

-   [AdminExecuteSequence](adminexecutesequence-table.md)
-   [AdminUISequence](adminuisequence-table.md)
-   [Condition](condition-table.md)
-   [CustomAction](customaction-table.md)
-   [File](file-table.md)
-   [FileSFPCatalog](filesfpcatalog-table.md)
-   [InstallExecuteSequence](installexecutesequence-table.md)
-   [InstallUISequence](installuisequence-table.md)
-   [Media](media-table.md)
-   [MoveFile](movefile-table.md)
-   [MsiAssembly](msiassembly-table.md)
-   [MsiDigitalCertificate](msidigitalcertificate-table.md)
-   [MsiDigitalSignature](msidigitalsignature-table.md)
-   [MsiFileHash](msifilehash-table.md)
-   [MsiPatchHeaders](msipatchheaders-table.md)
-   [Patch](patch-table.md)
-   [PatchPackage](patchpackage-table.md)
-   [Property](property-table.md)
-   [Registry](registry-table.md)
-   [SFPCatalog](sfpcatalog-table.md)
-   [TypeLib](typelib-table.md)
-   [\_Columns](-columns-table.md)
-   [\_Storages](-storages-table.md)
-   [\_Streams](-streams-table.md)
-   [\_Tables](-tables-table.md)
-   [\_TransformView Table](-transformview-table.md)
-   [\_Validation](-validation-table.md)

To turn off the patch optimization option, use the [DisableFlyWeightPatching](disableflyweightpatching.md) policy.

 

 



