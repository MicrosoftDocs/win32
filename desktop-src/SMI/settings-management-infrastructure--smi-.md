---
title: Settings Management Infrastructure
description: Provides a standardized infrastructure to access and manipulate Windows Vista settings that are modifiable by users and applications.
ms.assetid: 54e031cd-265e-4cd9-8aa1-a5b87d2f56bc
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Settings Management Infrastructure

Settings Management Infrastructure (SMI) provides a standardized infrastructure to access and manipulate Windows Vista settings that are modifiable by users and applications. A setting is mutable data that can affect component behavior. Settings are created during installation or servicing of Windows Vista. When settings are created, developers can use the SMI APIs to query and manipulate them. Settings that are managed by SMI have attributes that describe their properties. For example, an attribute can describe the type of the setting, its default value and whether it can be migrated. For more information and a list of attributes, see [SMI Attributes](smi-settings-and-attributes.md).

In addition to querying setting attributes, a user can modify a setting using the SMI API. Tools such as Windows Migration uses SMI APIs to make decisions when migrating settings that are managed by SMI. An OEM Preinstallation Kit (OPK) image manager tool uses SMI APIs to extract settings that are customizable by use of an answer (unattend) file. Customers such as OEMs, IT Cooperate, and system builders use answer files to customize the Windows image before it is deployed. The answer file is consulted by the unattend process during setup or migration.

> [!Note]  
> SMI APIs are intended to be used only for windows operating system deployment scenarios.

 

 

 




