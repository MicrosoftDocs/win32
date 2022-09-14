---
description: Adhere to these guidelines when authoring a 64-bit merge module.
ms.assetid: 326c274b-981e-4b21-a4fb-0060c178a01e
title: Using 64-bit Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Using 64-bit Merge Modules

A 64-bit merge module has any of the characteristics identified in this this topic.

-   The merge module contains at least one component that has been compiled for 64-bit operating systems.
-   The merge module contains no 64-bit components, but is intended for use only with [64-bit Windows Installer](64-bit-windows-installer-packages.md) packages.

Merge modules can be used as follows:

-   A 64-bit merge module can be merged into a [64-bit Windows Installer](64-bit-windows-installer-packages.md) package. The [**Template Summary**](template-summary.md) properties in the merge module and in the Windows Installer package must be set to the same type of 64-bit processor. A x64 merge module can be merged only into x64 packages and an Intel64 merge module can be merged only into Intel64 packages.
-   A 32-bit merge module can be merged into 32-bit or [64-bit Windows Installer](64-bit-windows-installer-packages.md) packages.
-   A 64-bit merge module can be merged into a 64-bit package on a 32-bit operating system.

Adhere to the following when authoring a 64-bit merge module:

-   Use the same general procedure as when authoring 32-bit merge modules. For information, see [About Merge Modules](about-merge-modules.md) and [Authoring Merge Modules](authoring-merge-modules.md).
-   You must set the [**Template Summary**](template-summary.md) property with the Intel64 value if running an Intel64 system. You must set the **Template Summary** property with the x64 value if running an x64 system. For information see [Merge Module Summary Information Stream Reference](merge-module-summary-information-stream-reference.md).
-   When both 32-bit and 64-bit merge modules exist for the same component, it is recommended that the modules have different signatures. This will enable a package to contain both versions of the component.

For more information, see [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md).

 

 



