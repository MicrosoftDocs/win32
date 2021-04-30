---
description: Whether a patch can be uninstalled depends upon how the patch was authored, the version of Windows Installer used to install the patch, and the changes made by the patch to the application.
ms.assetid: 95a5365c-e2ae-4e35-9aeb-67d04e67c7df
title: Uninstallable Patches
ms.topic: article
ms.date: 05/31/2018
---

# Uninstallable Patches

Whether a patch can be uninstalled depends upon how the patch was authored, the version of Windows Installer used to install the patch, and the changes made by the patch to the application. If a patch is not uninstallable, then the only way to remove the patch is to uninstall the entire application and reinstall without applying the patch being removed.

You can call for the uninstallation of patches applied with Windows Installer version 3.0 by using [Command Line Options](command-line-options.md), the [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa) function, or the [**RemovePatches method**](installer-removepatches.md) as described in the [Uninstalling Patches](uninstalling-patches.md) section. The Windows Installer verifies that each of the patches listed for removal in the [**MSIPATCHREMOVE**](msipatchremove.md) property is uninstallable. If the user does not have privileges to remove the patch, the patch is unknown for the product, patch policy prevents removal, or the patch was marked as not uninstallable, the installer returns an error indicating a failed installation transaction.

**Windows Installer 2.0:** Not supported. Patches applied using a version of Windows Installer that is earlier than Windows Installer 3.0 are not uninstallable.

## Patches that are Not Uninstallable

A patch (.msp file) applied to an installed application is not uninstallable in the following cases. The only method to remove a patch that is not uninstallable is to uninstall the patched application and then reinstall the application without reapplying the patch. In this case, you must reapply any patches that you do not wish to be removed from the application.

-   Patches applied using a version of Windows Installer that is less than Windows Installer 3.0 are not uninstallable.
-   Patches applied to applications installed on a computer that has had the [DisablePatchUninstall](disablepatchuninstall.md) policy set by an administrator are not uninstallable. When this [machine policy](machine-policies.md)has been set, no patches on the computer can be uninstalled, even by an administrator.
-   Patches that do not have a [MsiPatchMetadata](msipatchmetadata-table.md) table in their database are not uninstallable.
-   Patches that do not include the following row in their [MsiPatchMetadata](msipatchmetadata-table.md) table are not uninstallable. The patch is not uninstallable for other values of Company, Property, and Value.

    | Company | Property     | Value |
    |---------|--------------|-------|
    | {Null}  | AllowRemoval | 1     |

    

     

-   The patch has been applied to an application installed in a context for which the user has insufficient privileges to uninstall patches. The words "Not Allowed" in the following table indicate that an administrator or non-administrator user cannot uninstall patches from patched applications installed in this context. The word "Allowed" in this table means that privileges do not prevent an administrator or non-administrator user from uninstalling patches, however for any of the other reasons discussed in this section, it still might not be possible to uninstall the patch.

    | application Installation Context        | Administrator Uninstall of Patch | Non-Administrator Uninstall of Patch                                                                                                                                                                                                                                                                             |
    |-----------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Per-Machine                             | Allowed                          | Generally Not Allowed The only exception is if the patch was applied using (LUA) patching. A patch marked as a LUA patch is uninstallable by either administrators or non-administrators. LUA patching is only available for packages installed per-machine from media and require special authoring.<br/> |
    | Per-User Non-Managed for Current User   | Allowed                          | Allowed                                                                                                                                                                                                                                                                                                          |
    | Per-User Non-Managed for Different User | Not Allowed                      | Not Allowed                                                                                                                                                                                                                                                                                                      |
    | Per-User Managed for Current User       | Allowed                          | Not Allowed                                                                                                                                                                                                                                                                                                      |
    | Per-User Managed for Different User     | Not Allowed                      | Not Allowed                                                                                                                                                                                                                                                                                                      |

    

     

-   A [major upgrade](major-upgrades.md) applied by a patch is not uninstallable. Major Upgrades of an application should be performed by installing the upgraded application (.msi file) rather than a patch.
-   Patches applied to an administrative installation are not uninstallable. Patching administrative installations is not recommended. The current set of patches should be applied on the user's computer after the user installs the application from the administrative image. This can prevent the [package code](package-codes.md) cached on the user's computer from becoming different than the package code on the administrative installation. If the package code cached on the user's computer becomes different from that on the administrative installation, reinstall the application from the administrative installation and then patch the client computer.
-   When a patch adds new content to any of the tables in the following list, Windows Installer marks the patch as being not uninstallable. An uninstallable patch can add new files, assemblies, registry entries, components, or features to an installation by adding new rows to database tables that are not included in this list.

    -   [AppId](appid-table.md)
    -   [BindImage](bindimage-table.md)
    -   [Class](class-table.md)
    -   [Complus](complus-table.md)
    -   [CreateFolder](createfolder-table.md)
    -   [DuplicateFile](duplicatefile-table.md)
    -   [Environment](environment-table.md)
    -   [Extension](extension-table.md)
    -   [Font](font-table.md)
    -   [IniFile](inifile-table.md)
    -   [IsolatedComponent](isolatedcomponent-table.md)
    -   [LockPermissions](lockpermissions-table.md)
    -   [MsiLockPermissionsEx](msilockpermissionsex-table.md)
    -   [MIME](mime-table.md)
    -   [MoveFile](movefile-table.md)
    -   [MsiServiceConfig](msiserviceconfig-table.md)
    -   [MsiServiceConfigFailureActions](msiserviceconfigfailureactions-table.md)
    -   [ODBCAttribute](odbcattribute-table.md)
    -   [ODBCDataSource](odbcdatasource-table.md)
    -   [ODBCDriver](odbcdriver-table.md)
    -   [ODBCSourceAttribute](odbcsourceattribute-table.md)
    -   [ODBCTranslator](odbctranslator-table.md)
    -   [ProgId](progid-table.md)
    -   [PublishComponent](publishcomponent-table.md)
    -   [RemoveIniFile](removeinifile-table.md)
    -   [SelfReg](selfreg-table.md)
    -   [ServiceControl](servicecontrol-table.md)
    -   [ServiceInstall](serviceinstall-table.md)
    -   [TypeLib](typelib-table.md)
    -   [Verb](verb-table.md)
    -   [!Note]  
        > If a patch adds new content to the [RemoveFile](removefile-table.md) or [RemoveRegistry](removeregistry-table.md) tables, Windows Installer does not mark the patch as being not uninstallable. However, the patch is not uninstallable unless the resource to remove the new content does not already exist in the original installation package. For example, if the patch adds a new row to the RemoveFile table, the removed file cannot be restored by uninstalling the patch if the file is external to the [File table](file-table.md). The file must have been authored in the File table of the original package plus applied patches for the patch to be uninstallable.

         

## Related topics

<dl> <dt>

[Patch Sequencing](sequencing-patches.md)
</dt> <dt>

[Removing Patches](removing-patches.md)
</dt> <dt>

[Uninstalling Patches](uninstalling-patches.md)
</dt> <dt>

[Patch Uninstall Custom Actions](patch-uninstall-custom-actions.md)
</dt> <dt>

[**MSIPATCHREMOVE**](msipatchremove.md)
</dt> <dt>

[**MsiEnumapplicationsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
</dt> <dt>

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
</dt> </dl>

 

 




