---
description: The Windows Installer supports advertisement of applications and features.
ms.assetid: 9e5158bc-4877-49d1-9bb9-4dd17abb444d
title: Platform Support of Advertisement
ms.topic: article
ms.date: 05/31/2018
---

# Platform Support of Advertisement

The Windows Installer supports advertisement of applications and features.

The following advertisement capabilities are available on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000.

-   Shortcuts and their icons.

-   Extensions and their icons specified in the [ProgId Table](progid-table.md).

-   Shell and command Verbs registered underneath the ProgId key.

-   CLSID contexts and InProcHandler.

-   Install-On-Demand through OLE is only available programmatically through [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) (C/C++), and **CreateObject Function (Visual Basic)** or **GetObject Function (Visual Basic)**.

> [!Note]
> AppId and Typelib information is only written when an advertised component is installed.
> 
> To support file name extensions, the application must be published to Active Directory by an administrator using Group Policy.

## Remarks

The installation of the product may not require a restart, but any advertised shortcuts do not work until the machine is restarted. The advertised shortcuts of subsequent installations work without a restart.

To ensure that advertised shortcuts work correctly, the package author should schedule a forced restart at the end of the installation.

To avoid unnecessary restarts of the system, schedule a restart to run only if no version of the Windows Installer is installed.

Conditional statements can check the [**ShellAdvtSupport**](shelladvtsupport.md) property and [**Version9X**](version9x.md) property. For more information about scheduling a conditional forced restarts, see [System Reboots](system-reboots.md) and [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md).

 

 
