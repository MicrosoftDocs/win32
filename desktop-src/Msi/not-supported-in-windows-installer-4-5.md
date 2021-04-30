---
description: The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer&\#160;4.5 and earlier versions.
ms.assetid: 89662e62-53fb-4b50-8583-80518c6fda6d
title: Not Supported in Windows Installer 4.5
ms.topic: article
ms.date: 05/31/2018
---

# Not Supported in Windows Installer 4.5

The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer 4.5 and earlier versions. The absence of a feature from this list does not guarantee that the feature is supported. See the main documentation to determine which Windows Installer version is required for a particular feature. For information about other Windows Installer versions see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

Windows Installer 4.5 is available as a redistributable for Windows Server 2008, Windows Vista with Service Pack 1 (SP1), Windows XP with Service Pack 2 (SP2) and later, and Windows Server 2003 with Service Pack 1 (SP1) and later. For a complete list of all Windows Installer versions and redistributables, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

The following features are not supported in Windows Installer 4.5 and earlier versions.

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
-   [Bitmap Control](bitmap-control.md) support of WIC image file formats

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)

-   [ICE102](ice-102.md)
-   [ICE103](ice-103.md)
-   [ICE104](ice-104.md)
-   [ICE105](ice-105.md)

[Automation Interface](automation-interface.md)

-   Properties of the [**Installer Object**](installer-object.md)

    -   [**Installer.ClientsEx**](installer-clientsex.md)
    -   [**Installer.ComponentsEx**](installer-componentsex.md)
    -   [**Installer.ComponentPathEx**](installer-componentpathex.md)

-   Properties of the [**Component Object**](components.md)

    -   [**Component.ComponentCode**](component-componentcode.md)
    -   [**Component.UserSID**](component-usersid.md)
    -   [**Component.Context**](component-context.md)

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

Windows Installer 4.5 does not support some features that enable a single installation package to be installed in either the per-machine or per-user installation context. For more information, see [Single Package Authoring](single-package-authoring.md).

Windows Installer 4.5 does not support some services configuration options that can enable a package to customize the [services](../services/services.md) on a computer. For more information, see [Using Services Configuration](using-services-configuration.md).

Windows Installer 4.5 does not support some features that enable the Windows Installer to secure new accounts, Windows [services](../services/services.md), files, folders, and registry keys. For information, see [Securing Resources](securing-resources-.md).

Windows Installer 4.5 does not support some features that enable the installation to enumerate all components installed on the computer and obtain the key path for the component. For more information, see [Enumerating Components](enumerating-components-.md).

 

 
