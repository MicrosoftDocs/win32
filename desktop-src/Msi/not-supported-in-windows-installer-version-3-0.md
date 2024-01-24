---
description: The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer&\#160;3.0 and earlier versions.
ms.assetid: 35be6da4-2a20-4a7a-9f6e-0420cd5a227e
title: Not Supported in Windows Installer 3.0
ms.topic: article
ms.date: 05/31/2018
---

# Not Supported in Windows Installer 3.0

The Windows Installer functions, tables, and properties listed on this page are not supported by Windows Installer 3.0 and earlier versions. The absence of a feature from this list does not guarantee that the feature is supported. See the main documentation to determine which Windows Installer version is required for a particular feature. For information about other Windows Installer versions see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

Windows Installer 3.0 is available for Windows Server 2003, Windows XP, or Windows 2000. For a list of all Windows Installer versions and redistributables, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

The following features are not supported in Windows Installer 3.0 and earlier versions.

[Installer Functions](installer-functions.md)

-   [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord)
-   [**MsiNotifySidChange**](/windows/desktop/api/Msi/nf-msi-msinotifysidchangea)

Callback Function Prototype

-   [**INSTALLUI\_HANDLER\_RECORD**](/windows/win32/api/msi/nc-msi-installui_handler_record)

[Database Tables](database-tables.md)

-   The Value column of the [MsiPatchMetadata Table](msipatchmetadata-table.md) accepts **OptimizedInstallMode** and **MinorUpdateTargetRTM**.

[Properties](properties.md)

-   [**Msix64 Property**](msix64.md)

[Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md)

-   The [**Template Summary Property**](template-summary.md) accepts the value x64.

[Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)

-   [ICE99](ice99.md)

 

 
