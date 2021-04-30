---
description: A 64-bit package consists partially or entirely of 64-bit Windows Installer components.
ms.assetid: 615a5534-7c9e-4240-9a23-35f224122d0e
title: 64-bit Windows Installer Packages
ms.topic: article
ms.date: 05/31/2018
---

# 64-bit Windows Installer Packages

A 64-bit package consists partially or entirely of 64-bit [Windows Installer](windows-installer-components.md) components. The following list identifies the requirements for every 64-bit Windows Installer package:

-   The value "Intel64" must be entered in the platform field of the [**Template Summary**](template-summary.md) property if and only if the package runs on an Intel64 (Itanium) processor.
-   The value "x64" must be entered in the platform field of the [**Template Summary**](template-summary.md) property if and only if the package runs on an x64 processor.
-   The value "Arm64" must be entered in the platform field of the [**Template Summary**](template-summary.md) property if and only if the package runs on an Arm64 processor.
-   The [**Page Count Summary**](page-count-summary.md) property must be set to the integer 200 or greater, because Windows Installer 2.0 is the minimum version that is capable of installing 64-bit components. Packages for the Arm64 platform require a value of 500 or greater.
-   Each 64-bit Windows Installer component in the package must include the **msidbComponentAttributes64bit** bit in the Attributes column of the [Component Table](component-table.md).

For more information, see [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md) and [32-bit Windows Installer Packages](32-bit-windows-installer-packages.md).

 

 



