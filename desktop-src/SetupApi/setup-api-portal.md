---
description: Installs device drivers from programs with a set up script and inf files. Write a setup program for device set up and driver installation. This api is no longer recommended for the purpose of installing software applications.
ms.assetid: 96a9e472-9b92-4976-9379-dc0c96524963
title: Setup API
ms.topic: article
ms.date: 05/31/2018
---

# Setup API

## Purpose

The Setup API provides a set of functions that a setup application calls to perform installation operations.

## Where applicable

These setup functions are available to develop a setup application. Setup API should no longer be used for installing applications. Instead, use the [Windows Installer](/windows/desktop/Msi/windows-installer-portal)for developing application installers. Setup API continues to be used for installing device drivers.

The Setup API is intended for the development of desktop style applications.

## Developer audience

A developer can use the Setup API if their setup application requires the following functionality:

-   Queuing of files.
-   Installation of files.
-   Handling of installation errors and prompting for media.
-   Updating registry entries.
-   Logging of files as they are installed.
-   Storage of the most recently used source paths.

## Run-time requirements

For information about which operating systems are required to use a particular function, see the Requirements section of the documentation for the function.

## In this section



| Topic                                 | Description                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------|
| [Overview](overview.md)<br/>   | General information about Setup API.<br/>                                             |
| [Reference](reference.md)<br/> | Documentation of Setup API data types, structures, functions, and notifications.<br/> |



 

 

