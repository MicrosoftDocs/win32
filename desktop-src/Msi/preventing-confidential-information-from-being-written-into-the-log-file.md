---
description: Developers can prevent confidential information, such as passwords, from being entered into the log file during a Windows Installer installation.
ms.assetid: 950c3c56-3f16-4e1a-875f-d31f45065076
title: Preventing Confidential Information from Being Written into the Log File
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Confidential Information from Being Written into the Log File

When using the Windows Installer, you can prevent confidential information, for example passwords, from being entered into the log file and made visible.

-   The Installer never writes the information in the Password column of the [ServiceInstall table](serviceinstall-table.md) into the log.
-   You can prevent the Installer from writing the property that is associated with an [Edit Control](edit-control.md) into the log by setting the [Password Control Attribute](password-control-attribute.md). The property associated with an Edit Control that has the Password Control Attribute is hidden even if the [Debug](debug.md) policy is set to a value of 7.
-   You can prevent the Installer from writing a private property into the log by including the property in the [**MsiHiddenProperties**](msihiddenproperties.md) property.
    > [!Note]  
    > This method can make confidential information entered on a command line visible in the log. When the [Debug](debug.md) policy is set to a value of 7, the installer will write information entered on a command line into the log. This makes the property entered on a command line visible even if the property is included in the [**MsiHiddenProperties**](msihiddenproperties.md) property.

     

-   You can prevent the information in the Target column of the [CustomAction](customaction-table.md) Table from being written into the log by including the HideTarget bit flag in the Type field of the CustomAction table. The value of this flag is 8192 (0x2000). For more information, see [Custom Action Hidden Target Option](custom-action-hidden-target-option.md).

 

 



