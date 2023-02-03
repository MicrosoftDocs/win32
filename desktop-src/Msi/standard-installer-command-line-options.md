---
description: See standard command-line options for the Microsoft Standard Installer Msiexec.exe, the executable used for interpreting packages and installing programs. 
ms.assetid: b1707c88-1cca-45ab-bb23-6002bfd5204e
title: Microsoft Standard Installer command-line options
ms.topic: article
ms.date: 09/10/2021
---

# Microsoft Standard Installer command-line options

This article describes standard command-line options for the Microsoft Standard Installer *Msiexec.exe*, the app you use to interpret packages and install products.

Command-line options are case insensitive.

Msiexec sets and returns an error level that corresponds to [system error codes](../debug/system-error-codes.md).

> [!NOTE]
> The Msiexec command-line options are available beginning with Windows Installer 3.0. The [Windows Installer command-line options](command-line-options.md) are available with Windows Installer 3.0 and earlier. This article lists the Windows Installer command-line option that corresponds to each Msiexec option.

## /help

Help and quick reference option. Displays the correct usage of the setup command, including a list of all switches and behavior. You can display the usage description in the user interface. Incorrect use of any other option invokes this help option.

The equivalent Windows Installer command-line option is `/?`.

### Example

`Msiexec /help`.

## /quiet

Quiet display option. The installer runs an installation without displaying a user interface. No prompts, messages, or dialog boxes display to the user. The user can't cancel the installation.

Use the `/norestart` or `/forcerestart` standard command-line options to control reboots. If no reboot option is specified, the installer restarts the computer whenever necessary without displaying any prompt or warning to the user.

The equivalent Windows Installer command-line option is `/qn`.

### Examples

`Msiexec /package Application.msi /quiet`

`Msiexec /uninstall Application.msi /quiet`

`Msiexec /update msipatch.msp /quiet`

`Msiexec /uninstall msipatch.msp /package  Application.msi /quiet`

## /passive

Passive display option. The installer displays a progress bar to the user that indicates that an installation is in progress, but displays no prompts or error messages to the user. The user can't cancel the installation.

Use the `/norestart` or `/forcerestart` standard command-line options to control reboots. If no reboot option is specified, the installer restarts the computer whenever necessary without displaying any prompt or warning to the user.

The equivalent Windows Installer command-line option is `/qb!`- with `REBOOTPROMPT=S` set on the command line.

### Example

`msiexec /package Application.msi /passive`

## /norestart

Never restart option. The installer never restarts the computer after the installation.

The equivalent Windows Installer command line has `REBOOT=ReallySuppress` set on the command line.

### Example

`msiexec /package Application.msi /norestart`.

## /forcerestart

Always restart option. The installer restarts the computer after every installation.

The equivalent Windows Installer command line has `REBOOT=Force` set on the command line.

### Example

`msiexec /package Application.msi /forcerestart`

## /promptrestart

Prompt before restarting option. Displays a message that a restart is required to complete the installation and asks the user whether to restart the system now. You can't use this option with the `/quiet` option.

The equivalent Windows Installer command line has `REBOOTPROMPT = ""` set on the command line.

## /uninstall (product)

Uninstall product option. Uninstalls a product.

The equivalent Windows Installer Command-Line Option is `/x.`

### Parameter

`<Package.msi|ProductCode>`

## /uninstall (patch)

Uninstall update option. Uninstalls an update patch.

The equivalent Windows Installer command-line option is `/I` with `MSIPATCHREMOVE=Update1.msp | PatchGUID1[;Update2.msp | PatchGUID2]` set on the command line.

### Parameter

`/package <Package.msi | ProductCode> /uninstall [;Update2.msp | PatchGUID2]`

## /log

Log option. Writes logging information into a log file at the specified existing path. The path to the log file location must already exist. The installer doesn't create the directory structure for the log file.

For more information about all the methods that are available for setting the logging mode, see [Normal logging](normal-logging.md) for the Windows Installer.

The equivalent Windows Installer Command-Line Option is: `/L*`.

The following information is entered into the log:

- Status messages
- Nonfatal warnings
- All error messages
- Startup of actions
- Action-specific records
- User requests
- Initial UI parameters
- Out-of-memory or fatal exit information
- Out-of-disk-space messages
- Terminal properties

## /package

Install product option. Installs or configures a product.

The equivalent Windows Installer command-line option is `/I`.

### Parameter

`<Package.msi|ProductCode>`

## /update

Install patches option. Installs one or multiple patches.

The equivalent Windows Installer command line has `PATCH = [msipatch.msp]<;PatchGuid2>` set on the command line.

### Parameter

`[;Update2.msp]`
