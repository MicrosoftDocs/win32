---
description: If this per-machine system policy is set to 1, no package on the system gets the shared component functionality enabled by the msidbComponentAttributesShared attribute in the Component table.
ms.assetid: 28181f8c-8c03-4962-a142-c35d0dd88940
title: DisableSharedComponent
ms.topic: article
ms.date: 05/31/2018
---

# DisableSharedComponent

If this per-machine [system policy](system-policy.md) is set to 1, no package on the system gets the shared component functionality enabled by the **msidbComponentAttributesShared** attribute in the [Component table](component-table.md). The default value is 0, which enables the shared component functionality for components marked with **msidbComponentAttributesShared** in all packages.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This function is available beginning with Windows Installer 4.5.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 



