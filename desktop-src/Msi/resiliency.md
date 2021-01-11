---
description: Resiliency is the ability of an application to recover gracefully from situations in which a vital component is missing, or has been replaced by an incompatible version.
ms.assetid: c0504a84-6d51-4734-a55d-f1d1ebcb3e73
title: Resiliency
ms.topic: article
ms.date: 05/31/2018
---

# Resiliency

Resiliency is the ability of an application to recover gracefully from situations in which a vital component is missing, or has been replaced by an incompatible version. By authoring an installation package and using the [Installer Functions](installer-functions.md), developers can use the Windows Installer to produce resilient applications capable of recovering from such situations.

-   Use the installer's source list to increase the resiliency of applications that rely on network resources. For more information, see [Source Resiliency](source-resiliency.md).
-   Use the installer's API to check whether a vital feature, component, file, or file version is installed.
-   Use the installer's API to check the path to a component at run time. This reduces your application's dependency on static file paths, which commonly differ between computers.
-   Use the installer to reinstall damaged shortcuts, registry entries, and other components without having to rerun setup.
-   Increase the resiliency of your product's installation by leaving the rollback capability of the installer enabled. For more information, see [Rollback Installation](rollback-installation.md).

 

 



