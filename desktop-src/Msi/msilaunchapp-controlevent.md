---
description: This control event runs a specified file. If the file does not exist, or if the event fails, Windows Installer logs the error in the verbose log without displaying a dialog box containing an error message.
ms.assetid: a185c5a1-6584-4916-967a-313e6b7cf97c
title: MsiLaunchApp ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# MsiLaunchApp ControlEvent

This control event runs a specified file. If the file does not exist, or if the event fails, Windows Installer logs the error in the verbose log without displaying a dialog box containing an error message.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This ControlEvent is available beginning with Windows Installer 5.0.

## Published By

This ControlEvent is published by the installer.

## Argument

The fields of the argument value are delimited by spaces. The first field contains a string value that specifies the file that is to be run. Use a string value of \[\#*filekey*\] to identify the file and replace *filekey* with the file's identifier appearing in the File column of the [File](file-table.md) table. Any remaining fields of the argument can contain parameters being used by the file being run.

## Action on Subscribers

This ControlEvent performs no actions on subscribers.

## Typical Use

To enable a user to choose to run a file at the end of an installation. This event can be conditioned on a property set by a [CheckBox](checkbox-control.md) control displayed on the final dialog box of the installation. The CheckBox control should not be displayed during the removal of the package.

 

 



