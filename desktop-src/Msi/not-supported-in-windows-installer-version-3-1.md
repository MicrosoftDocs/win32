---
description: The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer&\#160;3.1 and earlier versions.
ms.assetid: fbf75dbe-3fa1-424b-83bb-cfd0b179107c
title: Not Supported in Windows Installer 3.1
ms.topic: article
ms.date: 05/31/2018
---

# Not Supported in Windows Installer 3.1

The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer 3.1 and earlier versions. The absence of a feature from this list does not guarantee that the feature is supported. See the main documentation to determine which Windows Installer version is required for a particular feature. For information about other Windows Installer versions see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

Windows Installer 3.1 is available for Windows Server 2003, Windows XP, or Windows 2000. For a list of all Windows Installer versions and redistributables, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

The following features are not supported in Windows Installer 3.1 and earlier versions.

[Installer Functions](installer-functions.md)

-   [**MsiGetPatchFileList**](/windows/desktop/api/Msi/nf-msi-msigetpatchfilelista)

[Properties](properties.md)

-   [**MSIARPSETTINGSIDENTIFIER**](msiarpsettingsidentifier.md)
-   [**MSIDEPLOYMENTCOMPLIANT**](msideploymentcompliant.md)
-   [**MSIDISABLERMRESTART**](msidisablermrestart.md)
-   [**MsiLogFileLocation**](msilogfilelocation.md)
-   [**MsiLogging**](msilogging.md)
-   [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md)
-   [**MsiRestartManagerSessionKey**](msirestartmanagersessionkey.md)
-   [**MSIRMSHUTDOWN**](msirmshutdown.md)
-   [**MsiRunningElevated**](msirunningelevated-.md)
-   [**MsiSystemRebootPending**](msisystemrebootpending.md)
-   [**MsiTabletPC**](msitabletpc.md)
-   [**MSIUSEREALADMINDETECTION**](msiuserealadmindetection.md)

[Summary Information Properties](summary-information-stream-reference.md)

-   The [**Word Count Summary Property**](word-count-summary.md) has new flag bits to specify whether the installation of the package requires elevated privileges.

[System Policy](system-policy.md)

-   [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md)
-   [DisableLoggingFromPackage](disableloggingfrompackage.md)

[Database Tables](database-tables.md)

-   [Shortcut Table](shortcut-table.md)

    New columns: DisplayResourceDLL, DisplayResourceId, DescriptionResourceDLL, and DescriptionResourceId

[Dialog Boxes](dialog-boxes.md)

-   [MsiRMFilesInUse Dialog](msirmfilesinuse-dialog.md)

[Control Attributes](control-attributes.md)

-   [ElevationShield](elevationshield-attribute.md)

[ControlEvents](control-events.md)

-   [RmShutdownAndRestart](rmshutdownandrestart-controlevent.md)

[External UI Message Types](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)

-   INSTALLLOGMODE\_RMFILESINUSE

[Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md)

-   **msidbComponentAttributesDisableRegistryReflection** attribute in [Component Table](component-table.md)

[Automation Interface](automation-interface.md)

-   Methods of [**Installer Object**](installer-object.md)

    -   [**Installer.AdvertiseProduct**](installer-advertiseproduct.md)
    -   [**Installer.AdvertiseScript**](installer-advertisescript.md)
    -   [**Installer.CreateAdvertiseScript**](installer-createadvertisescript.md)
    -   [**Installer.ProvideAssembly**](installer-provideassembly.md)

-   Properties of [**Installer Object**](installer-object.md)

    -   [**Installer.PatchFiles**](installer-patchfiles.md)
    -   [**Installer.ProductElevated**](installer-productelevated.md)
    -   [**Installer.ProductInfoFromScript**](installer-productinfofromscript.md)

## Notes

The Windows Installer service must run on Windows Vista to enable use of [Restart Manager](../rstmgr/restart-manager-portal.md), [*User Account Control*](u-gly.md), and [User Account Control (UAC) Patching](user-account-control--uac--patching.md). For information, see [Using Windows Installer with Restart Manager](using-windows-installer-with-restart-manager.md) and [Using Windows Installer with UAC](using-windows-installer-with-uac.md) and [User Account Control (UAC) Patching](user-account-control--uac--patching.md).

Windows Installer 3.1 supports Windows File Protection (WFP) and does not support Windows Resource Protection (WRP). WRP in Windows Server 2008 and Windows Vista replaces WFP in Windows Server 2003, Windows XP, and Windows 2000. For information about Windows Installer and WFP, see [Using Windows Installer and Windows Resource Protection](windows-resource-protection-on-windows-vista.md).

 

 
