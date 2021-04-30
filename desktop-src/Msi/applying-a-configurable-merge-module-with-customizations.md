---
description: Follow the general guidelines for applying merge modules described in Applying Merge Modules.
ms.assetid: 6035b1a9-d452-4020-9fe3-c20ba874a2ed
title: Applying a Configurable Merge Module with Customizations
ms.topic: article
ms.date: 05/31/2018
---

# Applying a Configurable Merge Module with Customizations

Follow the general guidelines for applying merge modules described in [Applying Merge Modules](applying-merge-modules.md). In addition, merge module consumers must do the following to configure a merge module at the time of installation:

-   Use a merge module that is authored to have configurable settings. For more information, see [Creating a Merge Module that Can Be Configured by the End-User](creating-a-merge-module-that-can-be-configured-by-the-end-user.md)
-   Use a merge and configuration tool that calls Mergemod.dll version 2.0 or later. Earlier versions of Mergmod.dll cannot configure merge module settings. Authors should create merge modules that provide default values and are compatible with earlier versions of Mergmod.dll.
-   Provide customization information when prompted by the configuration client tool. Authors should create merge modules that use default values when a user declines to provide information.

 

 



