---
description: The Windows Installer organizes an installation around the concepts of components and features.
ms.assetid: c560441e-89c5-4f82-837b-988c3f404d37
title: Components and Features
ms.topic: article
ms.date: 05/31/2018
---

# Components and Features

The Windows Installer organizes an installation around the concepts of components and features.

A feature is a part of the application's total functionality that a user may decide to install independently. For more information, see [Windows Installer Features](windows-installer-features.md).

A component is a piece of the application or product to be installed. The installer always installs or removes a component from a user's computer as a coherent piece. Components are usually hidden from the user. When a user selects a feature for installation, the installer determines which components must be installed to provide that feature. For more information, see [Windows Installer Components](windows-installer-components.md).

Authors of installation packages need to decide how to divide their application into features and components. The selection of features is primarily determined by the application's functionality from the user's perspective. Because components commonly must be shared across applications, or even across products, it is recommended that authors follow a standard method for selecting components. For more information, see [Organizing Applications into Components](organizing-applications-into-components.md).

 

 



