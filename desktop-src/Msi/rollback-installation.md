---
description: When the Windows Installer processes the installation script for the installation of a product or application, it simultaneously generates a rollback script and saves a copy of every file deleted during the installation.
ms.assetid: 6c70e788-beb0-46db-94b0-1bbaac972acf
title: Rollback Installation
ms.topic: article
ms.date: 05/31/2018
---

# Rollback Installation

When the Windows Installer processes the installation script for the installation of a product or application, it simultaneously generates a rollback script and saves a copy of every file deleted during the installation. These files are kept in a hidden system directory and are automatically deleted once the installation is successfully completed. If however the installation is unsuccessful, the installer automatically performs a rollback installation that returns the system to its original state.

Automatic rollback of an unsuccessful installation is the default behavior of the installer. To disable rollback during an installation use one of the following:

-   [**DISABLEROLLBACK Property**](-disablerollback.md)
-   [**PROMPTROLLBACKCOST Property**](promptrollbackcost.md)
-   [DisableRollback Action](disablerollback-action.md)
-   [DisableRollback](disablerollback.md)
-   [EnableRollback ControlEvent](enablerollback-controlevent.md)

Whenever rollback is disabled, the installer sets the [**RollbackDisabled**](rollbackdisabled.md) property.

If an installation uses [custom actions](custom-actions.md), additional authoring of the installation package is required to use rollback functionality. For more information, see [Rollback Custom Actions](rollback-custom-actions.md).

 

 



