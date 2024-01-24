---
description: The information in this topic identifies the additions and changes that are available in Windows Installer&\#160;5.0.
ms.assetid: c088c15b-0eef-4a92-bb65-e7fe871afbfe
title: What's New in Windows Installer 5.0
ms.topic: article
ms.date: 11/08/2019
---

# What's New in Windows Installer 5.0

The information in this topic identifies the additions and changes that are available in Windows Installer 5.0.

Windows Installer 5.0 is included with the following versions of Windows:

* Client: Windows 7 and all later versions.
* Server: Windows Server 2008 R2 and all later versions.

> [!NOTE]
> There is no redistributable for Windows Installer 5.0. For a list of redistributables available for previous versions of Windows Installer, see [Windows Installer Redistributables](windows-installer-redistributables.md). For a complete list of Windows Installer versions, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

This page is provided as a guide to the documentation. You should refer to the Requirements section on the main reference pages to determine the actual operating system requirements. Parts of the Windows Installer that are not linked to from this page may be available in another version of the Windows Installer. For information about other Windows Installer versions, see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

[Standard Actions](standard-actions.md)

-   [MsiConfigureServices](msiconfigureservices-action.md)

[Installer Functions](installer-functions.md)

-   [**MsiEnumComponentsEx**](/windows/desktop/api/Msi/nf-msi-msienumcomponentsexa)
-   [**MsiEnumClientsEx**](/windows/desktop/api/Msi/nf-msi-msienumclientsexa)
-   [**MsiGetComponentPathEx**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpathexa)

[Column Data Types](column-data-types.md)

-   [**FormattedSDDLText**](formattedsddltext.md)

[Properties](properties.md)

-   [**MSIFASTINSTALL**](msifastinstall.md)
-   [**MSIINSTALLPERUSER**](msiinstallperuser.md)

[Summary Information Properties](summary-information-stream-reference.md)

-   The [**Template Summary**](template-summary.md) has new values to indicate the database is compatible with Windows RT or the Arm64 platform.

[Database Tables](database-tables.md)

-   [MsiServiceConfig Table](msiserviceconfig-table.md)
-   [MsiServiceConfigFailureActions Table](msiserviceconfigfailureactions-table.md)
-   [MsiShortcutProperty Table](msishortcutproperty-table.md)
-   [MsiLockPermissionsEx Table](msilockpermissionsex-table.md)

[ControlEvents](control-events.md)

-   [MsiPrint ControlEvent](msiprint-controlevent.md)
-   [MsiLaunchApp ControlEvent](msilaunchapp-controlevent.md)

[Controls](controls.md)

-   [Hyperlink Control](hyperlink-control.md)

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)

-   [ICE101](ice-101.md)
-   [ICE102](ice-102.md)
-   [ICE103](ice-103.md)
-   [ICE104](ice-104.md)
-   [ICE105](ice-105.md)

[Automation Interface](automation-interface.md)

-   Properties of the [**Installer Object**](installer-object.md)

    -   [**Installer.ClientsEx**](installer-clientsex.md)
    -   [**Installer.ComponentsEx**](installer-componentsex.md)
    -   [**Installer.ComponentPathEx**](installer-componentpathex.md)

-   Properties of the [**Components Object**](components.md)

    -   [**Components.ComponentCode**](component-componentcode.md)
    -   [**Components.UserSID**](component-usersid.md)
    -   [**Components.Context**](component-context.md)

-   Properties of the [**Client Object**](client.md)

    -   [**Client.ProductCode**](client-productcode.md)
    -   [**Client.ComponentCode**](client-componentcode.md)
    -   [**Client.UserSID**](client-usersid.md)
    -   [**Client.Context**](client-context.md)

-   Properties of the [**ComponentInfo**](componentinfo.md) Object

    -   [**ComponentInfo.ComponentCode**](componentinfo-componentcode.md)
    -   [**ComponentInfo.Path**](componentinfo-path.md)
    -   [**ComponentInfo.State**](componentinfo-state.md)

## Notes

Setup developers can use Windows Installer 5.0 to author a single installation package capable of either per-machine installation or per-user installation of the application. For more information, see [Single Package Authoring](single-package-authoring.md). The internal consistency evaluator [ICE105](ice-105.md) checks that the package has been authored to be installed in a per-user context. An application capable of being installed, updated, run, and removed by a standard user without elevation is called a Per-User Application (PUA.) A PUA can provide a better user experience, minimize effects on the system and other users of the computer, and reserves UAC prompting to situations that actually require the elevation of the user's privileges. The Single Package Authoring features of Windows Installer 5.0 can facilitate the development of Per-User Applications.

Services configuration options enable a Windows Installer package to customize the [services](../services/services.md) on a computer. For more information, see [Using Services Configuration](using-services-configuration.md).

Beginning with Windows Installer 5.0, a Windows Installer package is capable to secure new accounts, Windows [services](../services/services.md), files, folders, and registry keys. The [MsiLockPermissionsEx](msilockpermissionsex-table.md) table can specify a security descriptor that denies permissions, specifies inheritance of permissions from a parent resource, or specifies the permissions of a new account. For information, see [Securing Resources](securing-resources-.md).

Windows Installer 5.0 can enumerate all components installed on the computer and obtain the key path for the component. For more information, see [Enumerating Components](enumerating-components-.md).

Windows Installer 5.0 running on Windows Server 2012 or Windows 8 supports the installation of approved apps on Windows RT. A Windows Installer package, patch, or transform that has not been signed by Microsoft cannot be installed on Windows RT. The [**Template Summary**](template-summary.md) property indicates the platform that is compatible with the installation database and should include the value for Windows RT.

Windows Installer 5.0 running on Windows 10 on Arm64 processors supports the installation of applications compiled specifically for the Arm64 platform.  The [**Template Summary**](template-summary.md) property of these packages needs to include the value Arm64. 

 
