---
description: The RegisterProduct action registers the product information with the installer and with Add/Remove Programs. Additionally, this action stores the Windows Installer database package on the local computer.
ms.assetid: 689b09c7-9c17-42f5-ba31-cf9c6252e453
title: RegisterProduct Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterProduct Action

The RegisterProduct action registers the product information with the installer and with Add/Remove Programs. Additionally, this action stores the Windows Installer database package on the local computer.

The RegisterProduct action configures the controls displayed by the Add/Remove Programs in Control Panel. For more information, see [Configuring Add/Remove Programs with Windows Installer](configuring-add-remove-programs-with-windows-installer.md).

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages



| Field | Description of action data            |
|-------|---------------------------------------|
| \[1\] | Information about registered product. |



 

## Remarks

The RegisterProduct action is not performed during installation to an administrative installation point.

 

 



