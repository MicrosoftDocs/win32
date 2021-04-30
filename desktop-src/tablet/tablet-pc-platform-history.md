---
description: This section describes version history for Tablet PC Technology.
ms.assetid: 69eb161a-2330-456f-b7b8-234cf02c8b58
title: Tablet PC Platform History
ms.topic: article
ms.date: 05/31/2018
---

# Tablet PC Platform History

This section describes version history for Tablet PC Technology.

## Platform Description

The Tablet PC Technology components enable you to develop applications designed for Tablet PC hardware.

These components can be used to build applications that run on Windows XP Tablet PC Edition 2005, Windows Vista, Windows 7, Windows Server 2008 R2, and certain other earlier operating systems.

The Windows Presentation Foundation also supports development of Tablet PC applications.

## Version History

### Tablet Platform in Windows 7 and Windows Server 2008 R2

Windows 7 introduces additional language support, the math input control, and custom dictionaries. [Windows Touch](../wintouch/windows-touch-portal.md) features have also been added to Windows operating systems.

Windows Server 2008 R2 introduces support for additional languages, custom dictionaries, and server-side recognition.

The following features enhance Tablet functionality and let developers deliver new applications that support practical scenarios for end users.

-   The math input control allows input of math formulas and functions from handwritten text in Windows 7.
-   In an effort to improve text recognition, Windows 7 and Windows Server 2008 R2 support custom dictionaries so that administrators can directly enable support for word lists.
-   Windows Touch supports input from multiple touch sources through new window messages in addition to a gesture recognition API that supports panning, zooming, and rotating.
-   Windows Server 2008 R2 supports server-side recognition of form input, and also supports custom dictionaries for server-side recognition. With the addition of these features, developers and administrators can create and customize powerful applications that support handwriting recognition from the server side.

### Tablet Platform in Windows Vista

The Tablet PC Technology binaries have been updated in Windows Vista. The updated Tablet PC Technology includes new ink analysis APIs and a COM version of the Stylus Input APIs. Applications written against previous versions of the Tablet PC Technology run on Windows Vista without modification.

The Tablet PC Technology components are available only as part of the Windows SDK beginning with the release of Windows Vista. For more information, see [What's New in Tablet PC Development](what-s-new-in-tablet-pc-development.md).

### Version 1.7

Tablet PC Development Kit 1.7 extended the development functionality beyond that available in version 1.5, adding the Stylus Input APIs and support for ink on the Web.

In the past, the functionality of version 1.5 was in a separate binary, but in the Tablet PC Development Kit 1.7, all functionality was placed into one single binary.

### Version 1.5

Version 1.5 of the Development Kit superseded version 1.1. It provided pen input panel APIs and the Divider object.

> [!Note]  
> If you install the Tablet PC Development Kit version 1.5, after installation you must reestablish references to the Microsoft ink assembly in applications written against previous versions of the Tablet PC SDK before compiling and running.

 

### Version 1.1

Version 1.1 of the Development Kit superseded version 1.0. The version 1.1 release consisted solely of updates to the documentation; the platform binaries were not changed between version 1.1 of the Development Kit and the shipped version of Windows XP Tablet PC Edition. Therefore, applications developed against the version 1.1 Development Kit do not need to redistribute any components to use platform features when installed on Tablet PCs.

> [!Note]  
> Applications being distributed to non–Tablet PC operating systems can use a subset of Tablet PC platform features. These applications must include the redistributed merge module that shipped in the version 1.1 Development Kit with their setup.

 

### Version 1.0

Version 1.0 of the Development Kit was superseded by version 1.1.

 

 
